import json
import re
from django.shortcuts import render, reverse, redirect
from bbs.models import Post, Classification
from django.core.paginator import Paginator
from means.views import create_related_tree, create_related_list
from user.views import check_authority, check_frequent, check_author
from notice.views import send_notifications


def bbs(request):
    if request.method == 'GET':
        page_num = request.GET.get('page', '1')
        post = Post.objects.filter(parent_post__isnull=True)
        paginator = Paginator(post, 30)
        page = paginator.get_page(int(page_num))
        return render(request, 'bbs.html', {'page_object_list': list(page.object_list),
                                            'total_num': paginator.count,
                                            'total_page_num': paginator.num_pages,
                                            'page_num': page.number})
    else:
        return render(request, 'error_400.html', status=400)


def view_post(request):
    if request.method == 'GET':
        post_id = request.GET.get('post_id', '')
        comment_id = request.GET.get('comment_id', '')
        try:
            post = Post.objects.get(id=post_id)
        except:
            return render(request, 'error_403.html', status=403)
        related_post_list = Post.objects.filter(parent_post__isnull=False, related_post__iregex=r'\D%s\D' % post_id).order_by("create_datetime")
        fields = "'id', 'content', 'user__username', 'create_datetime', 'parent_post__user__username', 'related_post'"
        # 将多级结构转成树形结构
        related_post_list = create_related_tree(related_post_list, fields, post.id, 'related_post', 'id', "create_datetime")
        return render(request, 'view_post.html', {'post': post, 'related_post_list': related_post_list, "comment_id": comment_id})
    else:
        return render(request, 'error_400.html', status=400)


@check_authority
@check_frequent(Post)
def add_comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id', '')
        try:
            post = Post.objects.get(id=post_id)
        except:
            return render(request, 'error_403.html', status=403)
        content = request.POST.get('content', '')
        pattern = re.compile("^@([A-Za-z0-9\u4E00-\u9FA5]+):(.*)")
        related_content = pattern.findall(content)
        if related_content:
            related_post_username = related_content[0][0]
            content = related_content[0][1]
            related_post_id = request.POST.get('related_post_id', '')
            try:
                related_post = Post.objects.get(id=related_post_id)
            except:
                return render(request, 'error_403.html', status=403)
            if related_post.user.username != related_post_username:
                return render(request, 'error_custom.html', {"msg": "回复对象错误"})
            comment = Post.objects.create(content=content, user=request.user, parent_post=related_post)
        else:
            comment = Post.objects.create(content=content, user=request.user, parent_post=post)
        related_list = json.dumps(create_related_list(comment.id, comment.parent_post, "parent_post"))
        comment.related_post = related_list
        comment.save()
        send_notifications(sender=request.user, recipient=comment.parent_post.user, verb="在论坛中评论了您的帖子", target=post, action_object=comment)
        # return redirect(reverse('bbs:view_post', kwargs={'post_id': post_id}))  # 传递url/参数值
        return redirect(reverse('bbs:view_post') + '?%s=%s' % ('post_id', post_id))  # 传递url?参数=参数值
    else:
        return render(request, 'error_400.html', status=400)


@check_authority
@check_frequent(Post)
def add_post(request):
    if request.method == 'POST':
        classification_id = request.POST.get('classification_id', '')
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        if not all([classification_id, title, content]):
            return render(request, 'error_custom.html', {'msg': '提交内容不能为空'})
        try:
            classification = Classification.objects.get(id=classification_id)
        except:
            return render(request, 'error_403.html', status=403)
        post = Post.objects.create(classification=classification, title=title, content=content, user=request.user)
        related_list = json.dumps(create_related_list(post.id, post.parent_post, "parent_post"))
        post.related_post = related_list
        post.save()
        return redirect(reverse('bbs:view_post') + "?post_id=%s" % post.id)
    else:
        classification = Classification.objects.all()
        return render(request, 'add_post.html', {"classification": classification})


@check_authority
@check_author(Post)
@check_frequent(Post)
def edit_post(request):
    if request.method == 'GET':
        post_id = request.GET.get('post_id', '')
        if not post_id:
            return render(request, 'error_403.html', status=403)
        try:
            post = Post.objects.get(id=post_id)
        except:
            return render(request, 'error_403.html', status=403)
        classification = Classification.objects.all()
        return render(request, 'add_post.html', {"post": post, "classification": classification})
    else:
        classification_id = request.POST.get('classification_id', '')
        post_id = request.POST.get('post_id', '')
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        if not all([classification_id, post_id, title, content]):
            return render(request, 'error_custom.html', {'msg': '提交内容不能为空'})
        try:
            classification = Classification.objects.get(id=classification_id)
            post = Post.objects.get(id=post_id)
        except:
            return render(request, 'error_403.html', status=403)
        post.classification = classification
        post.title = title
        post.content = content
        post.user = request.user
        related_list = json.dumps(create_related_list(post.id, post.parent_post, "parent_post"))
        post.related_post = related_list
        post.save()
        return redirect(reverse('bbs:view_post') + "?post_id=%s" % post_id)

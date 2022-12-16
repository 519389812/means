from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from notifications.signals import notify
from user.models import User
from user.views import check_authority, check_is_superuser


def send_notifications(sender, verb, recipient, target=None, description=None, **kwargs):
    """
        这里原本放的是上文各个参数的说明
        actor(发件人)：任何类型的对象。（必需）如果打算使用关键字参数，要使用sender
        recipient(收件人)： 一组或一个用户查询集或列表的用户（必需的）。
        verb(动作)： 一个字符串（必需的）。
        action_object：任何类型的对象（可选的）。
        target(目标)：任何类型的对象（可选的）。
        level(等级)：Notification.LEVELS ('success', 'info', 'warning', 'error') 之一（可选的）。
        description(描述)： 一个字符串（可选的）。
        public(公共的)：一个布尔值（默认值=True）（可选的）。
        timestamp(时间戳)
    """
    notify.send(sender=sender, recipient=recipient, verb=verb, target=target, description=description, **kwargs)


def show_notice(request):
    unread_list = request.user.notifications.unread()
    read_list = request.user.notifications.read()
    return render(request, "notice_list.html", {"read_list": read_list, "unread_list": unread_list})


def mark_notice_as_read(request):
    if request.method == "GET":
        # 获取未读消息
        notice_id = request.GET.get('notice_id', '')
        # 更新单条通知
        if notice_id:
            try:
                request.user.notifications.get(id=notice_id).mark_as_read()
                return redirect(request.user.notifications.get(id=notice_id))
            except:
                return redirect('notice:show_notice')
        # 更新全部通知
        else:
            request.user.notifications.mark_all_as_read()
            return redirect('notice:show_notice')
    else:
        return render(request, 'notice_list.html')


# ListView的实现方式，暂未使用
class NoticeListView(LoginRequiredMixin, ListView):
    """通知列表"""
    # 上下文的名称
    context_object_name = 'notices'
    # 模板位置
    template_name = 'notice_list.html'
    # 登录重定向
    login_url = '/login/'

    # 未读通知的查询集
    def get_queryset(self):
        return self.request.user.notifications.unread()


class MarkNoticeAsReadView(View):
    """更新通知状态"""
    # 处理 get 请求
    def get(self, request):
        # 获取未读消息
        notice_id = request.GET.get('notice_id')
        # 更新单条通知
        if notice_id:
            try:
                request.user.notifications.get(id=notice_id).mark_as_read()
                return redirect(request.user.notifications.get(id=notice_id))
            except:
                return redirect('notice:show_notice')
        # 更新全部通知
        else:
            request.user.notifications.mark_all_as_read()
            return redirect('notice:show_notice')


@check_authority
@check_is_superuser
def send_notice(request):
    if request.method == "POST":
        recipient = request.POST.get("recipient", "")
        content = request.POST.get("content", "")
        if not all([recipient, content]):
            return render(request, 'send_notice.html', {"msg": "存在未填写的字段"})
        if recipient == 'superuser':
            users = User.objects.filter(is_superuser=False)
        elif recipient == 'self':
            users = request.user
        else:
            users = User.objects.all()
        if users:
            send_notifications(sender=request.user, recipient=users, verb=content, target=None, description=None)
            return render(request, 'send_notice.html', {"msg": "发送成功"})
        else:
            return render(request, 'send_notice.html', {"msg": "未找到发送目标"})
    else:
        return render(request, 'send_notice.html')

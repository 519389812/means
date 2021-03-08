from django.shortcuts import render
from collection.models import Classification, Collection, Rate, Comment
from collections import OrderedDict
from django.db.models import Avg
from user.views import check_authority, check_frequent, check_bot, check_unique


def collection(request):
    if request.method == "GET":
        collection_object_dict = OrderedDict()
        classification_list = list(Classification.objects.all().values_list('name', flat=True).order_by('name'))
        for classification in classification_list:
            collection_object_dict[classification] = list(Collection.objects.filter(classification__name=classification).values('id', 'name', 'url', 'content'))
            for collection_object in collection_object_dict[classification]:
                score_avg = Rate.objects.filter(collection__name=collection_object['name']).aggregate(Avg('score'))['score__avg']
                collection_object['score'] = score_avg if score_avg else 0
                collection_object['score_count'] = Rate.objects.filter(collection__name=collection_object['name']).count()
                star_fill = round(collection_object['score'])
                collection_object['star_fill'] = range(star_fill)
                collection_object['star_empty'] = range(5 - star_fill)
        return render(request, "collection.html", {'content': collection_object_dict})
    else:
        return render(request, "error_500.html", status=500)


def collection_details(request, id):
    if request.method == "GET":
        collection_object = Collection.objects.filter(id=id).values('id', 'name', 'url', 'content')[0]
        rate_object_list = list(Rate.objects.filter(collection__id=id).values('user', 'score', 'content', 'create_datetime'))
        for rate_object in rate_object_list:
            rate_object['comment'] = list(Comment.objects.filter(rate__id=rate_object['id']).values('id', 'user', 'content', 'create_datetime'))
        return render(request, "collection_details.html", {'content': collection_object, 'rate_content': rate_object_list})
    else:
        return render(request, "error_500.html", status=500)


def get_user_ip(request):
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        return request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0]
    else:
        return request.META.get('REMOTE_ADDR').split(',')[0]


@check_bot
@check_authority
@check_unique
@check_frequent
def rate(request):
    if request.method == "POST":
        collection_id = request.POST.get('collection', '')
        score = request.POST.get('score', '')
        content = request.POST.get('content', '')
        ip = get_user_ip(request)
        try:
            collection = Collection.objects.get(id=collection_id)
        except:
            return render(request, "error_500.html", status=500)
        Rate.objects.create(collection=collection, user=request.user, score=score, content=content, ip=ip)
        collection_object = collection.values('id', 'name', 'url', 'content')
        rate_object_list = list(Rate.objects.filter(collection=collection).values('id', 'user', 'score', 'content', 'create_datetime'))
        for rate_object in rate_object_list:
            rate_object['comment'] = list(Comment.objects.filter(rate__id=rate_object['id']).values('id', 'user', 'content', 'create_datetime'))
        return render(request, "collection_details.html", {'content': collection_object, 'rate_content': rate_object_list})
    else:
        return render(request, "error_500.html", status=500)


@check_bot
@check_authority
@check_frequent
def comment(request):
    if request.method == "POST":
        rate_id = request.POST.get('rate', '')
        content = request.POST.get('content', '')
        ip = get_user_ip(request)
        try:
            rate = Rate.objects.get(id=rate_id)
        except:
            return render(request, "error_500.html", status=500)
        Comment.objects.create(rate=rate, user=request.user, content=content, ip=ip)
        collection_object = rate.collection.values('id', 'name', 'url', 'content')
        rate_object_list = list(Rate.objects.filter(collection=rate.collection).values('id', 'user', 'score', 'content', 'create_datetime'))
        for rate_object in rate_object_list:
            rate_object['comment'] = list(Comment.objects.filter(rate__id=rate_object['id']).values('id', 'user', 'content', 'create_datetime'))
        return render(request, "collection_details.html", {'content': collection_object, 'rate_content': rate_object_list})
    else:
        return render(request, "error_500.html", status=500)

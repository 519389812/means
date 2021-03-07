from django.shortcuts import render
from collection.models import Classification, Collection, Rate
from collections import OrderedDict
from django.db.models import Avg


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
        print(collection_object)
        return render(request, "collection_details.html", {'content': collection_object})
    else:
        return render(request, "error_500.html", status=500)
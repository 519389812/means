from django.shortcuts import render
from collection.models import Classification, Collection, Rate
from collections import OrderedDict
from django.db.models import Avg


def collection(request):
    if request.method == "GET":
        collection_object_dict = OrderedDict()
        classification_list = list(Classification.objects.all().values_list('name', flat=True).order_by('name'))
        for classification in classification_list:
            collection_object_dict[classification] = Collection.objects.filter(classification__name=classification).values('name', 'url', 'content')
            collection_object_dict[classification]['score'] = Rate.objects.filter(collection__name=collection_object_dict[classification]['name']).aggregate(Avg('score'))
            collection_object_dict[classification]['score_count'] = Rate.objects.filter(collection__name=collection_object_dict[classification]['name']).count()
            collection_object_dict[classification]['star_fill'] = range(round(collection_object_dict[classification]['score']))
            collection_object_dict[classification]['star_empty'] = range(5 - collection_object_dict[classification]['star_fill'])
        return render(request, "home.html", {'content': collection_object_dict})
    else:
        return render(request, "error_500.html", status=500)

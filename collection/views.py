from django.shortcuts import render
from collection.models import Classification, Collection
from collections import OrderedDict


def collection(request):
    if request.method == "GET":
        collection_object_dict = OrderedDict()
        classification_list = list(Classification.objects.all().values_list('name', flat=True).order_by('name'))
        for classification in classification_list:
            collection_object_dict[classification] = Collection.objects.filter(classification__name=classification).values('name', 'url', 'content')
        print(collection_object_dict)
        return render(request, "home.html", {'content': collection_object_dict})
    else:
        return render(request, "error_500.html", status=500)

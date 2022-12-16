from django.urls import path, re_path, include
from . import views

app_name = "collection"

urlpatterns = [
    path('', views.collection, name="collection"),
    re_path(r'collection_details/(.*)/$', views.collection_details, name="collection_details"),
    path('rate/', views.rate, name='collection_rate'),
    path('rate/comment/', views.comment, name='collection_rate_comment'),
    path(r'show_download/', views.show_download, name='show_download'),
]

from django.urls import path, re_path, include
from . import views

app_name = "search"


urlpatterns = [
    path('search/', views.search, name="search"),
    path('search_pan/', views.search_pan, name='search_pan'),
    re_path(r'search_pan/declare/(.+)/(.+)/(.+)$', views.show_declare_pan, name='show_declare_pan'),
    path('search_pan/jump/', views.jump_to_pan, name='jump_to_pan'),
    path('search_magnet/', views.search_magnet, name='search_magnet'),
    re_path(r'search_magnet/details/(.+)/(.+)$', views.show_details_magnet, name='show_details_magnet'),
    path('search_movie/', views.search_movie, name='search_movie'),
    path('search_movie/details/', views.show_details_movie, name='show_details_movie'),
]
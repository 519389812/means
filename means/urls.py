"""means URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
import means.views as main_views
from means.views import error_404, error_400, error_403, error_500
import notifications.urls

# ckeditor
from django.views import static
from django.conf import settings
from django.conf.urls import url

handler404 = error_404
handler400 = error_400
handler403 = error_403
handler500 = error_500

urlpatterns = [
    # ckeditor
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),

    # main
    path('admin/', admin.site.urls),
    path('', main_views.home, name="home"),
    path('home/', main_views.home, name="home"),
    path('error_404/', main_views.error_404, name="error_404"),
    path('error_400/', main_views.error_400, name="error_400"),
    path('error_403/', main_views.error_403, name="error_403"),
    path('error_500/', main_views.error_500, name="error_500"),
    path('error_404_clean/', main_views.error_404_clean, name="error_404_clean"),
    path('error_400_clean/', main_views.error_400_clean, name="error_400_clean"),
    path('error_403_clean/', main_views.error_403_clean, name="error_403_clean"),
    path('error_500_clean/', main_views.error_500_clean, name="error_500_clean"),
    path('error_not_accessible/', main_views.error_not_accessible, name="error_not_accessible"),
    path('error_too_frequent/', main_views.error_too_frequent, name="error_too_frequent"),
    path('error_same_operation/', main_views.error_same_operation, name="error_same_operation"),
    path('release_show/', main_views.release_show, name="release_show"),
    path('copyright_show/', main_views.copyright_show, name="copyright_show"),
    path('agreement_show/', main_views.agreement_show, name="agreement_show"),

    # search
    path("search/", include("search.urls", namespace="search")),

    # user
    path("user/", include("user.urls", namespace="user")),

    # collection
    path("collection/", include("collection.urls", namespace="collection")),

    # bbs
    path("bbs/", include("bbs.urls", namespace="bbs")),

    # notice
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path("notice/", include("notice.urls", namespace="notice")),
]

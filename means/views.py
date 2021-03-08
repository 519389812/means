from django.shortcuts import render
import os
import base64
from urllib import parse
from django.shortcuts import render
from django.http import *


def home(request):
    return render(request, 'collection.html')


def error_404(request, exception='', template_name='templates/error_404.html'):
    return render(request, "error_404.html")


def error_400(request, exception='', template_name='templates/error_400.html'):
    return render(request, "error_400.html")


def error_403(request, exception='', template_name='templates/error_403.html'):
    return render(request, "error_403.html")


def error_500(request):
    return render(request, "error_500.html")


def error_404_clean(request, exception='', template_name='templates/error_404_clean.html'):
    return render(request, "error_404_clean.html")


def error_400_clean(request, exception='', template_name='templates/error_400_clean.html'):
    return render(request, "error_400_clean.html")


def error_403_clean(request, exception='', template_name='templates/error_403_clean.html'):
    return render(request, "error_403_clean.html")


def error_500_clean(request):
    return render(request, "error_500_clean.html")


def error_not_accessible(request):
    return render(request, "error_not_accessible.html")


def error_too_frequent(request):
    return render(request, "error_too_frequent.html")


def error_same_operation(request):
    return render(request, "error_same_operation.html")


def release_show(request):
    return render(request, "release_show.html")


def copyright_show(request):
    return render(request, "copyright_show.html")


def agreement_show(request):
    return render(request, "agreement_show.html")


# 解析url中的参数
def parse_url_param(url):
    url_content = parse.urlparse(url)
    query_dict = parse.parse_qs(url_content.query)
    return query_dict

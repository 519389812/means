from django.shortcuts import render, redirect, reverse
import json
from urllib import parse
from django.forms.models import model_to_dict


def home(request):
    return redirect(reverse("collection:collection"))


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
    return render(request, "agreement.html")


# 解析url中的参数
def parse_next_url(http_referer, query_string, next_param="next"):
    """
    :param http_referer: 解析跳转前网页url
    :param query_string: 解析跳需要跳转到的url
    :param next_param: query_string中跳转到的网页参数名
    :return: origin_url, next_url, next_url_with_params
    """
    url_content = parse.urlparse(http_referer)
    url_referer_query = parse.parse_qs(url_content.query)
    origin_url = url_content.path
    url_content = parse.urlparse(query_string)
    url_query_path = parse.parse_qs(url_content.path)
    url_query_query = parse.parse_qs(url_content.query)
    url_query = dict(url_query_path, **url_query_query, **url_referer_query)
    if url_query.get(next_param, ""):
        next_url = url_query.get(next_param, "")[0]
        del(url_query[next_param])
    else:
        next_url = origin_url
    query_string = parse.urlencode(url_query, doseq=True)
    query_string = "?" + query_string if query_string else query_string
    return origin_url, next_url, query_string


def create_related_list(node_id, parent_object, parent_object_string):
    related_list = [node_id]
    while True:
        try:
            related_list.insert(0, parent_object.id)
            parent_object = eval("parent_object.%s" % parent_object_string)
        except:
            return related_list


# 解析[{},{}]格式数据为树结构
def create_related_tree(data_queryset, fields, root_value, related_field, node_field, order_field):
    """
    :param data:  queryset被解析的数据
    :param root_value: 根节点值
    :param related_field: 关系字段名称
    :param node_field: 当前节点定位字段名称
    :return: list
    """

    related_tree = []
    data_dict = eval("data_queryset.values(%s)" % fields)
    for i in data_dict:
        related_post_list = json.loads(i[related_field])
        if len(related_post_list) == 2:
            related_tree.append(i)
    for i in related_tree:
        related_data = data_queryset.filter(related_post__iregex=(r'\D%s\D+%s\D+\d+.*' % (root_value, i[node_field]))).order_by(order_field)
        i['children'] = eval("related_data.values(%s)" % fields)
    return related_tree

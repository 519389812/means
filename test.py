from urllib import parse

def parse_next_url(http_referer, query_string, next_param="next"):
    """
    :param http_referer: 解析跳转前网页url
    :param query_string: 解析跳需要跳转到的url
    :param next_param: query_string中跳转到的网页参数名
    :param with_params: 是否把所有query_string继续传递到下一个页面
    :return: origin_url, next_url, next_url_with_params
    """
    print("http_referer:", http_referer)
    print("query_string:", query_string)
    url_content = parse.urlparse(http_referer)
    origin_url = url_content.path
    url_content = parse.urlparse(query_string)
    url_query_path = parse.parse_qs(url_content.path)
    url_query_query = parse.parse_qs(url_content.query)
    url_query = dict(url_query_path, **url_query_query)
    if url_query.get(next_param, ""):
        next_url = url_query.get(next_param, "")[0]
        del(url_query[next_param])
        query_string = parse.urlencode(url_query, doseq=True)
    else:
        next_url = origin_url
    query_string = "?" + query_string if query_string else query_string
    print("origin_url:", origin_url)
    print("next_url:", next_url)
    print("query_string:", query_string)
    return origin_url, next_url, query_string


parse_next_url("http://127.0.0.1:8000/collection/collection_details/1/", "&next=/collection/collection_details/1/")
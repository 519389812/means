from django.shortcuts import render, redirect
import requests
import random
from bs4 import BeautifulSoup
from urllib import parse
import re
import faker
import configparser
from means.settings import config_file


fake = faker.Faker()
config = configparser.ConfigParser()
config.read(config_file)


def search(request):
    return render(request, "search.html")


user_agents = ['Mozilla/5.0 (Linux; Android 9; JKM-AL00 Build/HUAWEIJKM-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045118 Mobile Safari/537.36 MMWEBID/2787 MicroMessenger/7.0.12.1620(0x27000C34) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 8.1.0; vivo Y83A Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045111 Mobile Safari/537.36 MMWEBID/8248 MicroMessenger/7.0.12.1620(0x27000C35) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 9; ELE-AL00 Build/HUAWEIELE-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045130 Mobile Safari/537.36 MMWEBID/8968 MicroMessenger/7.0.4.1420(0x2700043C) Process/tools NetType/4G Language/zh_CN',
               'Mozilla/5.0 (Linux; Android 7.0; KNT-AL10 Build/HUAWEIKNT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045130 Mobile Safari/537.36 MMWEBID/7321 MicroMessenger/7.0.10.1580(0x27000AFE) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 10; LYA-AL00 Build/HUAWEILYA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045130 Mobile Safari/537.36 MMWEBID/9034 MicroMessenger/7.0.12.1620(0x27000C34) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 9; MAR-TL00 Build/HUAWEIMAR-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045130 Mobile Safari/537.36 MMWEBID/2964 MicroMessenger/7.0.12.1620(0x27000C34) Process/tools NetType/4G Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 8.1.0; M1813 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045033 Mobile Safari/537.36 MMWEBID/4612 MicroMessenger/7.0.12.1620(0x27000C35) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 8.1.0; vivo Y85A Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045111 Mobile Safari/537.36 MMWEBID/4462 MicroMessenger/7.0.12.1620(0x27000C35) Process/tools NetType/4G Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 9; PCNM00 Build/PKQ1.190630.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045111 Mobile Safari/537.36 MMWEBID/8346 MicroMessenger/7.0.11.1600(0x27000B35) Process/tools NetType/4G Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 9; V1836A Build/PKQ1.181030.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045111 Mobile Safari/537.36 MMWEBID/4281 MicroMessenger/7.0.10.1580(0x27000AFF) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 9; ASK-AL00x Build/HONORASK-AL00x; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045118 Mobile Safari/537.36 MMWEBID/6434 MicroMessenger/7.0.12.1620(0x27000C34) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 9; PCNM00 Build/PKQ1.190630.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045129 Mobile Safari/537.36 MMWEBID/1926 MicroMessenger/7.0.12.1620(0x27000C35) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 9; BLA-AL00 Build/HUAWEIBLA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045130 Mobile Safari/537.36 MMWEBID/4087 MicroMessenger/7.0.12.1620(0x27000C34) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 9; ELE-AL00 Build/HUAWEIELE-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045130 Mobile Safari/537.36 MMWEBID/8968 MicroMessenger/7.0.4.1420(0x2700043C) Process/tools NetType/WIFI Language/zh_CN',
               'Mozilla/5.0 (Linux; Android 9; GLK-AL00 Build/HUAWEIGLK-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045130 Mobile Safari/537.36 MMWEBID/9365 MicroMessenger/7.0.12.1620(0x27000C34) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 8.1.0; vivo X20A Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045129 Mobile Safari/537.36 MMWEBID/4501 MicroMessenger/7.0.12.1620(0x27000C35) Process/tools NetType/4G Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 8.1.0; PBEM00 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045129 Mobile Safari/537.36 MMWEBID/3371 MicroMessenger/7.0.12.1620(0x27000C35) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 10; VOG-TL00 Build/HUAWEIVOG-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045130 Mobile Safari/537.36 MMWEBID/8723 MicroMessenger/7.0.12.1620(0x27000C34) Process/tools NetType/4G Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.11(0x17000b21) NetType/WIFI Language/zh_CN',
               'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.11(0x17000b21) NetType/4G Language/zh_CN',
               'Mozilla/5.0 (Linux; Android 10; LIO-AL00 Build/HUAWEILIO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/1169 MMWEBSDK/200201 Mobile Safari/537.36 MMWEBID/4329 MicroMessenger/7.0.12.1620(0x27000C35) Process/tools NetType/4G Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 9; HMA-AL00 Build/HUAWEIHMA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045118 Mobile Safari/537.36 MMWEBID/2629 MicroMessenger/7.0.12.1620(0x27000C34) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 10; LYA-AL00 Build/HUAWEILYA-AL00L; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045118 Mobile Safari/537.36 MMWEBID/7246 MicroMessenger/7.0.12.1620(0x27000C34) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 10; VOG-AL00 Build/HUAWEIVOG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/45016 Mobile Safari/537.36 MMWEBID/3894 MicroMessenger/7.0.12.1620(0x27000C34) Process/tools NetType/4G Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 10; LIO-AN00 Build/HUAWEILIO-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045130 Mobile Safari/537.36 MMWEBID/8475 MicroMessenger/7.0.12.1620(0x27000C34) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 9; V1913A Build/P00610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045111 Mobile Safari/537.36 MMWEBID/8326 MicroMessenger/7.0.12.1620(0x27000C35) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 9; INE-TL00 Build/HUAWEIINE-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045118 Mobile Safari/537.36 MMWEBID/1176 MicroMessenger/7.0.11.1600(0x27000B32) Process/tools NetType/4G Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/1171 MMWEBSDK/191201 Mobile Safari/537.36 MMWEBID/49 MicroMessenger/7.0.11.1600(0x27000B33) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 9; VOG-AL00 Build/HUAWEIVOG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/1168 MMWEBSDK/191201 Mobile Safari/537.36 MMWEBID/268 MicroMessenger/7.0.11.1600(0x27000B32) Process/tools NetType/4G Language/zh_CN ABI/arm64',
               'Mozilla/5.0 (Linux; Android 9; ELE-AL00 Build/HUAWEIELE-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045118 Mobile Safari/537.36 MMWEBID/3123 MicroMessenger/7.0.4.1420(0x27000437) Process/tools NetType/4G Language/zh_CN',
               'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
               'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
               'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
               'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
               ]

pan_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
}


pan_authority = 'mso.pansoso.com'
pan_to_authority = 'to.pansoso.com'
pan_url = 'https://mso.pansoso.com/'
pan_url_search = 'https://mso.pansoso.com/zh/'
pan_url_redirect = 'http://to.pansoso.com/'


def search_pan(request):
    if request.method == 'POST':
        search_string = request.POST.get('search_string', '')
        pan_headers['authority'] = pan_authority
        pan_headers['method'] = 'GET'
        pan_headers['scheme'] = 'https'
        pan_headers['user-agent'] = user_agents[random.randint(0, len(user_agents)-1)]
        pan_headers['path'] = 'zh/' + parse.quote(search_string)
        response = requests.get(pan_url + 'zh/' + parse.quote(search_string), headers=pan_headers)
        if response.ok:
            html = response.content.decode()
            regex = re.compile(r'.+_\d+$')
            if regex.match(search_string):
                search_string = search_string.rsplit('_', 1)[0]
            # html = open('test_pan_1.html', 'r', encoding='utf-8')
            soup = BeautifulSoup(html, 'lxml')
            # html.close()
            tags = soup.find('div', id='con')
            if not tags:
                return render(request, 'error_500.html')
            content_tags = tags.find_all('a', attrs={'class': None})
            content = []
            if len(content_tags) == 0:
                return render(request, 'error_500.html')
            elif len(content_tags) == 1 and content_tags[0]['href'] == 'javascript:location.reload();':
                return render(request, 'search_list_pan.html', {'search_string': search_string, 'tab_name': 'cloud_disk_tab', 'content': content})
            else:
                for content_tag in content_tags:
                    href = parse.urlparse(content_tag['href']).path
                    title = content_tag.find('h2').text
                    details = content_tag.find('div', attrs={'class': 'des'}).text
                    content.append((href, title, details))
                page_up_href = parse.unquote(parse.urlparse(tags.find('a', attrs={'class': 's'})['href']).path.lstrip('/').split('/', 1)[-1]) if tags.find('a', attrs={'class': 's'}) else ''
                page_string = tags.find('span', attrs={'class': 'y'}).text if tags.find('span', attrs={'class': 'y'}) else ''
                page_down_href = parse.unquote(parse.urlparse(tags.find('a', attrs={'class': 'x'})['href']).path.lstrip('/').split('/', 1)[-1]) if tags.find('a', attrs={'class': 'x'}) else ''
                return render(request, 'search_list_pan.html', {'search_string': search_string, 'tab_name': 'cloud_disk', 'content': content, 'page_up_href': page_up_href, 'page_string': page_string, 'page_down_href': page_down_href})
        else:
            return render(request, 'error_500.html')
    else:
        return render(request, 'error_400.html')


def show_declare_pan(request, search_string, quote, details_id):
    if request.method == 'GET':
        pan_headers['authority'] = pan_authority
        pan_headers['method'] = 'GET'
        pan_headers['path'] = '/' + quote + '/' + details_id
        pan_headers['scheme'] = 'https'
        pan_headers['referer'] = pan_url_search + parse.quote(search_string)
        pan_headers['user-agent'] = user_agents[random.randint(0, len(user_agents)-1)]
        response = requests.get(pan_url + quote + '/' + details_id, headers=pan_headers)
        html = response.content.decode()
        soup = BeautifulSoup(html, 'lxml')
        # html = open('test_pan_second_page.html', 'r', encoding='utf-8')
        # soup = BeautifulSoup(html, 'lxml')
        # html.close()
        href = soup.find('a', id='down_button_link')['href']
        url_parse = parse.urlparse(href)
        pan_headers['path'] = url_parse.path + '?' + url_parse.query
        pan_headers['referer'] = pan_url + quote + '/' + details_id
        response = requests.get(href, headers=pan_headers)
        html = response.content.decode()
        soup = BeautifulSoup(html, 'lxml')
        # html = open('test_pan_third_page.html', 'r', encoding='utf-8')
        # soup = BeautifulSoup(html, 'lxml')
        # html.close()
        tags = soup.find('div', attrs={'class': 'url'})
        href = parse.urlparse(tags.find('a')['href']).query
        code = tags.find('p').text
        return render(request, 'search_declare_pan.html', {'href': href, 'code': code})
    else:
        return render(request, 'error_400.html')


def jump_to_pan(request):
    if request.method == 'GET':
        href = request.get_full_path()
        url = pan_url_redirect + '?' + parse.urlparse(href).query
        pan_headers['host'] = pan_to_authority
        return redirect(url, headers=pan_headers)
    else:
        return render(request, 'error_400.html')


options = config.options('mn')
magnet_urls = []
for i in range(len(options)):
    magnet_urls.append(config.get("mn", options[i]))


magnet_headers = {
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
}


def refresh_magnet_url(url):
    magnet_headers['authority'] = parse.urlparse(url).netloc
    magnet_headers['path'] = '/'
    magnet_headers['user-agent'] = fake.user_agent()
    response = requests.get(url, headers=magnet_headers)
    html = response.content.decode()
    soup = BeautifulSoup(html, 'lxml')
    tags = soup.find('div', attrs={'class': 'links'})
    if tags:
        tags = tags.find_all('a')
        if len(tags) > 0:
            magnet_urls = []
            config.remove_section("mg")
            with open(config_file, "w+") as f:
                config.write(f)
            config.add_section("mg")
            i = 0
            for tag in tags:
                href = tag['href']
                config.set("mg", "url_%s" % i, href)
                magnet_urls.append(href)
                i += 1
            with open(config_file, "w+") as f:
                config.write(f)


def search_magnet(request):
    if request.method == "POST":
        search_string = request.POST.get('search_string', '')
        need_refresh = False
        for i in range(len(magnet_urls)):
            magnet_url = magnet_urls[i]
            if need_refresh:
                refresh_magnet_url(magnet_url)
                need_refresh = False
            magnet_headers['authority'] = parse.urlparse(magnet_url).netloc
            magnet_headers['referer'] = magnet_url + '/'
            magnet_headers['user-agent'] = fake.user_agent()
            magnet_headers['sec-fetch-site'] = 'same-origin'
            search_path = '/search?q=%s' % search_string
            magnet_search_url = magnet_url + search_path
            magnet_headers['path'] = search_path
            response = requests.get(magnet_search_url, headers=magnet_headers)
            # html = open('test_bt_2.html', 'r', encoding='utf-8')
            # soup = BeautifulSoup(html, 'lxml')
            # html.close()
            if response.ok:
                html = response.content.decode()
                soup = BeautifulSoup(html, 'lxml')
                tags = soup.find('tbody')
                if not tags:
                    return render(request, 'error_500.html')
                results = tags.find_all('tr')
                content = []
                for result in results:
                    href = result.a['href']
                    title = result.a.text.split()[0]
                    size = result.find('td', attrs={'class': 'td-size'}).text
                    content.append((href, title, size))
                return render(request, 'search_list_magnet.html', {'search_string': search_string, 'tab_name': 'magnet', 'content': content})
            else:
                need_refresh = True
                continue
        return render(request, 'error_500.html')
    else:
        return render(request, 'error_500.html')


def show_details_magnet(request, search_string, details_id):
    if request.method == 'GET':
        need_refresh = False
        for i in range(len(magnet_urls)):
            magnet_url = magnet_urls[i]
            if need_refresh:
                refresh_magnet_url(magnet_url)
                need_refresh = False
            magnet_headers['authority'] = parse.urlparse(magnet_url).netloc
            magnet_headers['path'] = '/' + details_id
            magnet_headers['referer'] = magnet_url + '/search?q=%s' % search_string
            magnet_headers['user-agent'] = fake.user_agent()
            magnet_headers['sec-fetch-site'] = 'same-origin'
            response = requests.get(magnet_url + '/' + details_id, headers=magnet_headers)
            if response.ok:
                html = response.content.decode()
                soup = BeautifulSoup(html, 'lxml')
            # html = open('test_bt_3.html', 'r', encoding='utf-8')
            # soup = BeautifulSoup(html, 'lxml')
            # html.close()
                href = soup.find('input', id='input-magnet')['value']
                title = soup.find('h2', attrs={'class': 'magnet-title'}).text
                details = ' '.join([tag.text for tag in soup.find('dl').find_all(['dt', 'dd'], limit=6)])
                return render(request, 'search_details_magnet.html', {'href': href, 'title': title, 'details': details})
            else:
                need_refresh = True
                continue
        return render(request, 'error_500.html')
    else:
        return render(request, 'error_500.html')


movie_url = "http://m.codesea.xyz/"


movie_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'connection': 'keep-alive',
    'host': parse.urlparse(movie_url).netloc,
    'upgrade-insecure-requests': '1',
}


def search_movie(request):
    if request.method == "POST":
        search_string = request.POST.get('search_string', '')
        movie_headers['user-agent'] = fake.user_agent()
        regex = re.compile(r'.+paged=\d+$')
        if regex.match(search_string):
            movie_search_url = movie_url + '?' + search_string
            search_params = parse.parse_qs(search_string)
            search_string = search_params['s'][0]
        else:
            if re.compile(r'^s=.+$').match(search_string):
                search_params = parse.parse_qs(search_string)
                search_string = search_params['s'][0]
                movie_search_url = movie_url + '?s=%s' % search_string
            else:
                movie_search_url = movie_url + '?s=%s' % search_string
        response = requests.get(movie_search_url, headers=movie_headers)
        # html = open('test_movie_1.html', 'r', encoding='utf-8')
        # soup = BeautifulSoup(html, 'lxml')
        # html.close()
        if response.ok:
            html = response.content.decode()
            soup = BeautifulSoup(html, 'lxml')
            tags = soup.find('ul', id='post_container')
            if not tags:
                return render(request, 'error_500.html')
            results = tags.find_all('li')
            content = []
            for result in results:
                href = parse.urlparse(result.find('a')['href']).query
                title = result.find('a')['title']
                details = result.find('div', attrs={'class': 'info'}).text.rstrip().replace('\n', ' %s:').lstrip() % ('日期', '播放', '评价', '类型')
                content.append((href, title, details))
            page_up_href = parse.unquote(parse.urlparse(soup.find('a', attrs={'class': 'prev'})['href']).query) if soup.find('a', attrs={'class': 'prev'}) else ''
            page_string = soup.find('a', attrs={'class': 'current'}).text if soup.find('a', attrs={'class': 'current'}) else ''
            page_down_href = parse.unquote(parse.urlparse(soup.find('a', attrs={'class': 'next'})['href']).query) if soup.find('a', attrs={'class': 'next'}) else ''
            return render(request, 'search_list_movie.html', {'search_string': search_string, 'tab_name': 'movie', 'content': content, 'page_up_href': page_up_href, 'page_string': page_string, 'page_down_href': page_down_href})
        else:
            return render(request, 'error_500.html')
    else:
        return render(request, 'error_500.html')


def show_details_movie(request):
    if request.method == 'GET':
        details_id = parse.urlparse(request.get_full_path()).query
        movie_headers['user-agent'] = fake.user_agent()
        response = requests.get(movie_url + '?' + details_id, headers=movie_headers)
        if response.ok:
            html = response.content.decode()
            soup = BeautifulSoup(html, 'lxml')
            # html = open('test_movie_3.html', 'r', encoding='utf-8')
            # soup = BeautifulSoup(html, 'lxml')
            # html.close()
            tags = soup.find('div', id='post_content')
            if tags:
                results = tags.find_all('p')
                content = []
                title = soup.find('h1').text
                try:
                    i = 0
                    for result in results:
                        if result.text == '资源列表':
                            if len(results[i:]) > 1:
                                for target in results[i+1:]:
                                    href = target.find('a')['href']
                                    details = target.text.strip()
                                    content.append((href, details))
                                break
                        i += 1
                except:
                    pass
                return render(request, 'search_details_movie.html', {'title': title, 'content': content})
            else:
                return render(request, 'error_500.html')
        else:
            return render(request, 'error_500.html')
    else:
        return render(request, 'error_500.html')

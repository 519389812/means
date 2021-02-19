from django.shortcuts import render
from PIL import Image
import paddlehub as hub
import os
from paddleocr import PaddleOCR, draw_ocr
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import random
import string
import time
import faker
from means.settings import online


fake = faker.Faker()


# lover_words_module = hub.Module(name="ernie_gen_lover_words")


# def generate(request):
#     return render(request, "generate.html")


# def generate_honeyed_words(request):
#     if request.method == 'POST':
#         words = request.POST.get('generate_string', '')
#         if words == "":
#             return render(request, 'error_400.html')
#         words = [words]
#         results = lover_words_module.generate(texts=words, use_gpu=False, beam_width=5)
#         return render(request, "generate_list_honeyed_words.html", {"content": results[0]})
#     else:
#         return render(request, 'error_400.html')


def predict_words(request):
    return render(request, "predict_words.html")


def predict_words_inner(request):
    return render(request, "predict_words_inner.html")


# text_detector = hub.Module(name="chinese_text_detection_db_server")
# ocr = hub.Module(name="chinese_ocr_db_crnn_server")
if online:
    ocr = PaddleOCR(
        det_model_dir='/home/means/means/predict/static/predict/models/ch_ppocr_mobile_v1.1_det_infer',
        rec_model_dir='/home/means/means/predict/static/predict/models/ch_ppocr_mobile_v1.1_rec_infer',
        # rec_char_dict_path='',
        cls_model_dir='/home/means/means/predict/static/predict/models/ch_ppocr_mobile_v1.1_cls_infer',
        use_angle_cls=True,
        lang="ch",  # 中英文、英文、法语、德语、韩语、日语lang参数依次为`ch`, `en`, `french`, `german`, `korean`, `japan`
    )
    image_dir = "/home/means/means/predict/static/predict/images/"
else:
    ocr = PaddleOCR(
        det_model_dir='../models/ch_ppocr_server_v2.0_det_infer',
        rec_model_dir='../models/ch_ppocr_server_v2.0_rec_infer',
        # rec_char_dict_path='',
        cls_model_dir='../models/ch_ppocr_mobile_v2.0_cls_infer',
        use_angle_cls=True,
        lang="ch",  # 中英文、英文、法语、德语、韩语、日语lang参数依次为`ch`, `en`, `french`, `german`, `korean`, `japan`
    )
    image_dir = "predict/static/predict/images/"


def predict_words_inner_atp_image(request):
    if request.method == 'POST':
        try:
            img = request.FILES["img"]
        except:
            img = None
        if img is not None:
            img_name = img.name.lower()
            if img_name.endswith("jpg") or img_name.endswith("jpeg") or img_name.endswith("png"):
                try:
                    img = Image.open(img)
                    img_path = os.path.join(image_dir, img_name)
                    img.save(img_path)
                    result = ocr.ocr(img_path, cls=True)
                    text, confidence = '', 0
                    for line in result:
                        text += line[1][0]
                        confidence += line[1][1]
                    text = text.replace(" ", "")
                    confidence = confidence / len(result) * 100
                    confidence = "%.2f" % confidence + "%"
                    atp_regex = re.compile("ATP-?(?P<atp>\d+)")
                    atp = re.search(atp_regex, text).group('atp') if re.search(atp_regex, text) else ''
                    date_regex = re.compile("from(?P<from>\d{1,2}/?-?(?:[A-Za-z]{3,9}|\d{1,2})/?-?\d{2,4})to(?P<to>\d{1,2}/?-?(?:[A-Za-z]{3,9}|\d{1,2})/?-?\d{2,4})")
                    date_from = re.search(date_regex, text).group('from') if re.search(date_regex, text) else ''
                    date_to = re.search(date_regex, text).group('to') if re.search(date_regex, text) else ''
                    # 显示结果
                    # image = Image.open(img_path).convert('RGB')
                    # boxes = [line[0] for line in result]
                    # txts = [line[1][0] for line in result]
                    # scores = [line[1][1] for line in result]
                    # im_show = draw_ocr(image, boxes, txts, scores, font_path='/path/to/PaddleOCR/doc/simfang.ttf')
                    # im_show = Image.fromarray(im_show)
                    # im_show.save('result.jpg')
                    if os.path.exists(img_path):
                        os.remove(img_path)
                    return render(request, 'predict_words_inner_atp_result.html', {'atp': atp, 'date_from': date_from, 'date_to': date_to, 'confidence': confidence})
                except:
                    return render(request, 'predict_words_inner.html', {'msg': '无效的图片！'})
            else:
                return render(request, 'predict_words_inner.html', {'msg': '图片格式错误，仅支持jpg/jpeg/png图片！'})
        else:
            return render(request, 'predict_words_inner.html', {'msg': '请先选择图片！'})
    else:
        return render(request, 'error_500_clean.html')


atp_url = 'https://capels.caas.gov.sg/atp-check'


def generate_random_str(length=8):
    """
    生成一个指定长度的随机字符串，其中
    string.digits=0123456789
    string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    """
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(length)]
    random_str = ''.join(str_list)
    return random_str


def submit_atp(request):
    if request.method == "POST":
        atp = request.POST.get('atp', '')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        i = 0
        while i <= 2:
            try:
                random_str = generate_random_str(8)
                img_path = image_dir + '%s.png' % random_str
                if online:
                    driver = webdriver.Chrome(options=chrome_options)
                else:
                    driver = webdriver.Chrome(executable_path="./static/means/driver/chromedriver.exe", chrome_options=chrome_options)
                driver.maximize_window()
                driver.get(atp_url)
                driver.implicitly_wait(10)
                driver.save_screenshot(img_path)
                atp_input = driver.find_element_by_id('dnn_ctr530_View_txtReferenceNo')
                atp_input.send_keys(atp)
                time.sleep(3)
                captcha_selection = driver.find_element_by_id('dnn_ctr530_View_captcha')
                captcha = captcha_selection.find_element_by_tag_name('img')
                location = captcha.location
                size = captcha.size
                coordinate = (int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))
                img = Image.open(img_path)
                img = img.crop(coordinate)
                img.save(img_path)
                result = ocr.ocr(img_path, cls=True)
                text = ''
                for line in result:
                    text += line[1][0]
                text = text.replace(" ", "")
                captcha_selection.find_element_by_tag_name('input').send_keys(text)
                time.sleep(2)
                driver.find_element_by_id('dnn_ctr530_View_btnUpdate').click()
                driver.implicitly_wait(10)
                try:
                    label = driver.find_element_by_class_name('pass-form')
                except NoSuchElementException:
                    i += 1
                    time.sleep(3)
                    if os.path.exists(img_path):
                        os.remove(img_path)
                    continue
                if os.path.exists(img_path):
                    os.remove(img_path)
                result = label.text
                return render(request, 'submit_atp_result.html', {'atp': atp, 'result': result})
            except:
                i += 1
                time.sleep(3)
                if os.path.exists(img_path):
                    os.remove(img_path)
                continue
            finally:
                driver.quit()
        return render(request, 'submit_atp_result.html', {'msg': '访问ATP网站失败，请重试！'})
    else:
        return render(request, 'error_500_clean.html')

from django import template
from django.utils.html import format_html
import json

register = template.Library()


@register.simple_tag
def background_color():
    return "#e3f2fe;"


@register.simple_tag
def html_format(content):
    return format_html(content)


@register.simple_tag
def to_list(string):
    return json.loads(string)

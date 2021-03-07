from django import template

register = template.Library()


@register.simple_tag
def background_color():
    return "#e3f2fe;"

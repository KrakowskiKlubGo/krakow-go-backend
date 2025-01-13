# utils/templatetags/utils.py
from django.template import Library
from django.urls import translate_url as django_translate_url

register = Library()


@register.simple_tag(takes_context=True)
def translate_url(context, lang_code):
    path = context.get("request").get_full_path()
    return django_translate_url(path, lang_code)

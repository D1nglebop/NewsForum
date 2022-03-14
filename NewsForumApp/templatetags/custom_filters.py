from django import template
import string


register = template.Library()


@register.filter(name='censor_words')
def censor_words(value):
    mat = ['мат', 'брань', 'Воландеморт']
    for i in mat:
        if i in value:
            value = value.replace(i, '*')
    return value


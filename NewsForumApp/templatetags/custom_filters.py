from django import template


register = template.Library()

mat = ['мат', 'брань', 'Воландеморт']

@register.filter(name='censor_words')
def censor_words(value):
    if not isinstance(value, str):
        raise ValueError('Нельзя цензурировать не строку')

    for i in mat:
        value = value.replace(i, '*' * len(i))

    return value


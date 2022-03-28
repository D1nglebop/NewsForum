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

@register.filter(name='update_page')
def update_page(full_path: str, page: int):
    try:
        params_list = full_path.split('?')[1].split('&')
        params = dict([tuple(str(param).split('=')) for param in params_list])
        params.update({'page' : page})
        link = ''
        for key, value in params.items():
            link += (f"{key}={value}&")
        return link[:-1]
    except:
        return f"page={page}"


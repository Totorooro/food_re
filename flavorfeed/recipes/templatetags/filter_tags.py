from django import template
from urllib.parse import urlencode

register = template.Library() # регистратор тегов

@register.simple_tag(takes_context=True)
def filter_url(context, field, value, reset_page=False):
    request = context['request']
    params = request.GET.copy()

    if value == 'all': # при всех значениях URL пуст
        params.pop(field, None)
    else:
        params[field] = value

    if reset_page or field == 'category' or field == 'difficulty': # при ресете, страница должна быть первой
        params['page'] = 1

    return '?' + params.urlencode()


@register.simple_tag(takes_context=True)
def is_active(context, field, value):
    request = context['request']
    current_value = request.GET.get(field)
    return 'active' if (value == 'all' and not current_value) or current_value == value else '' # активно, если не выбран ни один фильтр либо значение совпадает

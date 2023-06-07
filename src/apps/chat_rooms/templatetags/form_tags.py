from django import template
from django.utils.safestring import mark_safe
from django import forms
from django.forms.boundfield import BoundField

register = template.Library()

def get_attrs(field):
    try:
        attrs = field.field.widget.attrs
    except:
        attrs = {}
    return attrs

def form_field_attr(field, attr, value):
    if isinstance(field, BoundField):
        attrs = get_attrs(field)
        attrs[attr] = value
        field.field.widget.attrs = attrs
    return field

def get_class_value(field):
    attrs = get_attrs(field)
    return attrs.get('class', '')

def set_attrs(field, attrs):
    field.field.widget.attrs = attrs
    return field

def append_class(field, value):
    attrs = get_attrs(field)
    attrs['class'] = u"%s %s" % (get_class_value(field), value)
    field = set_attrs(field, attrs)
    return field


def css_class(value, arg):
    field = form_field_attr(value, 'class', arg)
    if isinstance(value, BoundField):
        if get_attrs(value).get('readonly', False):
            field = append_class(value, 'form-disabled')
    return field

register.filter('css_class', css_class)

def err_class(value, arg):
    if value and value.errors:
        return append_class(value, arg)
    return value

register.filter('err_class', err_class)

def placeholder(value, arg=None):
    if arg is None:
        arg = value.label
    return form_field_attr(value, 'placeholder', arg)


register.filter('placeholder', placeholder)
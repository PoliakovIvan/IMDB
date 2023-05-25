from django import template

register = template.Library()

@register.filter(name="add_5")
def add_5(value):
    return value + '5'
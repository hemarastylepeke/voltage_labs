from django import template

register = template.Library()

@register.filter
def extract_username(email):
    return email.split("@")[0]

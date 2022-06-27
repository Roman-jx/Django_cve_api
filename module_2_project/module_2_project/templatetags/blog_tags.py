from django import template
from ..models import Vulnes

register = template.Library()

@register.filter
def startswith(text):
    return text.startswith("CVE-2022")
from django import template
from django.template.defaultfilters import stringfilter

def hello_word(value):
  return 'Hello, World!'
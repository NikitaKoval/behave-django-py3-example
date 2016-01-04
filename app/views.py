from django.shortcuts import render
from django.views.generic import View, TemplateView


class HelloView(TemplateView):
    template_name = 'hello.html'
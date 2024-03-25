from django.shortcuts import render
from django.views.generic.base import TemplateView

class ModelView(TemplateView):
    
    template_name = "front/home.html"
    
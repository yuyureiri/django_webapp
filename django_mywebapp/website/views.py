# from django.shortcuts import render
# Create your views here.


from django.views.generic import TemplateView

class IndexView (TemplateView):
    template_name = "index.html"

class WorksView (TemplateView):
    template_name = "works.html"

class ContactView (TemplateView):
    template_name = "contact.html"
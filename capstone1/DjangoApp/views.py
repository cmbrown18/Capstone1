from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class CreatePageView(TemplateView):
    template_name = "create.html"

class AnalysisPageView(TemplateView):
    template_name = "analysis.html"

class DisplayPageView(TemplateView):
    template_name = "display.html"

class UserPageView(TemplateView):
    template_name = "user.html"

class DisUserPageView(TemplateView):
    template_name = "dis_user.html"

class CreUserPageView(TemplateView):
    template_name = "create_user.html"

class ModUserPageView(TemplateView):
    template_name = "mod_user.html"

class DelUserPageView(TemplateView):
    template_name = "del_user.html"

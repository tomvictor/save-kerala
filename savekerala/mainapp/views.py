from django.shortcuts import render

# Create your views here.


from django.views.generic import TemplateView



class CampHome(TemplateView):
    template_name = 'mainapp/camp/index.html'


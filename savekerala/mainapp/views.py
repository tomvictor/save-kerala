from django.shortcuts import render

# Create your views here.


from django.views.generic import TemplateView



class EmergencyNo(TemplateView):
    template_name = 'mainapp/emer_numbers.html'
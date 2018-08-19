from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)

from mainapp.models import *

class CampHome(TemplateView):
    template_name = 'mainapp/camp/index.html'

    # def get_context_data(self,*args,**kwargs):
    #     context = {}
    #     return context



class CamplListApi(APIView):

    permission_classes = [AllowAny]

    def get(self,*args,**kwargs):
        camps = []
        for obj in Camp.objects.all():
            atom = {
                "title" : obj.title,
                "lat" : obj.latitude,
                "long" : obj.longitude,
                "location" : obj.location,
                "contact_no" : obj.contact_no,
                "alternative_no" : obj.alternative_no,
                "administrator"  : obj.admin.email
            }
            camps.append(atom)
        context = {
            "camps" : camps,
            "status" : "Sucess",
            "status_code" : 1
        }

        return Response(context,status=status.HTTP_200_OK)
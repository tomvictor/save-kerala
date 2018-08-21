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
from django.shortcuts import redirect, get_object_or_404
from mainapp.models import *

class CampList(TemplateView):
    template_name = 'mainapp/camplist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dists"] = Districts.objects.all()
        context["camps"] = Camp.objects.all()
        context["locality"] = Locality.objects.all()
        return context

class CampList2(TemplateView):
    template_name = 'mainapp/camplist2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dists"] = Districts.objects.all()
        context["camps"] = Camp.objects.all()
        context["locality"] = Locality.objects.all()
        return context


class Search(TemplateView):
    template_name = 'mainapp/camplist2.html'

    def get_context_data(self, **kwargs):

        try:
            q = self.request.GET.get("q")
        except:
            q = 1
        print(q)

        context = super().get_context_data(**kwargs)
        context["dists"] = Districts.objects.all()
        context["camps"] = Camp.objects.filter(title__icontains=q)
        context["locality"] = Locality.objects.all()
        return context


class DistrictFil(TemplateView):
    template_name = 'mainapp/camplist2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            q = self.request.GET.get("q")
        except:
            q = 1
        print(q)
        context["dists"] = Districts.objects.all()
        context["camps"] = Camp.objects.filter(locality__district__id=int(q))
        context["locality"] = Locality.objects.all()
        return context

class About(TemplateView):
    template_name = 'mainapp/about.html'


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


class DistrictList(APIView):
    permission_classes = [AllowAny]

    def get(self,*args,**kwargs):
        dist_list = []
        for dist in Districts.objects.all():
            print(dist)
            atomic_dist = {
                "title" : dist.title,
                "id"  : dist.id
            }
            dist_list.append(atomic_dist)
        
        context = {
            "status" : 1,
            "message" : "sucess",
            "dist"  : dist_list
        }
        return Response(context,status=status.HTTP_200_OK)


class CampQuery(APIView):
    permission_classes = [AllowAny]

    def get(self,*args,**kwargs):
        req = self.request
        status_code = 0
        message = "fail"
        try:
            print("get the query")
            query = self.request.GET.get("q")
            message = "query sucess"
            print(message)
            print(query)
        except:
            print("except query")
            message = "unable to get query"
            status_code = 0
            context = {
                "message" : message,
                "code" : status_code
            }
            return Response(context,status=status.HTTP_200_OK)
        
        # get the camplist
        try:
            # retrive the camps
            print("getting camps")
            camps = Camp.objects.filter(district__id=int(query))
            print(camps)

        except:
            message = "unable to get data"
            status_code  = 0
            print("exept camp")
            context = {
                "message" : message,
                "code" : status_code
            }
            return Response(context,status=status.HTTP_200_OK)

        context = {
            "message" : "fail",
            "code" : 0
        }
        return Response(context, status=status.HTTP_404_NOT_FOUND)
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
)
#functions
from django.db.models.functions import Coalesce,Concat
from django.db.models import Q,F,Sum,Count
from django.db.models import Value
from django.urls import reverse
#datetime
from datetime import datetime
#JSON AJAX
from django.core import serializers
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.template import RequestContext

from .models import (
    Tips_Region,
    Tips_Province,
    Tips_City_Municipality,
    Tips_Barangay,
)

from time import strptime

success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'


import calendar
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

class Tips_Province_AJAXView(View):
    def get(self, request):
        data = dict()
        try:
            region = self.request.GET.get('region')
        except KeyError:
            region = None
        print(region)
        if region:
            region = Tips_Region.objects.get(id = region)
            province = Tips_Province.objects.filter(region_id = region.id)
        else:
            province = Tips_Province.objects.none()
        context = {
            'province':province,
        }
        data['province_data'] = render_to_string('tips/dropdown-list/province_droplist.html',context)
        return JsonResponse(data)

class Tips_City_Municipality_AJAXView(View):
    def get(self, request):
        data = dict()
        try:
            province = self.request.GET.get('province')
        except KeyError:
            province = None
        if province:
            province = Tips_Province.objects.get(id = province)
            city_municipality = Tips_City_Municipality.objects.filter(province_id = province.id)
        else:
            city_municipality = Tips_City_Municipality.objects.none()
        context = {
            'city_municipality':city_municipality,
        }
        data['city_municipality_data'] = render_to_string('tips/dropdown-list/city_municipality_droplist.html',context)
        return JsonResponse(data)

class Tips_Barangay_AJAXView(View):
    def get(self, request):
        data = dict()
        try:
            city_municipality = self.request.GET.get('city_municipality')
        except KeyError:
            city_municipality = None
        if city_municipality:
            city_municipality = Tips_City_Municipality.objects.get(id=city_municipality)
            barangay = Tips_Barangay.objects.filter(city_municipality_id = city_municipality.id)
        else:
            barangay = Tips_Barangay.objects.none()
        context = {
            'barangay':barangay,
        }
        data['barangay_data'] = render_to_string('tips/dropdown-list/barangay_droplist.html',context)
        return JsonResponse(data)

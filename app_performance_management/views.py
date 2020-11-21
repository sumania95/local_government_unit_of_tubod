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
#auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
#datetime
from datetime import datetime
#JSON AJAX
from django.core import serializers
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.template import RequestContext

from .models import (
    Accomplishment,
    Year,
)

from app_info_profile.models import (
    Profile
)

from .forms import (
    AccomplishmentForm,
    YearForm,
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
from django.utils import timezone

class Main_Accomplishment_AJAXView(LoginRequiredMixin,View):
    queryset = Accomplishment.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
        except KeyError:
            filter = None
        if filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(profile_id = self.request.user.profile.id).count()
            profile = self.queryset.filter(profile_id = self.request.user.profile.id).order_by('date_created')[:int(filter)]
            data['profile_table'] = render_to_string('main/components/list_accomplishment.html',{'profile':profile})
        return JsonResponse(data)

class Main_Accomplishment_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = AccomplishmentForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('main/forms/accomplishment_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = AccomplishmentForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Main_Accomplishment_Update_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        accomplishment = Accomplishment.objects.get(id=pk)
        form = AccomplishmentForm(instance=accomplishment)
        context = {
            'form': form,
            'is_Create': False,
            'accomplishment': accomplishment,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/accomplishment_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        accomplishment = Accomplishment.objects.get(id=pk)
        if request.method == 'POST':
            form = AccomplishmentForm(request.POST,request.FILES,instance = accomplishment)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

# ADMINISTRATOR

class Accomplishment_Year_AJAXView(LoginRequiredMixin,View):
    queryset = Year.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
        except KeyError:
            filter = None
        if filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.count()
            year = self.queryset.order_by('date_created')[:int(filter)]
            data['year_table'] = render_to_string('administrator/ajax-filter-table/table_accomplishment_year.html',{'year':year})
        return JsonResponse(data)

class Accomplishment_Year_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = YearForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/accomplishment_year_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = YearForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
                data['url'] = reverse('accomplishment_year')
        return JsonResponse(data)

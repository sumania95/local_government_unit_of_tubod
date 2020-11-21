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
from django.db.models import Q,F,Sum,Count,Avg
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
    Success_Indicator,
    Rating,
    Year,
)

from app_designation.models import (
    Designation,
)

from app_info_profile.models import (
    Profile
)

from .forms import (
    AccomplishmentForm,
    Success_IndicatorForm,
    YearForm,
    RatingForm,
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

class Accomplishment_AJAXView(LoginRequiredMixin,View):
    queryset = Designation.objects.all()
    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
            search = self.request.GET.get('search')
        except KeyError:
            filter = None
            search = None
        if filter or search:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(Q(profile__surname__icontains = search)|Q(profile__firstname__icontains = search)).count()
            profile = self.queryset.filter(Q(profile__surname__icontains = search)|Q(profile__firstname__icontains = search)).order_by('profile__surname','profile__firstname')[:int(filter)]
            data['profile_table'] = render_to_string('administrator/ajax-filter-table/table_accomplishment.html',{'profile':profile})
        return JsonResponse(data)

class Accomplishment_Detail_AJAXView(LoginRequiredMixin,View):
    queryset = Accomplishment.objects.all()
    def get(self, request):
        data = dict()
        try:
            id = self.request.GET.get('id')
        except KeyError:
            id = None
        if id:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(profile_id = id).exclude(id__in = Rating.objects.values('accomplishment__id').filter(year=Year.objects.filter(is_active=True).first())).count()
            accomplishment = self.queryset.filter(profile_id = id).exclude(id__in = Rating.objects.values('accomplishment__id').filter(year=Year.objects.filter(is_active=True).first())).order_by('date_created')
            data['accomplishment_table'] = render_to_string('administrator/ajax-filter-table/table_accomplishment_detail.html',{'accomplishment':accomplishment})
        return JsonResponse(data)

class Accomplishment_Detail_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        accomplishment = Accomplishment.objects.get(id=pk)
        form = RatingForm()
        context = {
            'form': form,
            'accomplishment': accomplishment,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/accomplishment_detail_rating_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            form = RatingForm(request.POST,request.FILES)
            accomplishment = Accomplishment.objects.get(id=pk)
            if form.is_valid():
                form.instance.accomplishment_id = pk
                form.instance.year = Year.objects.filter(is_active=True).first()
                form.instance.user_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
                data['url'] = reverse('accomplishment_detail',kwargs={'pk':accomplishment.profile.id})
        return JsonResponse(data)

class Accomplishment_Indicator_AJAXView(LoginRequiredMixin,View):
    queryset = Rating.objects.all()
    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
        except KeyError:
            filter = None
        if filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(year = Year.objects.filter(is_active=True).first()).count()
            profile = self.queryset.filter(year = Year.objects.filter(is_active=True).first()).order_by('date_created')[:int(filter)]
            data['profile_table'] = render_to_string('administrator/ajax-filter-table/table_accomplishment_indicator.html',{'profile':profile})
        return JsonResponse(data)

class Accomplishment_Indicator_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        accomplishment = Accomplishment.objects.get(id=pk)
        form = Success_IndicatorForm()
        context = {
            'form': form,
            'accomplishment': accomplishment,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/accomplishment_indicator_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        accomplishment = Accomplishment.objects.get(id=pk)
        if request.method == 'POST':
            form = Success_IndicatorForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.user_id = self.request.user.profile.id
                p = form.save()
                accomplishment.indicator.add(p)
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Accomplishment_Indicator_Remove_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            Success_Indicator.objects.filter(id=pk).delete()
            data['message_type'] = success
            data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)


class Accomplishment_IPCR_AJAXView(LoginRequiredMixin,View):
    queryset = Rating.objects
    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
            search = self.request.GET.get('search')
        except KeyError:
            filter = None
            search = None
        if filter or search:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.values('accomplishment__profile__firstname','accomplishment__profile__surname','year').filter(year = Year.objects.filter(is_active=True).first()).order_by('year').annotate(total_ratings=Sum('ratings')).count()
            profile = self.queryset.values('accomplishment__profile__firstname','accomplishment__profile__surname','year').filter(year = Year.objects.filter(is_active=True).first()).order_by('year').annotate(total_ratings=Sum('ratings'),total_count=Count('ratings'),total_avg=Avg('ratings'))[:int(filter)]
            data['profile_table'] = render_to_string('administrator/ajax-filter-table/table_accomplishment_ipcr.html',{'profile':profile})
        return JsonResponse(data)


class Accomplishment_OPCR_LIST_AJAXView(LoginRequiredMixin,View):
    queryset = Rating.objects

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
            search = self.request.GET.get('search')
        except KeyError:
            filter = None
            search = None
        if filter or search:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.values('accomplishment__profile__designation__plantilla__department__name').filter(year = Year.objects.filter(is_active=True).first()).order_by('accomplishment__profile__designation__plantilla__department__name').annotate(total_ratings=Sum('ratings'),total_count=Count('ratings'),total_avg=Avg('ratings')).count()
            profile = self.queryset.values('accomplishment__profile__designation__plantilla__department__name').filter(year = Year.objects.filter(is_active=True).first()).order_by('accomplishment__profile__designation__plantilla__department__name').annotate(total_ratings=Sum('ratings'),total_count=Count('ratings'),total_avg=Avg('ratings'))[:int(filter)]
            print(profile)
            data['profile_table'] = render_to_string('administrator/ajax-filter-table/table_accomplishment_opcr.html',{'profile':profile})
        return JsonResponse(data)

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
                Year.objects.update(is_active=False)
                form.instance.is_active = True
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
                data['url'] = reverse('accomplishment_year')
        return JsonResponse(data)

class Accomplishment_Year_Activate_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            Year.objects.update(is_active=False)
            Year.objects.filter(id=pk).update(is_active=True)
            data['message_type'] = success
            data['message_title'] = 'Successfully saved.'
            data['url'] = reverse('accomplishment_year')
        return JsonResponse(data)

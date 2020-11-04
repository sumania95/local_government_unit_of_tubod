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
    Service_Record,
)

from app_info_profile.models import (
    Profile
)

from .forms import Service_RecordForm

from time import strptime

success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

import calendar
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from .render import Render
from django.utils import timezone
from app_user_type.decorators import LogoutIfNotAdministratorHRISMixin
# administrator =====================================
class Service_Record_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = Service_Record.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
            profile_id = self.request.GET.get('profile_id')
        except KeyError:
            filter = None
            profile_id = None
        if filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(profile_id = profile_id).count()
            service_record = self.queryset.filter(profile_id = profile_id).order_by('profile__surname','profile__firstname')[:int(filter)]
            data['service_record_table'] = render_to_string('administrator/ajax-filter-table/table_profile_service_record.html',{'service_record':service_record})
        return JsonResponse(data)

class Service_Record_Print(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request,pk):
        now = timezone.now()
        profile = Profile.objects.get(id=pk)
        service_record = Service_Record.objects.filter(profile_id=profile.pk).order_by('date_from')
        params = {
            'now': now,
            'profile': profile,
            'service_record' :service_record,
        }
        pdf = Render.render('pdf/service_record.html', params)
        return pdf

class Service_Record_Create_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            profile_id= self.request.GET.get('profile_id')
        except KeyError:
            profile_id = None
        form = Service_RecordForm()
        context = {
            'form': form,
            'profile_id':profile_id,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Submit",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/profile_service_record_forms.html',context)
        return JsonResponse(data)

class Service_Record_Create_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            form = Service_RecordForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = pk
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
                data['url'] = reverse('profile_detail',kwargs={'pk':pk})
        return JsonResponse(data)

class Service_Record_Update_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            service_record_id = self.request.GET.get('service_record_id')
        except KeyError:
            service_record_id = None
        service_record = Service_Record.objects.get(pk=service_record_id)
        form = Service_RecordForm(instance = service_record)
        context = {
            'form': form,
            'service_record':service_record,
            'is_Create': False,
            'btn_name': "warning",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/profile_service_record_forms.html',context)
        return JsonResponse(data)

class Service_Record_Update_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def post(self, request,pk):
        data =  dict()
        service_record = Service_Record.objects.get(pk=pk)
        if request.method == 'POST':
            form = Service_RecordForm(request.POST,request.FILES,instance = service_record)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'

                data['url'] = reverse('profile_detail',kwargs={'pk':service_record.profile.id})
        return JsonResponse(data)

class Service_Record_Delete_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def post(self, request,pk):
        data =  dict()
        service_record = Service_Record.objects.get(pk=pk)
        if request.method == 'POST':
            Service_Record.objects.get(id=service_record.id).delete()
            data['message_type'] = success
            data['message_title'] = 'Successfully updated.'
            data['url'] = reverse('profile_detail',kwargs={'pk':service_record.profile.id})
        return JsonResponse(data)

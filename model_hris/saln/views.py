from django.shortcuts import render

from django.views.generic import (
    View,
    TemplateView,
)

#FUNCTIONS
from django.db.models.functions import Coalesce,Concat
from django.db.models import Q,F,Sum,Count
from django.db.models import Value
from django.urls import reverse

#JSON AJAX
from django.core import serializers
from django.http import JsonResponse
from django.template.loader import render_to_string

success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

from django.utils import timezone
from dateutil.relativedelta import relativedelta
from model_hris.info_profile.models import (
    Profile,
)
from model_hris.saln.models import (
    Saln_Filling,
    Saln_Business_Interest_Financial_Connections,
)
from model_hris.saln.render import Render
from model_hris.saln.forms import (
    Saln_FillingForm,
    Saln_Business_Interest_Financial_ConnectionsForm,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from app_hris.decorators import LogoutIfNotAdministratorHRISMixin

class Main_Profile_Saln_Filling_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        profile = Saln_Filling.objects.filter(profile_id = self.request.user.profile.id).exists()
        if profile:
            form = Saln_FillingForm(instance = self.request.user.profile.saln_filling)
        else:
            form = Saln_FillingForm()
        context = {
            'form': form,
            'is_Create': False,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/saln/profile_filling_type_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        profile = Saln_Filling.objects.filter(profile_id = self.request.user.profile.id).exists()
        if request.method == 'POST':
            if profile:
                form = Saln_FillingForm(request.POST,request.FILES,instance = self.request.user.profile.saln_filling)
            else:
                form = Saln_FillingForm(request.POST,request.FILES)
            if form.is_valid():
                if profile:
                    form.save()
                else:
                    form.instance.profile_id = self.request.user.profile.id
                    form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Saln_Business_Interest_Financial_Connections_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        data['profile_business_interest_financial_connections_template'] = render_to_string('main/saln/list_profile_business_interest_financial_connections.html')
        return JsonResponse(data)

class Main_Profile_Saln_Business_Interest_Financial_Connections_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Saln_Business_Interest_Financial_Connections.objects.all()

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
            data['profile_table'] = render_to_string('main/saln/list_profile_business_interest_financial_connections_table.html',{'profile':profile})
        return JsonResponse(data)

class Main_Profile_Saln_Business_Interest_Financial_Connections_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = Saln_Business_Interest_Financial_ConnectionsForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('main/saln/list_profile_business_interest_financial_connections_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Saln_Business_Interest_Financial_ConnectionsForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Main_Profile_Saln_Business_Interest_Financial_Connections_Update_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        business_interest_financial_connections = Saln_Business_Interest_Financial_Connections.objects.get(id=pk)
        form = Saln_Business_Interest_Financial_ConnectionsForm(instance=business_interest_financial_connections)
        context = {
            'form': form,
            'is_Create': False,
            'business_interest_financial_connections': business_interest_financial_connections,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/saln/list_profile_business_interest_financial_connections_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        business_interest_financial_connections = Saln_Business_Interest_Financial_Connections.objects.get(id=pk)
        if request.method == 'POST':
            form = Saln_Business_Interest_Financial_ConnectionsForm(request.POST,request.FILES,instance = business_interest_financial_connections)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Saln_Business_Interest_Financial_Connections_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            if pk:
                Saln_Business_Interest_Financial_Connections.objects.get(id=pk).delete()
                data['message_type'] = success
                data['message_title'] = 'Successfully deleted.'
            else:
                data['message_type'] = error
                data['message_title'] = 'Error Connection Lost.'
        return JsonResponse(data)


class Print_SALN_Report(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request,pk):
        now = timezone.now()
        profile = Profile.objects.get(id=pk)
        params = {
            'now': now,
            'profile': profile,
        }
        pdf = Render.render('pdf/saln.html', params)
        return pdf

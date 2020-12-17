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

from model_profiling.tips_nature_of_services.models import (
    Tips_Recommended_Services,
    Tips_Recommended_Services_Action,
    Tips_Category,
    Tips_Sub_Category,
)

from model_profiling.tips_nature_of_services.forms import (
    Tips_Recommended_ServicesForm,
    Tips_Recommended_Services_ActionForm,
    Tips_Recommended_Services_Action_UpdateForm,
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
from app_hris.decorators import LogoutIfNotAdministratorHRISMixin
# administrator =====================================
class Tips_Recommended_Services_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = Tips_Recommended_Services.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter_person_recommended_services')
            person_id = self.request.GET.get('person_id')
        except KeyError:
            filter = None
            person_id = None
        if filter or person_id:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(person_id = person_id).count()
            person_recommended_services = self.queryset.filter(person_id = person_id)[:int(filter)]
            data['table_person_recommended_services'] = render_to_string('tips/components/table_person_recommended_services.html',{'person_recommended_services':person_recommended_services})
        return JsonResponse(data)

class Tips_Recommended_Services_Create_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            person_id= self.request.GET.get('person_id')
        except KeyError:
            person_id = None
        form = Tips_Recommended_ServicesForm()
        context = {
            'form': form,
            'person_id':person_id,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Submit",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/person_recommended_services_forms.html',context)
        return JsonResponse(data)

class Tips_Recommended_Services_Create_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            form = Tips_Recommended_ServicesForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.person_id = pk
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
                data['url'] = reverse('person_detail',kwargs={'pk':pk})
        return JsonResponse(data)

class Tips_Recommended_Services_Update_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            recommended_services_id = self.request.GET.get('recommended_services_id')
        except KeyError:
            recommended_services_id = None
        recommended_services = Tips_Recommended_Services.objects.get(pk=recommended_services_id)
        form = Tips_Recommended_ServicesForm(instance = recommended_services)
        context = {
            'form': form,
            'recommended_services':recommended_services,
            'is_Create': False,
            'btn_name': "warning",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/person_recommended_services_forms.html',context)
        return JsonResponse(data)

class Tips_Recommended_Services_Update_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def post(self, request,pk):
        data =  dict()
        recommended_services = Tips_Recommended_Services.objects.get(pk=pk)
        if request.method == 'POST':
            form = Tips_Recommended_ServicesForm(request.POST,request.FILES,instance = recommended_services)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'

                data['url'] = reverse('person_detail',kwargs={'pk':recommended_services.person.id})
        return JsonResponse(data)

class Tips_Recommended_Services_Delete_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def post(self, request,pk):
        data =  dict()
        recommended_services = Tips_Recommended_Services.objects.get(pk=pk)
        if request.method == 'POST':
            Tips_Recommended_Services.objects.get(id=recommended_services.id).delete()
            data['message_type'] = success
            data['message_title'] = 'Successfully updated.'
            data['url'] = reverse('person_detail',kwargs={'pk':recommended_services.person.id})
        return JsonResponse(data)

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
#datetime
import datetime
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

class Tips_Sub_Category_AJAXView(View):
    def get(self, request):
        data = dict()
        try:
            category = self.request.GET.get('category')
        except KeyError:
            category = None
        if category:
            category = Tips_Category.objects.get(id = category)
            sub_category = Tips_Sub_Category.objects.filter(category_id = category.id)
        else:
            sub_category = Tips_Province.objects.none()
        context = {
            'sub_category':sub_category,
        }
        data['sub_category_data'] = render_to_string('tips/dropdown-list/sub_category_droplist.html',context)
        return JsonResponse(data)

# administrator =====================================

class Tips_Services_Assistance_Logs_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = Tips_Recommended_Services.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter_services_assistance')
            datepicker1 = self.request.GET.get('datepicker1')
            datepicker2 = self.request.GET.get('datepicker2')
        except KeyError:
            filter = None
            datepicker1 = None
            datepicker2 = None
        start =datetime.datetime.strptime(datepicker1+' 00:00:00', "%Y-%m-%d %H:%M:%S")
        end =datetime.datetime.strptime(datepicker2+' 23:59:59', "%Y-%m-%d %H:%M:%S")
        if filter or datepicker1 or datepicker2:
            data['form_is_valid'] = True
            data['counter_services_assistance'] = self.queryset.filter(date_created__range = [start,end]).count()
            services_assistance = self.queryset.filter(date_created__range = [start,end])[:int(filter)]
            data['table_person'] = render_to_string('tips/components/table_services_assistance_logs.html',{'services_assistance':services_assistance})
        return JsonResponse(data)

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
        print(person_id)
        if filter or person_id:
            data['form_is_valid'] = True
            data['counter_person_recommended_services'] = self.queryset.filter(person_id = person_id).count()
            person_recommended_services = self.queryset.filter(person_id = person_id)[:int(filter)]
            data['table_person_recommended_services'] = render_to_string('tips/components/table_person_recommended_services.html',{'person_recommended_services':person_recommended_services})
        return JsonResponse(data)

class Tips_Recommended_Services_Create_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            person_id= self.request.GET.get('person_id')
            services_assistance = self.request.GET.get('services_assistance')
        except KeyError:
            person_id = None
            services_assistance = None
        print(person_id)
        form = Tips_Recommended_ServicesForm()
        if services_assistance == '4':
            form_action = Tips_Recommended_Services_ActionForm()
            context = {
                'form': form,
                'person_id':person_id,
                'is_Create': True,
                'btn_name': "primary",
                'btn_title': "Submit",
            }
            context2 = {
                'form_action': form_action,
            }
            data['action'] = True
            data['action_html_form'] = render_to_string('tips/forms/person_recommended_services_action_forms.html',context2)
            data['html_form'] = render_to_string('tips/forms/person_recommended_services_forms.html',context)

        else:
            context = {
                'form': form,
                'person_id':person_id,
                'is_Create': True,
                'btn_name': "primary",
                'btn_title': "Submit",
            }
            data['action'] = False
            data['html_form'] = render_to_string('tips/forms/person_recommended_services_forms.html',context)

        return JsonResponse(data)

class Tips_Recommended_Services_Create_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def post(self, request,pk):
        data =  dict()
        try:
            services_assistance = self.request.POST.get('services_assistance')
        except KeyError:
            services_assistance = None

        if request.method == 'POST':
            if services_assistance == '4':
                form = Tips_Recommended_ServicesForm(request.POST,request.FILES)
                form_action = Tips_Recommended_Services_ActionForm(request.POST,request.FILES)
                if form.is_valid() and form_action.is_valid():
                    form.instance.person_id = pk
                    form.save()
                    form_action.instance.recommended_services_id = form.instance.id
                    form_action.save()
                    data['message_type'] = success
                    data['message_title'] = 'Successfully saved.'
                    data['url'] = reverse('tips_person_detail',kwargs={'pk':pk})
            else:
                form = Tips_Recommended_ServicesForm(request.POST,request.FILES)
                if form.is_valid():
                    form.instance.person_id = pk
                    form.save()
                    data['message_type'] = success
                    data['message_title'] = 'Successfully saved.'
                    data['url'] = reverse('tips_person_detail',kwargs={'pk':pk})
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

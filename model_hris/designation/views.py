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
from model_hris.designation.models import (
    Designation,
    Designationlog,
    Contractual,
    Plantilla,
)
from model_hris.info_profile.models import Notification
from model_hris.designation.forms import PlantillaForm,DesignationForm,ContractualForm,ContractualUpdateForm
from model_hris.designation.render import Render

from time import strptime
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'
import calendar
from django.contrib.auth.mixins import LoginRequiredMixin
from app_hris.decorators import LogoutIfNotAdministratorHRISMixin
from django.shortcuts import render

class Plantilla_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = Plantilla.objects.all()

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
            data['counter'] = self.queryset.filter(positiontitle__icontains = search).count()
            plantilla = self.queryset.filter(positiontitle__icontains = search).order_by('positiontitle')[:int(filter)]
            data['plantilla_table'] = render_to_string('administrator/ajax-filter-table/table_plantilla.html',{'plantilla':plantilla})
        return JsonResponse(data)

class Plantilla_Create_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        form = PlantillaForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Submit",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/plantilla_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = PlantillaForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
                data['url'] = reverse('designation')
        return JsonResponse(data)

class Plantilla_Update_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            plantilla_id = self.request.GET.get('plantilla_id')
        except KeyError:
            plantilla_id = None
        print(plantilla_id)
        plantilla = Plantilla.objects.get(id=plantilla_id)
        form = PlantillaForm(instance=plantilla)
        context = {
            'form': form,
            'plantilla': plantilla,
            'is_Create': False,
            'btn_name': "warning",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/plantilla_forms.html',context)
        return JsonResponse(data)

class Plantilla_Update_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            plantilla = Plantilla.objects.get(id=pk)
            form = PlantillaForm(request.POST,request.FILES,instance=plantilla)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
                data['url'] = reverse('designation')
        return JsonResponse(data)

class Designated_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = Plantilla.objects.all()

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
            data['counter'] = self.queryset.annotate(fullname = Concat('designation__profile__surname',Value(', '),'designation__profile__firstname'),fullname_back = Concat('designation__profile__firstname',Value(' '),'designation__profile__surname')).filter(Q(fullname__icontains = search)|Q(fullname_back__icontains = search)|Q(designation__profile__surname__icontains = search)|Q(designation__profile__firstname__icontains = search)).count()
            profile = self.queryset.annotate(fullname = Concat('designation__profile__surname',Value(', '),'designation__profile__firstname'),fullname_back = Concat('designation__profile__firstname',Value(' '),'designation__profile__surname')).filter(Q(fullname__icontains = search)|Q(fullname_back__icontains = search)|Q(designation__profile__surname__icontains = search)|Q(designation__profile__firstname__icontains = search)).order_by('designation__profile')[:int(filter)]
            data['profile_table'] = render_to_string('administrator/ajax-filter-table/table_designated.html',{'profile':profile})
        return JsonResponse(data)

class Contractual_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = Contractual.objects.all()

    def get(self, request):
        data = dict()
        try:
            search = self.request.GET.get('search')
            filter = self.request.GET.get('filter')
        except KeyError:
            search = None
            filter = None
        if search or filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(Q(profile__surname__icontains = search)|Q(profile__firstname__icontains = search)).count()
            contractual = self.queryset.filter(Q(profile__surname__icontains = search)|Q(profile__firstname__icontains = search)).order_by('profile__surname','profile__firstname')[:int(filter)]
            data['contractual_table'] = render_to_string('administrator/ajax-filter-table/table_contractual.html',{'contractual':contractual})
        else:
            data['form_is_valid'] = False
            data['counter'] = self.queryset.count()
            contractual = self.queryset.order_by('surname','firstname')[:int(filter)]
            data['contractual_table'] = render_to_string('administrator/ajax-filter-table/table_contractual.html',{'contractual':contractual})
        return JsonResponse(data)

class Designated_Create_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            plantilla_id = self.request.GET.get('plantilla_id')
        except KeyError:
            plantilla_id = None
        form = DesignationForm()
        context = {
            'form': form,
            'is_Create': True,
            'plantilla_id':plantilla_id,
            'btn_name': "primary",
            'btn_title': "Submit",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/designated_forms.html',context)
        return JsonResponse(data)

class Designated_Create_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            form = DesignationForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.plantilla_id = pk
                Designationlog.objects.create(profile_id=form.instance.profile_id,plantilla_id = pk,detail="Assigned",date_appointed = form.instance.date_appointed)
                Notification.objects.create(profile_id = form.instance.profile_id,detail="You are now a designated",user_id = self.request.user.id)
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
                data['url'] = reverse('designation')
        return JsonResponse(data)

class Designated_Delete_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def post(self, request,pk):
        data =  dict()
        designation = Designation.objects.get(id=pk)
        if request.method == 'POST':
            Designationlog.objects.create(profile_id=designation.profile_id,plantilla_id = designation.plantilla_id,detail="Removed assigned",date_appointed = designation.date_appointed)
            Designation.objects.filter(id=pk).delete()
            Notification.objects.create(profile_id = designation.profile_id,detail="You are remove from designated",user_id = self.request.user.id)
            data['message_type'] = success
            data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Contractual_Create_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            contractual_id = self.request.GET.get('contractual_id')
        except KeyError:
            contractual_id = None
        form = ContractualForm()
        context = {
            'form': form,
            'is_Create': True,
            'contractual_id':contractual_id,
            'btn_name': "primary",
            'btn_title': "Submit",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/contractual_forms.html',context)
        return JsonResponse(data)
    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = ContractualForm(request.POST,request.FILES)
            if form.is_valid():
                Notification.objects.create(profile_id = form.instance.profile_id,detail="You are now a contractual",user_id = self.request.user.id)
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
                data['url'] = reverse('designation')
        return JsonResponse(data)

class Contractual_Update_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            contractual_id = self.request.GET.get('contractual_id')
        except KeyError:
            contractual_id = None
        contractual = Contractual.objects.get(pk=contractual_id)
        form = ContractualUpdateForm(instance = contractual)
        context = {
            'form': form,
            'contractual':contractual,
            'is_Create': False,
            'btn_name': "warning",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/contractual_forms.html',context)
        return JsonResponse(data)

class Contractual_Update_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def post(self, request,pk):
        data =  dict()
        contractual = Contractual.objects.get(pk=pk)
        if request.method == 'POST':
            form = ContractualUpdateForm(request.POST,request.FILES,instance = contractual)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
                data['url'] = reverse('designation')
        return JsonResponse(data)

class Contractual_Delete_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def post(self, request,pk):
        data =  dict()
        profile = Contractual.objects.get(id=pk)
        if request.method == 'POST':
            Notification.objects.create(profile_id = profile.profile_id,detail="You are remove from contractual",user_id = self.request.user.id)
            Contractual.objects.filter(id=pk).delete()
            data['message_type'] = success
            data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)


        # P R I N T A B L E S #

class Print_Contract_Contractual_Report(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        profile = Contractual.objects.all().order_by('profile__surname')
        params = {
            'profile': profile,
        }
        pdf = Render.render('pdf/contractual.html', params)
        return pdf

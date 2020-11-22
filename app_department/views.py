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
    Department
)

from .forms import (
    DepartmentForm
)
from time import strptime
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'
import calendar
from django.contrib.auth.mixins import LoginRequiredMixin
from app_user_type.decorators import LogoutIfNotAdministratorHRISMixin
from django.shortcuts import render

class Department_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = Department.objects.all()

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
            data['counter'] = self.queryset.filter(name__icontains = search).count()
            department = self.queryset.filter(name__icontains = search).order_by('name')[:int(filter)]
            data['department_table'] = render_to_string('administrator/ajax-filter-table/table_department.html',{'department':department})
        return JsonResponse(data)

class Department_Create_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        form = DepartmentForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Submit",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/department_forms.html',context)
        return JsonResponse(data)
    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = DepartmentForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Department_Update_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request,pk):
        data = dict()
        department = Department.objects.get(id=pk)
        form = DepartmentForm(instance=department)
        context = {
            'form': form,
            'department': department,
            'is_Create': False,
            'btn_name': "warning",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/department_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        department = Department.objects.get(id=pk)
        if request.method == 'POST':
            form = DepartmentForm(request.POST,request.FILES,instance = department)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

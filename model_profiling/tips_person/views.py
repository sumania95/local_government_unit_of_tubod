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
from django.utils import timezone

# models
from .models import (
    Tips_Person,
    Tips_Address,
)

# forms
from .forms import (
    Tips_PersonForm,
    Tips_AddressForm,
    Tips_Update_AddressForm,
)

success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

class Tips_Person_Search_AJAXView(View):
    def get(self, request):
        data = dict()
        try:
            search_surname = self.request.GET.get('search_surname')
            search_firstname = self.request.GET.get('search_firstname')
            filter_person = self.request.GET.get('filter_person')
        except KeyError:
            search_surname = None
            search_firstname = None
            filter_person = None
        person = Tips_Person.objects.filter(surname__exact = search_surname,firstname__icontains = search_firstname)[:int(filter_person)]
        data['counter_person'] = Tips_Person.objects.filter(surname__exact = search_surname,firstname__icontains = search_firstname).count()
        data['table_person'] = render_to_string('tips/components/table_person.html',{'person':person})
        return JsonResponse(data)

class Tips_Person_Search_Result_AJAXView(View):
    def get(self, request):
        data = dict()
        try:
            result = self.request.GET.get('result')
        except KeyError:
            result = None
        if result and (int(result) > 0):
            data['form_is_valid'] = True
            context = {
                'result':result,
                'success':True,
            }
        else:
            data['form_is_valid'] = False
            context = {
                'result':result,
                'success':False,
            }

        data['html_form'] = render_to_string('tips/button/button_search_result.html',context)
        return JsonResponse(data)

class Tips_Person_Create_AJAXView(View):
    def get(self, request):
        data = dict()
        person_form = Tips_PersonForm()
        address_form = Tips_AddressForm()
        context = {
            'person_form':person_form,
            'address_form':address_form,
            'btn_name' : 'success',
            'btn_title' : 'Register',
            'is_Created' : True,
        }
        data['html_form'] = render_to_string('tips/forms/registration_forms.html',context)
        return JsonResponse(data)
    def post(self, request):
        data = dict()
        if request.method == 'POST':
            person_form = Tips_PersonForm(request.POST,request.FILES)
            address_form = Tips_AddressForm(request.POST,request.FILES)
            if person_form.is_valid() and address_form.is_valid():
                person_form.save()
                address_form.instance.person_id = person_form.instance.id
                address_form.save()
                data['url'] = reverse('tips_person_detail',kwargs={'pk':person_form.instance.id})
                data['message_type'] = success
                data['message_title'] = 'Successfully created.'
                data['form_is_valid'] = True
            else:
                data['form_is_valid'] = False
                data['message_type'] = error
                data['message_title'] = 'An error occurred.'
        return JsonResponse(data)

class Tips_Person_Update_AJAXView(View):
    def get(self, request,pk):
        data = dict()
        person = Tips_Person.objects.get(id=pk)
        address_exist = Tips_Address.objects.filter(person_id=pk).exists()
        person_form = Tips_PersonForm(instance=person)
        if address_exist:
            address = Tips_Address.objects.get(person_id=pk)
            address_form = Tips_Update_AddressForm(instance=address)
        else:
            address_form = Tips_AddressForm()
        context = {
            'person_form':person_form,
            'address_form':address_form,
            'person':person,
            'btn_name' : 'success',
            'btn_title' : 'Register',
            'is_Created' : False,

        }
        data['html_form'] = render_to_string('tips/forms/registration_forms.html',context)
        return JsonResponse(data)
    def post(self, request,pk):
        data = dict()
        person = Tips_Person.objects.get(id=pk)
        address_exist = Tips_Address.objects.filter(person_id=pk).exists()
        if address_exist:
            address = Tips_Address.objects.get(person_id=pk)
        if request.method == 'POST':
            person_form = Tips_PersonForm(request.POST,request.FILES,instance=person)
            if address_exist:
                address_form = Tips_Update_AddressForm(request.POST,request.FILES,instance=address)
            else:
                address_form = Tips_AddressForm(request.POST,request.FILES)

            if person_form.is_valid() and address_form.is_valid():
                person_form.save()
                if address_exist:
                    address_form.save()
                else:
                    address_form.instance.person_id = person_form.instance.id
                    address_form.save()
                data['url'] = reverse('tips_person_detail',kwargs={'pk':pk})
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
                data['form_is_valid'] = True
            else:
                data['form_is_valid'] = False
                data['message_type'] = error
                data['message_title'] = 'An error occurred.'
        return JsonResponse(data)

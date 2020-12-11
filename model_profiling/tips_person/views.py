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
)

# forms
from .forms import (
    Tips_PersonForm,
    Tips_AddressForm,
)

success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

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
        }
        data['html_form'] = render_to_string('tips/forms/registration_forms.html',context)
        return JsonResponse(data)
    def post(self, request):
        data = dict()
        if request.method == 'POST':
            form = Tips_PersonForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully changed.'
                data['form_is_valid'] = True
            else:
                data['form_is_valid'] = False
                data['message_type'] = error
                data['message_title'] = 'An error occurred.'
        return JsonResponse(data)

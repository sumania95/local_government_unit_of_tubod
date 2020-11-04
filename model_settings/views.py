from django.shortcuts import render,get_object_or_404
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

from app_user_type.decorators import LogoutIfNotAdministratorHRISMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SettingsForm
from .models import Settings


class Settings_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        setting = Settings.objects.get(id=1)
        form = SettingsForm(instance=setting)
        context = {
            'form':form,
            'btn_name' : 'primary',
            'btn_title' : 'Change',
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/settings_forms.html',context)
        return JsonResponse(data)
    def post(self, request):
        data = dict()
        if request.method == 'POST':
            setting = Settings.objects.get(id=1)
            form = SettingsForm(request.POST,request.FILES,instance = setting)
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

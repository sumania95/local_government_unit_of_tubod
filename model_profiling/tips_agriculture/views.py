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

from model_profiling.tips_person.models import (
    Tips_Person,
)
from .models import (
    Tips_Land_Description,
    Tips_Livestock_Poultry,
)

from .forms import (
    Tips_Land_DescriptionForm,
    Tips_Livestock_PoultryForm,
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


class Tips_Farmer_Parcel_Create_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            person_id= self.request.GET.get('person_id')
            commodity = self.request.GET.get('commodity')
        except KeyError:
            person_id = None
            commodity = None
        landform = Tips_Land_DescriptionForm()
        if commodity == '4' or commodity == '5' or commodity == '6':
            livestockform = Tips_Livestock_PoultryForm()
            context = {
                'landform': landform,
                'person_id':person_id,
                'is_Create': True,
                'btn_name': "primary",
                'btn_title': "Submit",
            }
            context2 = {
                'livestockform': livestockform,
            }
            data['action'] = True
            data['action_html_form'] = render_to_string('tips/forms/farmer_parcel_action_forms.html',context2)
        else:
            context = {
                'landform': landform,
                'person_id':person_id,
                'is_Create': True,
                'btn_name': "primary",
                'btn_title': "Submit",
            }
            data['action'] = False
        data['html_form'] = render_to_string('tips/forms/farmer_parcel_forms.html',context)

        return JsonResponse(data)

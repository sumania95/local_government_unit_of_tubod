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
    Tips_Farmer,
)

from .forms import (
    Tips_FarmerForm,
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


class Tips_Farmer_Create_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request,pk):
        data = dict()
        person = Tips_Person.objects.get(id=pk)
        form = Tips_FarmerForm()
        context = {
            'form': form,
            'person': person,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Submit",
        }
        data['html_form'] = render_to_string('tips/forms/farmer_forms.html',context)

        return JsonResponse(data)

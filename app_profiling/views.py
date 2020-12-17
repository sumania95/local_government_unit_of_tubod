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

from model_hris.info_profile.models import Profile as ProfileModel
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
from django.contrib.auth.mixins import LoginRequiredMixin
from model_profiling.tips_person.models import (
    Tips_Person as PersonModel,
)

class Tips_Dashboard_Page(LoginRequiredMixin,TemplateView):
    template_name = 'tips/dashboard.html'

class Tips_Person_Page(LoginRequiredMixin,TemplateView):
    template_name = 'tips/person.html'

class Tips_Person_Detail_Page(LoginRequiredMixin,DetailView):
    model = PersonModel
    template_name = 'tips/person_detail.html'

class Tips_Person_Detail_Create_Page(LoginRequiredMixin,TemplateView):
    template_name = 'tips/person_detail_create.html'

class Tips_Person_Detail_Update_Page(LoginRequiredMixin,TemplateView):
    template_name = 'tips/person_detail_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['person'] = PersonModel.objects.get(id = id)
        except Exception as e:
            pass
        return context

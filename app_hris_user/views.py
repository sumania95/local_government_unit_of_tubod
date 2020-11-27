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
from app_hris.models import Administrator as AdministratorModel
from django.contrib.auth.mixins import LoginRequiredMixin


class Home_Page(LoginRequiredMixin,TemplateView):
    template_name = 'main/home.html'

class History_Leave_Page(LoginRequiredMixin,TemplateView):
    template_name = 'main/history_leave.html'

class Earn_Rewards_Page(LoginRequiredMixin,TemplateView):
    template_name = 'main/earn_rewards.html'

class Document_Page(LoginRequiredMixin,TemplateView):
    template_name = 'main/form.html'

class History_Leave_Create(LoginRequiredMixin,TemplateView):
    template_name = 'main/components/apply_leave_create.html'

class Accomplishment_Page(LoginRequiredMixin,TemplateView):
    template_name = 'main/accomplishment.html'

class Voucher_Create(LoginRequiredMixin,TemplateView):
    template_name = 'main/components/voucher_create.html'

class Profile_Info_Page(LoginRequiredMixin,TemplateView):
    template_name = 'main/profile_info.html'

class Security_Page(LoginRequiredMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'main/components/security_create.html'

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
from django.db.models import Q,F,Sum,Count,Max
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

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

from model_hris.info_profile.models import (
    Profile,
    Notification,
    Message,
)
from model_hris.designation.models import (
    Designation,
    Contractual,
)
from model_hris.rewards_recognitions.models import (
    Rewards_Recognitions,
)
from model_hris.info_profile.forms import (
    ProfileForm,
    CustomAuthenticationForm,
    UsernameForm,
)
from model_hris.transaction.models import (
    Deducted_Action_Transaction,
)
#datetime
import datetime
from time import strptime

success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User

import calendar
from django.contrib.auth.mixins import LoginRequiredMixin
from app_hris.decorators import LogoutIfNotAdministratorHRISMixin
from django.shortcuts import render
from django.utils import timezone
from dateutil.relativedelta import relativedelta
import json
import random

def remove(string):
    return "".join(string.split())

class Login(LoginView):
    template_name = 'authentication/login.html'
    form_class = CustomAuthenticationForm

    def get_success_url(self,*args,**kwargs):
        return reverse('main_home')

class Logout(LoginRequiredMixin,View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    def get(self, request):
        logout(request)
        return redirect('login')

class Main_Profile_Leave_Remaining_Template_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        now = timezone.now()
        profile = Profile.objects.get(id=self.request.user.profile.id)
        special_leave = Deducted_Action_Transaction.objects.filter(deducted_transaction__profile_id = self.request.user.profile.id,deducted_transaction__leave_type = 3,deducted_transaction__date_from__year = now.year).aggregate(dsum=Coalesce(Sum('days'), Value(0)))['dsum']
        print(special_leave)
        context = {
            'profile':profile,
            'special_leave':3-special_leave,
        }
        data['profile_table'] = render_to_string('main/components/list_leave_remaining.html',context)
        return JsonResponse(data)

class Main_Notification_Template_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        data['notification_table'] = render_to_string('main/components/notification_notification.html')
        return JsonResponse(data)

class Main_Notification_AJAXView(LoginRequiredMixin,View):
    queryset = Notification.objects.all()

    def get(self, request):
        data = dict()
        data['form_is_valid'] = True
        notification = self.queryset.filter(profile_id = self.request.user.profile.id).order_by('-date_created')[:3]
        context = {
            'notification':notification,
        }
        data['notification_table'] = render_to_string('main/components/notification_notification_content.html',context)
        return JsonResponse(data)

class Main_Message_Template_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        data['message_form'] = render_to_string('main/components/notification_message.html')
        return JsonResponse(data)

class Main_Message_AJAXView(LoginRequiredMixin,View):
    queryset = Message.objects.all()

    def get(self, request):
        data = dict()
        data['form_is_valid'] = True
        message = self.queryset.filter(profile_id = self.request.user.profile.id).order_by('-date_created')[:3]
        context = {
            'message':message,
        }
        data['message_table'] = render_to_string('main/components/notification_message_content.html',context)
        return JsonResponse(data)

class Main_Profile_Sidebar_AJAXView(LoginRequiredMixin,View):
    queryset = Profile.objects.all()

    def get(self, request):
        data = dict()
        now = timezone.now()
        month = now.strftime("%B")
        current_day = now.day
        current_month = now.month
        current_year = now.year
        data['form_is_valid'] = True
        data_profile = []
        designation = Designation.objects.all()
        contractual = Contractual.objects.all()
        for p in designation:
            data_profile.append(p.profile_id)
        for c in contractual:
            data_profile.append(c.profile_id)
        profile = self.queryset.filter(date_of_birth__month=current_month,id__in = data_profile).order_by('date_of_birth__day','surname')
        profile_awardee = Rewards_Recognitions.objects.values('profile__surname','profile__firstname','profile__image').annotate(total=Count('pk')).order_by('-total')
        context = {
            'profile':profile,
            'profile_awardee':profile_awardee,
            'now':now,
        }
        data['profile_table'] = render_to_string('main/components/main_sidebar.html',context)
        return JsonResponse(data)

class Main_Profile_Basic_Info_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = ProfileForm(instance = self.request.user.profile)
        context = {
            'form': form,
            'is_Create': False,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/profile_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES,instance = self.request.user.profile)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Security_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        profile = Profile.objects.get(pk=self.request.user.profile.id)
        form = SetPasswordForm(user=profile.user)
        context = {
            'form': form,
            'profile': profile,
            'btn_name': "primary",
            'btn_title': "Submit",
        }
        data['html_form'] = render_to_string('main/forms/security_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()

        profile = Profile.objects.get(pk=self.request.user.profile.id)
        if request.method == 'POST':
            form = SetPasswordForm(user=profile.user,data=request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                Notification.objects.create(profile_id = profile.id,detail="Changed password",user_id = self.request.user.id)
                data['valid'] = True
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
                logout(request)
                data['url'] = reverse('main_home')
            else:
                error_message = form.errors.as_json()
                y = json.loads(error_message)
                data['valid'] = False
                data['message_type'] = error
                new_password2 = y['new_password2']
                for p in new_password2:
                    data['message_title'] = p['message']
        return JsonResponse(data)

# administrator =================================================

class Profile_Detail_Security_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            profile_id = self.request.GET.get('profile_id')
        except KeyError:
            profile_id = None
        profile = Profile.objects.get(pk=profile_id)
        form = SetPasswordForm(user=profile.user)
        context = {
            'form': form,
            'profile': profile,
            'btn_name': "primary",
            'btn_title': "Submit",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/security_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        try:
            profile_id = self.request.POST.get('profile_id')
        except KeyError:
            profile_id = None
        profile = Profile.objects.get(pk=profile_id)

        if request.method == 'POST':
            form = SetPasswordForm(user=profile.user,data=request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                Notification.objects.create(profile_id = profile.id,detail="Password changed.",user_id = self.request.user.id)
                data['valid'] = True
                data['message_type'] = success
                data['message_title'] = 'Successfully changed.'
                data['url'] = reverse('profile_detail',kwargs={'pk':profile.id})
            else:
                error_message = form.errors.as_json()
                y = json.loads(error_message)
                data['valid'] = False
                data['message_type'] = error
                new_password2 = y['new_password2']
                for p in new_password2:
                    data['message_title'] = p['message']
        return JsonResponse(data)

class Profile_Detail_Username_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            profile_id = self.request.GET.get('profile_id')
        except KeyError:
            profile_id = None
        profile = Profile.objects.get(pk=profile_id)
        form = UsernameForm(instance=profile.user)
        context = {
            'form': form,
            'profile': profile,
            'btn_name': "primary",
            'btn_title': "Submit",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/username_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        try:
            profile_id = self.request.POST.get('profile_id')
        except KeyError:
            profile_id = None
        profile = Profile.objects.get(pk=profile_id)

        if request.method == 'POST':
            form = UsernameForm(instance=profile.user,data=request.POST)
            if form.is_valid():
                user = form.save()
                Notification.objects.create(profile_id = profile.id,detail="Username changed.",user_id = self.request.user.id)
                data['valid'] = True
                data['message_type'] = success
                data['message_title'] = 'Successfully changed.'
                data['url'] = reverse('profile_detail',kwargs={'pk':profile.id})
            else:
                error_message = form.errors.as_json()
                y = json.loads(error_message)
                data['valid'] = False
                data['message_type'] = error
                username = y['username']
                for p in username:
                    data['message_title'] = p['message']
        return JsonResponse(data)

# LOG AUDIT
class Notification_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = Notification.objects.all()

    def get(self, request):
        data = dict()
        try:
            datepicker1 = self.request.GET.get('datepicker1')
            datepicker2 = self.request.GET.get('datepicker2')
            filter = self.request.GET.get('filter')
        except KeyError:
            datepicker1 = None
            datepicker2 = None
            filter = None
        start =datetime.datetime.strptime(datepicker1+' 00:00:00', "%Y-%m-%d %H:%M:%S")
        end =datetime.datetime.strptime(datepicker2+' 23:59:59', "%Y-%m-%d %H:%M:%S")
        if start or end or filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(date_created__range = [start,end]).count()
            notification = self.queryset.filter(date_created__range = [start,end]).order_by('date_created')[:int(filter)]
            data['notification_table'] = render_to_string('administrator/ajax-filter-table/table_notification_list.html',{'notification':notification})
        return JsonResponse(data)

class Profile_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = Profile.objects.all()

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
            data['counter'] = self.queryset.annotate(fullname = Concat('surname',Value(', '),'firstname'),fullname_back = Concat('firstname',Value(' '),'surname')).filter(Q(fullname__icontains = search)|Q(fullname_back__icontains = search)|Q(surname__icontains = search)|Q(firstname__icontains = search)).count()
            profile = self.queryset.annotate(fullname = Concat('surname',Value(', '),'firstname'),fullname_back = Concat('firstname',Value(' '),'surname')).filter(Q(fullname__icontains = search)|Q(fullname_back__icontains = search)|Q(surname__icontains = search)|Q(firstname__icontains = search)).order_by('surname','firstname')[:int(filter)]
            data['profile_table'] = render_to_string('administrator/ajax-filter-table/table_profile_list.html',{'profile':profile})
        else:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.count()
            profile = self.queryset.order_by('surname','firstname')[:int(filter)]
            data['profile_table'] = render_to_string('administrator/ajax-filter-table/table_profile_list.html',{'profile':profile})
        return JsonResponse(data)

class Profile_Retirables_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = Profile.objects.all()

    def get(self, request):
        data = dict()
        try:
            search = self.request.GET.get('search')
            filter = self.request.GET.get('filter')
        except KeyError:
            search = None
            filter = None
        now = timezone.now()
        age_55 = (now - relativedelta(years=55)).year
        data['form_is_valid'] = True
        data['counter'] = self.queryset.annotate(fullname = Concat('surname',Value(', '),'firstname'),fullname_back = Concat('firstname',Value(' '),'surname')).filter(Q(fullname__icontains = search)|Q(fullname_back__icontains = search)|Q(surname__icontains = search)|Q(firstname__icontains = search),date_of_birth__year__lte = age_55,id__in = Designation.objects.values('profile_id')).count()
        data['counter_male'] = self.queryset.filter(sex=1,date_of_birth__year__lte = age_55,id__in = Designation.objects.values('profile_id')).count()
        data['counter_female'] = self.queryset.filter(sex=2,date_of_birth__year__lte = age_55,id__in = Designation.objects.values('profile_id')).count()
        profile = self.queryset.annotate(fullname = Concat('surname',Value(', '),'firstname'),fullname_back = Concat('firstname',Value(' '),'surname')).filter(Q(fullname__icontains = search)|Q(fullname_back__icontains = search)|Q(surname__icontains = search)|Q(firstname__icontains = search),date_of_birth__year__lte = age_55,id__in = Designation.objects.values('profile_id')).order_by('surname')[:int(filter)]
        data['profile_table'] = render_to_string('administrator/ajax-filter-table/table_retirables.html',{'profile':profile})
        return JsonResponse(data)

class Profile_Create_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        form = ProfileForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Submit",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/profile_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            random_username_int = str(random.randint(11111, 99999))
            form = ProfileForm(request.POST,request.FILES)
            user_exist = Profile.objects.filter(firstname = form.instance.firstname,surname = form.instance.surname,middlename = form.instance.middlename,ext_name = form.instance.ext_name).exists()
            if user_exist:
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
            else:
                if form.is_valid():
                    number_of_users = Profile.objects.all().count()
                    if number_of_users < 250:
                        username =str(remove(form.instance.firstname.lower()))+str(random_username_int)
                        user = User.objects.create_user(username=username,email='',password=username)
                        form.instance.user = user
                        form.save()
                        data['message_type'] = success
                        data['message_title'] = 'Successfully saved.'
                        data['url'] = reverse('profile')
                    else:
                        data['message_type'] = error
                        data['message_title'] = 'Error Message Found.'
        return JsonResponse(data)

class Profile_Update_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            profile_id = self.request.GET.get('profile_id')
        except KeyError:
            profile_id = None
        profile = Profile.objects.get(pk=profile_id)
        form = ProfileForm(instance = profile)
        context = {
            "profile" : profile,
            'form': form,
            'is_Create': False,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/profile_forms.html',context)
        return JsonResponse(data)

class Profile_Update_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def post(self, request,pk):
        data =  dict()
        profile = Profile.objects.get(pk=pk)
        if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES,instance = profile)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'

                data['url'] = reverse('profile_detail',kwargs={'pk':pk})
        return JsonResponse(data)

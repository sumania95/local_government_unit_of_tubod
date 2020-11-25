from django.shortcuts import render

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

from model_hris.rewards_recognitions.models import Rewards_Recognitions
from model_hris.rewards_recognitions.forms import Rewards_RecognitionsForm
from model_hris.info_profile.models import Notification

from django.contrib.auth.mixins import LoginRequiredMixin
from app_hris.decorators import LogoutIfNotAdministratorHRISMixin

class Earn_Rewards_AJAXView(LoginRequiredMixin,View):
    queryset = Rewards_Recognitions.objects.all()
    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
        except KeyError:
            filter = None
        if filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(profile_id = self.request.user.profile.id).count()
            profile = self.queryset.filter(profile_id = self.request.user.profile.id).order_by('-date_created')[:int(filter)]
            data['profile_table'] = render_to_string('main/components/table_earn_rewards.html',{'profile':profile})
        return JsonResponse(data)
# administrator ================================
class Rewards_Recognitions_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = Rewards_Recognitions.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
            search = self.request.GET.get('search')
        except KeyError:
            filter = None
            search = None
        if search or filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.annotate(fullname = Concat('profile__surname',Value(', '),'profile__firstname'),fullname_back = Concat('profile__firstname',Value(' '),'profile__surname')).filter(Q(fullname__icontains = search)|Q(fullname_back__icontains = search)|Q(profile__surname__icontains = search)|Q(profile__firstname__icontains = search)).count()
            profile = self.queryset.annotate(fullname = Concat('profile__surname',Value(', '),'profile__firstname'),fullname_back = Concat('profile__firstname',Value(' '),'profile__surname')).filter(Q(fullname__icontains = search)|Q(fullname_back__icontains = search)|Q(profile__surname__icontains = search)|Q(profile__firstname__icontains = search)).order_by('-date_created')[:int(filter)]
            data['profile_table'] = render_to_string('administrator/ajax-filter-table/table_rewards_recognitions.html',{'profile':profile})
        return JsonResponse(data)

class Rewards_Recognitions_Create_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        form = Rewards_RecognitionsForm()
        context = {
            'form':form,
            'is_Create': True,
            'btn_name' : 'primary',
            'btn_title' : 'Submit',
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/rewards_recognitions_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Rewards_RecognitionsForm(request.POST,request.FILES)
            if form.is_valid():
                Notification.objects.create(profile_id = form.instance.profile_id,detail="Rewarded you",user_id = self.request.user.id)
                print(form.instance.profile_id)
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully created.'
                data['form_is_valid'] = True
                data['url'] = reverse('rewards_recognitions')
            else:
                data['form_is_valid'] = False
                data['message_type'] = error
                data['message_title'] = 'An error occurred.'
        return JsonResponse(data)

class Rewards_Recognitions_Update_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            rewards_recognitions_id = self.request.GET.get('rewards_recognitions_id')
        except KeyError:
            rewards_recognitions_id = None
        rewards_recognitions = Rewards_Recognitions.objects.get(pk=rewards_recognitions_id)
        form = Rewards_RecognitionsForm(instance = rewards_recognitions)
        context = {
            'form':form,
            'rewards_recognitions':rewards_recognitions,
            'is_Create': False,
            'btn_name' : 'warning',
            'btn_title' : 'Update',
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/rewards_recognitions_forms.html',context)
        return JsonResponse(data)

class Rewards_Recognitions_Update_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
        def post(self, request,pk):
            data =  dict()
            if request.method == 'POST':
                rewards_recognitions = Rewards_Recognitions.objects.get(pk=pk)
                form = Rewards_RecognitionsForm(request.POST,request.FILES,instance = rewards_recognitions)
                if form.is_valid():
                    form.save()
                    data['message_type'] = success
                    data['message_title'] = 'Successfully updated.'
                    data['form_is_valid'] = True
                    data['url'] = reverse('rewards_recognitions')
                else:
                    data['form_is_valid'] = False
                    data['message_type'] = error
                    data['message_title'] = 'An error occurred.'
            return JsonResponse(data)

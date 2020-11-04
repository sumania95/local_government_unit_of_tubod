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

from .render import Render
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from app_info_profile.models import (
    Profile,
)
from .models import (
    Learning_Development,
    Family_Background,
    Children,
    Educational_Background,
    Eligibility,
)
from .forms import (
    Family_BackgroundForm,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from app_user_type.decorators import LogoutIfNotAdministratorHRISMixin

class Main_Profile_Family_Background_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        profile = Family_Background.objects.filter(profile_id = self.request.user.profile.id).exists()
        print(profile)
        if profile:
            form = Family_BackgroundForm(instance = self.request.user.profile.family_background)
        else:
            form = Family_BackgroundForm()
        context = {
            'form': form,
            'is_Create': False,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/family_background_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        profile = Family_Background.objects.filter(profile_id = self.request.user.profile.id).exists()
        if request.method == 'POST':
            if profile:
                form = Family_BackgroundForm(request.POST,request.FILES,instance = self.request.user.profile.family_background)
            else:
                form = Family_BackgroundForm(request.POST,request.FILES)
            if form.is_valid():
                if profile:
                    form.save()
                else:
                    form.instance.profile_id = self.request.user.profile.id
                    form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Children_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        data['profile_children_template'] = render_to_string('main/components/list_profile_children.html')
        return JsonResponse(data)

class Main_Profile_Children_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Children.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
        except KeyError:
            filter = None
        if filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(profile_id = self.request.user.profile.id).count()
            profile = self.queryset.filter(profile_id = self.request.user.profile.id).order_by('surname','firstname')[:int(filter)]
            data['profile_table'] = render_to_string('main/components/list_profile_children_table.html',{'profile':profile})
        return JsonResponse(data)

class Main_Profile_Educational_Background_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        data['profile_educational_background_template'] = render_to_string('main/components/list_profile_educational_background.html')
        return JsonResponse(data)

class Main_Profile_Educational_Background_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Educational_Background.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
        except KeyError:
            filter = None
        if filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(profile_id = self.request.user.profile.id).count()
            profile = self.queryset.filter(profile_id = self.request.user.profile.id).order_by('level')[:int(filter)]
            data['profile_table'] = render_to_string('main/components/list_profile_educational_background_table.html',{'profile':profile})
        return JsonResponse(data)

class Main_Profile_Eligibility_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        data['profile_eligibility_template'] = render_to_string('main/components/list_profile_eligibility.html')
        return JsonResponse(data)

class Main_Profile_Eligibility_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Eligibility.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
        except KeyError:
            filter = None
        if filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(profile_id = self.request.user.profile.id).count()
            profile = self.queryset.filter(profile_id = self.request.user.profile.id).order_by('date_created')[:int(filter)]
            data['profile_table'] = render_to_string('main/components/list_profile_eligibility_table.html',{'profile':profile})
        return JsonResponse(data)

# administrator =========================================
class Learning_Development_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = Learning_Development.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
            action = self.request.GET.get('action')
            search = self.request.GET.get('search')
        except KeyError:
            filter = None
            search = None
            action = None
        if search or filter or action:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(title__icontains = search,typeofld = action).count()
            profile = self.queryset.filter(title__icontains = search,typeofld = action).order_by('-fromdate')[:int(filter)]
            data['profile_table'] = render_to_string('administrator/ajax-filter-table/table_learning_development.html',{'profile':profile})
        return JsonResponse(data)

class Print_Personal_Data_Sheet_Report(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request,pk):
        now = timezone.now()

        limit = (now - relativedelta(years=5)).year
        print(limit)
        profile = Profile.objects.filter(id=pk)
        params = {
            'now':now,
            'profile': profile,
        }
        pdf = Render.render('pdf/personal_data_sheet.html', params)
        return pdf

class Print_SALN_Report(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request,pk):
        now = timezone.now()
        profile = Profile.objects.filter(id=pk)[:1]
        params = {
            'now': now,
            'profile': profile,
        }
        pdf = Render.render('pdf/saln.html', params)
        return pdf

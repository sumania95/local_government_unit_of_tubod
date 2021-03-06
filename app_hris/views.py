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
from model_hris.designation.models import (
    Plantilla as PlantillaModel,
    Designation as DesignationModel,
    Contractual as ContractualModel
)
from model_hris.service_records.models import (
    Service_Record as Service_RecordModel
)
from model_hris.rewards_recognitions.models import (
    Rewards_Recognitions as Rewards_RecognitionsModel
)
from model_hris.transaction.models import (
    Deducted_Transaction as Deducted_TransactionModel
)
from model_hris.pds.models import (
    Learning_Development as Learning_DevelopmentModel,
)
from model_hris.performance_management.models import (
    Year as YearModel,
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

from django.contrib.auth.mixins import LoginRequiredMixin
from app_hris.decorators import LogoutIfNotAdministratorHRISMixin
from django.utils import timezone
from dateutil.relativedelta import relativedelta

from .forms import SettingsForm
from .models import Settings as SettingsModel
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

class Settings_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        setting = SettingsModel.objects.first()
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
            setting = SettingsModel.objects.get(id=1)
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


class Dashboard(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/dashboard.html'

class Dashboard_Panels_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = ProfileModel.objects.all()

    def get(self, request):
        data = dict()
        now = timezone.now()
        age_55 = (now - relativedelta(years=55)).year
        retirables = self.queryset.filter(date_of_birth__year__lte = age_55,id__in = DesignationModel.objects.values('profile_id')).count()
        total_users = self.queryset.count()
        total_designates = DesignationModel.objects.all().count()
        total_contractual = ContractualModel.objects.all().count()

        people_designate = []
        # DESIGNATED
        male_designates = DesignationModel.objects.filter(profile__sex = 1).all().order_by('profile__sex').count()
        female_designates = DesignationModel.objects.filter(profile__sex = 2).all().order_by('profile__sex').count()
        people_designate.append(female_designates)
        people_designate.append(male_designates)
        # CONTRACTUAL
        people_contractual = []
        male_contractual = ContractualModel.objects.filter(profile__sex = 1).all().order_by('profile__sex').count()
        female_contractual = ContractualModel.objects.filter(profile__sex = 2).all().order_by('profile__sex').count()
        people_contractual.append(female_contractual)
        people_contractual.append(male_contractual)
        # RETIRABLES
        people_retirables = []
        male_retirables = ProfileModel.objects.filter(sex=1,date_of_birth__year__lte = age_55,id__in = DesignationModel.objects.values('profile_id')).order_by('sex').count()
        female_retirables = ProfileModel.objects.filter(sex=2,date_of_birth__year__lte = age_55,id__in = DesignationModel.objects.values('profile_id')).order_by('sex').count()
        people_retirables.append(female_retirables)
        people_retirables.append(male_retirables)
        # TRAININGS
        trainings = []
        Managerial = Learning_DevelopmentModel.objects.filter(type_of_ld = 'Managerial').all().count()
        Supervision = Learning_DevelopmentModel.objects.filter(type_of_ld = 'Supervision').all().count()
        Technical = Learning_DevelopmentModel.objects.filter(type_of_ld = 'Technical').all().count()
        trainings.append(Managerial)
        trainings.append(Supervision)
        trainings.append(Technical)

        civil_status_list = []
        single = ProfileModel.objects.filter(civil_status = 1).count()
        married = ProfileModel.objects.filter(civil_status = 2).count()
        widowed = ProfileModel.objects.filter(civil_status = 3).count()
        separated = ProfileModel.objects.filter(civil_status = 4).count()
        anulled = ProfileModel.objects.filter(civil_status = 5).count()
        civil_status_list.append(single)
        civil_status_list.append(married)
        civil_status_list.append(widowed)
        civil_status_list.append(separated)
        civil_status_list.append(anulled)
        context = {
            'people_designate':people_designate,
            'people_contractual':people_contractual,
            'people_retirables':people_retirables,
            'trainings':trainings,
            'retirables':retirables,
            'total_users':total_users,
            'total_designates':total_designates,
            'total_contractual':total_contractual,
            'civil_status_list':civil_status_list,
        }
        data['form_is_valid'] = True
        data['dashboard_content'] = render_to_string('administrator/dashboard/dashboard_content.html',context)
        return JsonResponse(data)


class Profile(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/profile.html'

class Profile_Create(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/action-components/profile_create.html'

class Profile_Update(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/action-components/profile_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['profile'] = ProfileModel.objects.get(id = id)
        except Exception as e:
            pass
        return context

class Profile_Detail_Security(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/action-components/profile_security_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['profile'] = ProfileModel.objects.get(id = id)
        except Exception as e:
            pass
        return context

class Profile_Detail_Username(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/action-components/profile_username_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['profile'] = ProfileModel.objects.get(id = id)
        except Exception as e:
            pass
        return context

class Profile_Detail_Learning_Development_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request, pk):
        data = dict()
        trainings = []
        Managerial = Learning_DevelopmentModel.objects.filter(type_of_ld = 'Managerial',profile_id = pk).all().count()
        Supervision = Learning_DevelopmentModel.objects.filter(type_of_ld = 'Supervision',profile_id = pk).all().count()
        Technical = Learning_DevelopmentModel.objects.filter(type_of_ld = 'Technical',profile_id = pk).all().count()
        trainings.append(Managerial)
        trainings.append(Supervision)
        trainings.append(Technical)
        print(trainings)
        context = {
            'trainings':trainings,
        }
        data['profile_learning_development_content'] = render_to_string('administrator/action-components/profile_learning_development.html',context)
        return JsonResponse(data)

class Profile_Detail(DetailView):
    model = ProfileModel
    template_name = 'administrator/profile_detail.html'

class Profile_Detail_Service_Create(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/action-components/profile_service_record_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['profile'] = ProfileModel.objects.get(id = id)
        except Exception as e:
            pass
        return context

class Profile_Detail_Service_Update(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/action-components/profile_service_record_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['service_record'] = Service_RecordModel.objects.get(id = id)
        except Exception as e:
            pass
        return context

class Designation(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/designation.html'

class Designation_Plantilla_Create(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/action-components/plantilla_create.html'

class Designation_Plantilla_Update(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/action-components/plantilla_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['plantilla'] = PlantillaModel.objects.get(id = id)
        except Exception as e:
            pass
        return context

class Designation_Designated_Create(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/action-components/designated_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['plantilla'] = PlantillaModel.objects.get(id = id)
        except Exception as e:
            pass
        return context

class Designation_Contractual_Create(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/action-components/contractual_create.html'

class Designation_Contractual_Update(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/action-components/contractual_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['contractual'] = ContractualModel.objects.get(id = id)
        except Exception as e:
            pass
        return context

class Learning_Development(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/learning_development.html'

class Accomplishment(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/accomplishment.html'

class Accomplishment_Detail(DetailView):
    model = DesignationModel
    template_name = 'administrator/accomplishment_detail.html'

class Accomplishment_IPCR(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/accomplishment_ipcr.html'

class Accomplishment_OPCR(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/accomplishment_opcr.html'

class Accomplishment_Semester(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/accomplishment_semester.html'

class Accomplishment_Year(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/accomplishment_year.html'

class Accomplishment_Year_Create(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/action-components/accomplishment_year_create.html'

class Rewards_Recognitions(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/rewards_recognitions.html'

class Rewards_Recognitions_Create(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/action-components/rewards_recognitions_create.html'

class Rewards_Recognitions_Update(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/action-components/rewards_recognitions_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['rewards_recognitions'] = Rewards_RecognitionsModel.objects.get(id = id)
        except Exception as e:
            pass
        return context

class Retirables(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/retirables.html'

class Transaction(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/transaction.html'

class Transaction_Request_Pending_Create(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/transaction/transaction_request_pending_create.html'

class Transaction_Approved_Create(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/transaction/transaction_approved_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['request_pending'] = Deducted_TransactionModel.objects.get(id=id)
        except Exception as e:
            pass
        return context

class Transaction_Rejected_Create(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/transaction/transaction_rejected_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            context['request_pending'] = Deducted_TransactionModel.objects.get(id=id)
        except Exception as e:
            pass
        return context

class Transaction_Generated_Create(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/transaction/transaction_generated_create.html'

class Dtr_Assign(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/dtr_profile_assign.html'

class Print_DTR(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/print_dtr.html'

class Dtr_Download_Report(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/dtr_download_report.html'

class Settings(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/settings.html'

class Department(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/department.html'

class Document(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/document.html'

class Internet_Ticket(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/internet_ticket.html'

class Internet_Ticket_Create(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/action-components/internet_ticket_create.html'

class Activity_Logs(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,TemplateView):
    LOGIN_URL = 'login'
    template_name = 'administrator/activity_logs.html'

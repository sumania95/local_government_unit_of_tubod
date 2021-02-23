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

from django.utils import timezone
from dateutil.relativedelta import relativedelta
from model_hris.info_profile.models import (
    Profile,
)
from model_hris.saln.models import (
    Saln_Filling,
    Saln_Business_Interest_Financial_Connections,
    Saln_Liabilities,
    Saln_Personal_Properties,
    Saln_Real_Properties,
    Saln_Relatives_In_The_Government_Service,
)
from model_hris.saln.render import Render
from model_hris.saln.forms import (
    Saln_FillingForm,
    Saln_Business_Interest_Financial_ConnectionsForm,
    Saln_LiabilitiesForm,
    Saln_Personal_PropertiesForm,
    Saln_Real_PropertiesForm,
    Saln_Relatives_In_The_Government_ServiceForm,
)

from model_hris.pds.models import (
    Children,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from app_hris.decorators import LogoutIfNotAdministratorHRISMixin

class Main_Profile_Saln_Filling_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        profile = Saln_Filling.objects.filter(profile_id = self.request.user.profile.id).exists()
        print(profile)
        if profile:
            form = Saln_FillingForm(instance = self.request.user.profile.saln_filling)
        else:
            form = Saln_FillingForm()
        context = {
            'form': form,
            'is_Create': False,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/saln/profile_saln_filling_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        profile = Saln_Filling.objects.filter(profile_id = self.request.user.profile.id).exists()
        if request.method == 'POST':
            if profile:
                form = Saln_FillingForm(request.POST,request.FILES,instance = self.request.user.profile.saln_filling)
            else:
                form = Saln_FillingForm(request.POST,request.FILES)
            if form.is_valid():
                if profile:
                    form.save()
                else:
                    form.instance.profile_id = self.request.user.profile.id
                    form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Saln_Filling_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        profile = Saln_Filling.objects.filter(profile_id = self.request.user.profile.id).exists()
        if profile:
            form = Saln_FillingForm(instance = self.request.user.profile.saln_filling)
        else:
            form = Saln_FillingForm()
        context = {
            'form': form,
            'is_Create': False,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/saln/profile_filling_type_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        profile = Saln_Filling.objects.filter(profile_id = self.request.user.profile.id).exists()
        if request.method == 'POST':
            if profile:
                form = Saln_FillingForm(request.POST,request.FILES,instance = self.request.user.profile.saln_filling)
            else:
                form = Saln_FillingForm(request.POST,request.FILES)
            if form.is_valid():
                if profile:
                    form.save()
                else:
                    form.instance.profile_id = self.request.user.profile.id
                    form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Saln_Business_Interest_Financial_Connections_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        data['profile_business_interest_financial_connections_template'] = render_to_string('main/saln/list_profile_business_interest_financial_connections.html')
        return JsonResponse(data)

class Main_Profile_Saln_Business_Interest_Financial_Connections_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Saln_Business_Interest_Financial_Connections.objects.all()

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
            data['profile_table'] = render_to_string('main/saln/list_profile_business_interest_financial_connections_table.html',{'profile':profile})
        return JsonResponse(data)

class Main_Profile_Saln_Business_Interest_Financial_Connections_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = Saln_Business_Interest_Financial_ConnectionsForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('main/saln/list_profile_business_interest_financial_connections_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Saln_Business_Interest_Financial_ConnectionsForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Main_Profile_Saln_Business_Interest_Financial_Connections_Update_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        business_interest_financial_connections = Saln_Business_Interest_Financial_Connections.objects.get(id=pk)
        form = Saln_Business_Interest_Financial_ConnectionsForm(instance=business_interest_financial_connections)
        context = {
            'form': form,
            'is_Create': False,
            'business_interest_financial_connections': business_interest_financial_connections,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/saln/list_profile_business_interest_financial_connections_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        business_interest_financial_connections = Saln_Business_Interest_Financial_Connections.objects.get(id=pk)
        if request.method == 'POST':
            form = Saln_Business_Interest_Financial_ConnectionsForm(request.POST,request.FILES,instance = business_interest_financial_connections)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Saln_Business_Interest_Financial_Connections_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            if pk:
                Saln_Business_Interest_Financial_Connections.objects.get(id=pk).delete()
                data['message_type'] = success
                data['message_title'] = 'Successfully deleted.'
            else:
                data['message_type'] = error
                data['message_title'] = 'Error Connection Lost.'
        return JsonResponse(data)

#####LIABILITIES

class Main_Profile_Saln_Liabilities_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        data['profile_liabilities_template'] = render_to_string('main/saln/list_profile_liabilities.html')
        return JsonResponse(data)

class Main_Profile_Saln_Liabilities_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Saln_Liabilities.objects.all()

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
            data['profile_table'] = render_to_string('main/saln/list_profile_liabilities_table.html',{'profile':profile})
        return JsonResponse(data)

class Main_Profile_Saln_Liabilities_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = Saln_LiabilitiesForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('main/saln/list_profile_liabilities_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Saln_LiabilitiesForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Main_Profile_Saln_Liabilities_Update_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        liabilities = Saln_Liabilities.objects.get(id=pk)
        form = Saln_LiabilitiesForm(instance=liabilities)
        context = {
            'form': form,
            'is_Create': False,
            'liabilities': liabilities,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/saln/list_profile_liabilities_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        liabilities = Saln_Liabilities.objects.get(id=pk)
        if request.method == 'POST':
            form = Saln_LiabilitiesForm(request.POST,request.FILES,instance = liabilities)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Saln_Liabilities_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            if pk:
                Saln_Liabilities.objects.get(id=pk).delete()
                data['message_type'] = success
                data['message_title'] = 'Successfully deleted.'
            else:
                data['message_type'] = error
                data['message_title'] = 'Error Connection Lost.'
        return JsonResponse(data)
#####PERSONAL PROPERTIES

class Main_Profile_Saln_Personal_Properties_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        data['profile_personal_properties_template'] = render_to_string('main/saln/list_profile_personal_properties.html')
        return JsonResponse(data)

class Main_Profile_Saln_Personal_Properties_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Saln_Personal_Properties.objects.all()

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
            data['profile_table'] = render_to_string('main/saln/list_profile_personal_properties_table.html',{'profile':profile})
        return JsonResponse(data)

class Main_Profile_Saln_Personal_Properties_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = Saln_Personal_PropertiesForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('main/saln/list_profile_personal_properties_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Saln_Personal_PropertiesForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Main_Profile_Saln_Personal_Properties_Update_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        personal_properties = Saln_Personal_Properties.objects.get(id=pk)
        form = Saln_Personal_PropertiesForm(instance=personal_properties)
        context = {
            'form': form,
            'is_Create': False,
            'personal_properties': personal_properties,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/saln/list_profile_personal_properties_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        personal_properties = Saln_Personal_Properties.objects.get(id=pk)
        if request.method == 'POST':
            form = Saln_Personal_PropertiesForm(request.POST,request.FILES,instance = personal_properties)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Saln_Personal_Properties_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            if pk:
                Saln_Personal_Properties.objects.get(id=pk).delete()
                data['message_type'] = success
                data['message_title'] = 'Successfully deleted.'
            else:
                data['message_type'] = error
                data['message_title'] = 'Error Connection Lost.'
        return JsonResponse(data)

#####Real PROPERTIES

class Main_Profile_Saln_Real_Properties_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        data['profile_real_properties_template'] = render_to_string('main/saln/list_profile_real_properties.html')
        return JsonResponse(data)

class Main_Profile_Saln_Real_Properties_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Saln_Real_Properties.objects.all()

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
            data['profile_table'] = render_to_string('main/saln/list_profile_real_properties_table.html',{'profile':profile})
        return JsonResponse(data)

class Main_Profile_Saln_Real_Properties_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = Saln_Real_PropertiesForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('main/saln/list_profile_real_properties_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Saln_Real_PropertiesForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Main_Profile_Saln_Real_Properties_Update_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        real_properties = Saln_Real_Properties.objects.get(id=pk)
        form = Saln_Real_PropertiesForm(instance=real_properties)
        context = {
            'form': form,
            'is_Create': False,
            'real_properties': real_properties,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/saln/list_profile_real_properties_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        real_properties = Saln_Real_Properties.objects.get(id=pk)
        if request.method == 'POST':
            form = Saln_Real_PropertiesForm(request.POST,request.FILES,instance = real_properties)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Saln_Real_Properties_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            if pk:
                Saln_Real_Properties.objects.get(id=pk).delete()
                data['message_type'] = success
                data['message_title'] = 'Successfully deleted.'
            else:
                data['message_type'] = error
                data['message_title'] = 'Error Connection Lost.'
        return JsonResponse(data)


#####Relatives in the government service

class Main_Profile_Saln_Relatives_In_The_Government_Service_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        data['profile_relatives_in_the_government_service_template'] = render_to_string('main/saln/list_profile_relatives_in_the_government_service.html')
        return JsonResponse(data)

class Main_Profile_Saln_Relatives_In_The_Government_Service_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Saln_Relatives_In_The_Government_Service.objects.all()

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
            data['profile_table'] = render_to_string('main/saln/list_profile_relatives_in_the_government_service_table.html',{'profile':profile})
        return JsonResponse(data)

class Main_Profile_Saln_Relatives_In_The_Government_Service_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = Saln_Relatives_In_The_Government_ServiceForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('main/saln/list_profile_relatives_in_the_government_service_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Saln_Relatives_In_The_Government_ServiceForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Main_Profile_Saln_Relatives_In_The_Government_Service_Update_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        relatives_in_the_government_service = Saln_Relatives_In_The_Government_Service.objects.get(id=pk)
        form = Saln_Relatives_In_The_Government_ServiceForm(instance=relatives_in_the_government_service)
        context = {
            'form': form,
            'is_Create': False,
            'relatives_in_the_government_service': relatives_in_the_government_service,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/saln/list_profile_relatives_in_the_government_service_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        relatives_in_the_government_service = Saln_Relatives_In_The_Government_Service.objects.get(id=pk)
        if request.method == 'POST':
            form = Saln_Relatives_In_The_Government_ServiceForm(request.POST,request.FILES,instance = relatives_in_the_government_service)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Saln_Relatives_In_The_Government_Service_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            if pk:
                Saln_Relatives_In_The_Government_Service.objects.get(id=pk).delete()
                data['message_type'] = success
                data['message_title'] = 'Successfully deleted.'
            else:
                data['message_type'] = error
                data['message_title'] = 'Error Connection Lost.'
        return JsonResponse(data)


from app_hris.models import (
    Settings
)
class Self_Print_SALN_Report(LoginRequiredMixin,View):
    def get(self, request):
        now = timezone.now()
        settings = Settings.objects.last()
        profile = Profile.objects.get(id=self.request.user.profile.id)
        children = Children.objects.filter(profile_id=self.request.user.profile.id,civil_status = 1)
        saln_filling = Saln_Filling.objects.filter(profile_id = self.request.user.profile.id).first()
        saln_liabilities = Saln_Liabilities.objects.filter(profile_id = self.request.user.profile.id)
        saln_personal_properties = Saln_Personal_Properties.objects.filter(profile_id = self.request.user.profile.id)
        saln_real_properties = Saln_Real_Properties.objects.filter(profile_id = self.request.user.profile.id)
        saln_business_interest_financial_connections = Saln_Business_Interest_Financial_Connections.objects.filter(profile_id = self.request.user.profile.id)
        saln_relatives_in_the_government_service = Saln_Relatives_In_The_Government_Service.objects.filter(profile_id = self.request.user.profile.id)
        params = {
            'now': now,
            'settings': settings,
            'children': children,
            'profile': profile,
            'saln_filling':saln_filling,
            'saln_liabilities':saln_liabilities,
            'saln_personal_properties':saln_personal_properties,
            'saln_real_properties':saln_real_properties,
            'saln_business_interest_financial_connections':saln_business_interest_financial_connections,
            'saln_relatives_in_the_government_service':saln_relatives_in_the_government_service,
        }
        pdf = Render.render('pdf/saln.html', params)
        return pdf

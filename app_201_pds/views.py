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
    Work_Experience,
    Voluntary_Work,
)
from .forms import (
    Family_BackgroundForm,
    ChildrenForm,
    Educational_BackgroundForm,
    EligibilityForm,
    Work_ExperienceForm,
    Voluntary_WorkForm,
    Learning_DevelopmentForm,
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

class Main_Profile_Children_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = ChildrenForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('main/forms/profile_children_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = ChildrenForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Main_Profile_Children_Update_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        children = Children.objects.get(id=pk)
        form = ChildrenForm(instance=children)
        context = {
            'form': form,
            'is_Create': False,
            'children': children,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/profile_children_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        children = Children.objects.get(id=pk)
        if request.method == 'POST':
            form = ChildrenForm(request.POST,request.FILES,instance = children)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
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

class Main_Profile_Educational_Background_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = Educational_BackgroundForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('main/forms/profile_educational_background_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Educational_BackgroundForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Main_Profile_Educational_Background_Update_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        educational_background = Educational_Background.objects.get(id=pk)
        form = Educational_BackgroundForm(instance=educational_background)
        context = {
            'form': form,
            'is_Create': False,
            'educational_background': educational_background,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/profile_educational_background_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        educational_background = Educational_Background.objects.get(id=pk)
        if request.method == 'POST':
            form = Educational_BackgroundForm(request.POST,request.FILES,instance = educational_background)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
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

class Main_Profile_Eligibility_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = EligibilityForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('main/forms/profile_eligibility_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = EligibilityForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
            else:
                data['message_type'] = error
                data['message_title'] = 'Error Connection Lost.'
        return JsonResponse(data)

class Main_Profile_Eligibility_Update_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        eligibility = Eligibility.objects.get(id=pk)
        form = EligibilityForm(instance=eligibility)
        context = {
            'form': form,
            'is_Create': False,
            'eligibility': eligibility,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/profile_eligibility_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        eligibility = Eligibility.objects.get(id=pk)
        if request.method == 'POST':
            form = EligibilityForm(request.POST,request.FILES,instance = eligibility)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Work_Experience_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        data['profile_work_experience_template'] = render_to_string('main/components/list_profile_work_experience.html')
        return JsonResponse(data)

class Main_Profile_Work_Experience_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Work_Experience.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
        except KeyError:
            filter = None
        if filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(profile_id = self.request.user.profile.id).count()
            profile = self.queryset.filter(profile_id = self.request.user.profile.id).order_by('date_to')[:int(filter)]
            data['profile_table'] = render_to_string('main/components/list_profile_work_experience_table.html',{'profile':profile})
        return JsonResponse(data)

class Main_Profile_Work_Experience_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = Work_ExperienceForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('main/forms/profile_work_experience_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Work_ExperienceForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Main_Profile_Work_Experience_Update_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        work_experience = Work_Experience.objects.get(id=pk)
        form = Work_ExperienceForm(instance=work_experience)
        context = {
            'form': form,
            'is_Create': False,
            'work_experience': work_experience,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/profile_work_experience_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        work_experience = Work_Experience.objects.get(id=pk)
        if request.method == 'POST':
            form = Work_ExperienceForm(request.POST,request.FILES,instance = work_experience)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Voluntary_Work_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        data['profile_voluntary_work_template'] = render_to_string('main/components/list_profile_voluntary_work.html')
        return JsonResponse(data)

class Main_Profile_Voluntary_Work_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Voluntary_Work.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
        except KeyError:
            filter = None
        if filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(profile_id = self.request.user.profile.id).count()
            profile = self.queryset.filter(profile_id = self.request.user.profile.id).order_by('date_to')[:int(filter)]
            data['profile_table'] = render_to_string('main/components/list_profile_voluntary_work_table.html',{'profile':profile})
        return JsonResponse(data)

class Main_Profile_Voluntary_Work_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = Voluntary_WorkForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('main/forms/profile_voluntary_work_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Voluntary_WorkForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Main_Profile_Voluntary_Work_Update_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        voluntary_work = Voluntary_Work.objects.get(id=pk)
        form = Voluntary_WorkForm(instance=voluntary_work)
        context = {
            'form': form,
            'is_Create': False,
            'voluntary_work': voluntary_work,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/profile_voluntary_work_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        voluntary_work = Voluntary_Work.objects.get(id=pk)
        if request.method == 'POST':
            form = Voluntary_WorkForm(request.POST,request.FILES,instance = voluntary_work)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Learning_Development_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        data['profile_learning_development_template'] = render_to_string('main/components/list_profile_learning_development.html')
        return JsonResponse(data)

class Main_Profile_Learning_Development_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Learning_Development.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
        except KeyError:
            filter = None
        if filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(profile_id = self.request.user.profile.id).count()
            profile = self.queryset.filter(profile_id = self.request.user.profile.id).order_by('date_to')[:int(filter)]
            data['profile_table'] = render_to_string('main/components/list_profile_learning_development_table.html',{'profile':profile})
        return JsonResponse(data)

class Main_Profile_Learning_Development_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = Learning_DevelopmentForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('main/forms/profile_learning_development_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Learning_DevelopmentForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Main_Profile_Learning_Development_Update_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        learning_development = Learning_Development.objects.get(id=pk)
        form = Learning_DevelopmentForm(instance=learning_development)
        context = {
            'form': form,
            'is_Create': False,
            'learning_development': learning_development,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/profile_learning_development_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        learning_development = Learning_Development.objects.get(id=pk)
        if request.method == 'POST':
            form = Learning_DevelopmentForm(request.POST,request.FILES,instance = learning_development)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
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
            data['counter'] = self.queryset.filter(title__icontains = search,type_of_ld = action).count()
            profile = self.queryset.filter(title__icontains = search,type_of_ld = action).order_by('-date_from')[:int(filter)]
            data['profile_table'] = render_to_string('administrator/ajax-filter-table/table_learning_development.html',{'profile':profile})
        return JsonResponse(data)

class Print_Personal_Data_Sheet_Report(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request,pk):
        now = timezone.now()

        limit = (now - relativedelta(years=5)).year
        print(limit)
        profile = Profile.objects.get(id=pk)
        learning_development = Learning_Development.objects.filter(profile_id=pk).all()
        children = Children.objects.filter(profile_id=pk).all()
        educational_background = Educational_Background.objects.filter(profile_id=pk).all()
        eligibility = Eligibility.objects.filter(profile_id=pk).all()
        params = {
            'now':now,
            'profile': profile,
            'learning_development': learning_development,
            'children': children,
            'educational_background': educational_background,
            'eligibility': eligibility,
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

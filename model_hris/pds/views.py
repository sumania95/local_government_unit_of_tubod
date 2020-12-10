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
from model_hris.pds.models import (
    Learning_Development,
    Family_Background,
    Children,
    Educational_Background,
    Eligibility,
    Work_Experience,
    Voluntary_Work,
    Q34,
    Q35,
    Q36,
    Q37,
    Q38,
    Q39,
    Q40,
    References1,
    References2,
    References3,
    Government_Other_Info,
    Skill_Hobbies,
    Non_Academic,
    Member_Organization,
)
from model_hris.pds.render import Render
from model_hris.pds.forms import (
    Family_BackgroundForm,
    ChildrenForm,
    Educational_BackgroundForm,
    EligibilityForm,
    Work_ExperienceForm,
    Voluntary_WorkForm,
    Learning_DevelopmentForm,
    Q34Form,
    Q35Form,
    Q36Form,
    Q37Form,
    Q38Form,
    Q39Form,
    Q40Form,
    References1Form,
    References2Form,
    References3Form,
    Government_Other_InfoForm,
    Skill_HobbiesForm,
    Non_AcademicForm,
    Member_OrganizationForm,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from app_hris.decorators import LogoutIfNotAdministratorHRISMixin

class Main_Profile_Family_Background_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        profile = Family_Background.objects.filter(profile_id = self.request.user.profile.id).exists()
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
        data['html_form'] = render_to_string('main/forms/profile_family_background_forms.html',context)
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

class Main_Profile_Q34_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        profile = Q34.objects.filter(profile_id = self.request.user.profile.id).exists()
        if profile:
            form = Q34Form(instance = self.request.user.profile.q34)
        else:
            form = Q34Form()
        context = {
            'form': form,
            'is_Create': False,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/q34_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        profile = Q34.objects.filter(profile_id = self.request.user.profile.id).exists()
        if request.method == 'POST':
            if profile:
                form = Q34Form(request.POST,request.FILES,instance = self.request.user.profile.q34)
            else:
                form = Q34Form(request.POST,request.FILES)
            if form.is_valid():
                if profile:
                    form.save()
                else:
                    form.instance.profile_id = self.request.user.profile.id
                    form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Q35_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        profile = Q35.objects.filter(profile_id = self.request.user.profile.id).exists()
        if profile:
            form = Q35Form(instance = self.request.user.profile.q35)
        else:
            form = Q35Form()
        context = {
            'form': form,
            'is_Create': False,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/q35_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        profile = Q35.objects.filter(profile_id = self.request.user.profile.id).exists()
        if request.method == 'POST':
            if profile:
                form = Q35Form(request.POST,request.FILES,instance = self.request.user.profile.q35)
            else:
                form = Q35Form(request.POST,request.FILES)
            if form.is_valid():
                if profile:
                    form.save()
                else:
                    form.instance.profile_id = self.request.user.profile.id
                    form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Q36_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        profile = Q36.objects.filter(profile_id = self.request.user.profile.id).exists()
        if profile:
            form = Q36Form(instance = self.request.user.profile.q36)
        else:
            form = Q36Form()
        context = {
            'form': form,
            'is_Create': False,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/q36_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        profile = Q36.objects.filter(profile_id = self.request.user.profile.id).exists()
        if request.method == 'POST':
            if profile:
                form = Q36Form(request.POST,request.FILES,instance = self.request.user.profile.q36)
            else:
                form = Q36Form(request.POST,request.FILES)
            if form.is_valid():
                if profile:
                    form.save()
                else:
                    form.instance.profile_id = self.request.user.profile.id
                    form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Q37_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        profile = Q37.objects.filter(profile_id = self.request.user.profile.id).exists()
        if profile:
            form = Q37Form(instance = self.request.user.profile.q37)
        else:
            form = Q37Form()
        context = {
            'form': form,
            'is_Create': False,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/q37_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        profile = Q37.objects.filter(profile_id = self.request.user.profile.id).exists()
        if request.method == 'POST':
            if profile:
                form = Q37Form(request.POST,request.FILES,instance = self.request.user.profile.q37)
            else:
                form = Q37Form(request.POST,request.FILES)
            if form.is_valid():
                if profile:
                    form.save()
                else:
                    form.instance.profile_id = self.request.user.profile.id
                    form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Q38_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        profile = Q38.objects.filter(profile_id = self.request.user.profile.id).exists()
        if profile:
            form = Q38Form(instance = self.request.user.profile.q38)
        else:
            form = Q38Form()
        context = {
            'form': form,
            'is_Create': False,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/q38_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        profile = Q38.objects.filter(profile_id = self.request.user.profile.id).exists()
        if request.method == 'POST':
            if profile:
                form = Q38Form(request.POST,request.FILES,instance = self.request.user.profile.q38)
            else:
                form = Q38Form(request.POST,request.FILES)
            if form.is_valid():
                if profile:
                    form.save()
                else:
                    form.instance.profile_id = self.request.user.profile.id
                    form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Q39_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        profile = Q39.objects.filter(profile_id = self.request.user.profile.id).exists()
        if profile:
            form = Q39Form(instance = self.request.user.profile.q39)
        else:
            form = Q39Form()
        context = {
            'form': form,
            'is_Create': False,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/q39_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        profile = Q39.objects.filter(profile_id = self.request.user.profile.id).exists()
        if request.method == 'POST':
            if profile:
                form = Q39Form(request.POST,request.FILES,instance = self.request.user.profile.q39)
            else:
                form = Q39Form(request.POST,request.FILES)
            if form.is_valid():
                if profile:
                    form.save()
                else:
                    form.instance.profile_id = self.request.user.profile.id
                    form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Q40_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        profile = Q40.objects.filter(profile_id = self.request.user.profile.id).exists()
        if profile:
            form = Q40Form(instance = self.request.user.profile.q40)
        else:
            form = Q40Form()
        context = {
            'form': form,
            'is_Create': False,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/q40_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        profile = Q40.objects.filter(profile_id = self.request.user.profile.id).exists()
        if request.method == 'POST':
            if profile:
                form = Q40Form(request.POST,request.FILES,instance = self.request.user.profile.q40)
            else:
                form = Q40Form(request.POST,request.FILES)
            if form.is_valid():
                if profile:
                    form.save()
                else:
                    form.instance.profile_id = self.request.user.profile.id
                    form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_References1_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        profile = References1.objects.filter(profile_id = self.request.user.profile.id).exists()
        if profile:
            form = References1Form(instance = self.request.user.profile.references1)
        else:
            form = References1Form()
        context = {
            'form': form,
            'is_Create': False,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/references1_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        profile = References1.objects.filter(profile_id = self.request.user.profile.id).exists()
        if request.method == 'POST':
            if profile:
                form = References1Form(request.POST,request.FILES,instance = self.request.user.profile.references1)
            else:
                form = References1Form(request.POST,request.FILES)
            if form.is_valid():
                if profile:
                    form.save()
                else:
                    form.instance.profile_id = self.request.user.profile.id
                    form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_References2_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        profile = References2.objects.filter(profile_id = self.request.user.profile.id).exists()
        if profile:
            form = References2Form(instance = self.request.user.profile.references2)
        else:
            form = References2Form()
        context = {
            'form': form,
            'is_Create': False,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/references2_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        profile = References2.objects.filter(profile_id = self.request.user.profile.id).exists()
        if request.method == 'POST':
            if profile:
                form = References2Form(request.POST,request.FILES,instance = self.request.user.profile.references2)
            else:
                form = References2Form(request.POST,request.FILES)
            if form.is_valid():
                if profile:
                    form.save()
                else:
                    form.instance.profile_id = self.request.user.profile.id
                    form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_References3_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        profile = References3.objects.filter(profile_id = self.request.user.profile.id).exists()
        if profile:
            form = References3Form(instance = self.request.user.profile.references3)
        else:
            form = References3Form()
        context = {
            'form': form,
            'is_Create': False,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/references3_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        profile = References3.objects.filter(profile_id = self.request.user.profile.id).exists()
        if request.method == 'POST':
            if profile:
                form = References3Form(request.POST,request.FILES,instance = self.request.user.profile.references3)
            else:
                form = References3Form(request.POST,request.FILES)
            if form.is_valid():
                if profile:
                    form.save()
                else:
                    form.instance.profile_id = self.request.user.profile.id
                    form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Government_Other_Info_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        profile = Government_Other_Info.objects.filter(profile_id = self.request.user.profile.id).exists()
        if profile:
            form = Government_Other_InfoForm(instance = self.request.user.profile.government_other_info)
        else:
            form = Government_Other_InfoForm()
        context = {
            'form': form,
            'is_Create': False,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/government_other_info_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        profile = Government_Other_Info.objects.filter(profile_id = self.request.user.profile.id).exists()
        if request.method == 'POST':
            if profile:
                form = Government_Other_InfoForm(request.POST,request.FILES,instance = self.request.user.profile.government_other_info)
            else:
                form = Government_Other_InfoForm(request.POST,request.FILES)
            if form.is_valid():
                if profile:
                    form.save()
                else:
                    form.instance.profile_id = self.request.user.profile.id
                    form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

# skills
class Main_Profile_Skill_Hobbies_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        data['profile_skill_hobbies_template'] = render_to_string('main/components/list_profile_skill_hobbies.html')
        return JsonResponse(data)

class Main_Profile_Skill_Hobbies_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Skill_Hobbies.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
        except KeyError:
            filter = None
        if filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(profile_id = self.request.user.profile.id).count()
            profile = self.queryset.filter(profile_id = self.request.user.profile.id).order_by('description')[:int(filter)]
            data['profile_table'] = render_to_string('main/components/list_profile_skill_hobbies_table.html',{'profile':profile})
        return JsonResponse(data)

class Main_Profile_Skill_Hobbies_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = Skill_HobbiesForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('main/forms/profile_skill_hobbies_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Skill_HobbiesForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Main_Profile_Skill_Hobbies_Update_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        skill_hobbies = Skill_Hobbies.objects.get(id=pk)
        form = Skill_HobbiesForm(instance=skill_hobbies)
        context = {
            'form': form,
            'is_Create': False,
            'skill_hobbies': skill_hobbies,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/profile_skill_hobbies_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        skill_hobbies = Skill_Hobbies.objects.get(id=pk)
        if request.method == 'POST':
            form = Skill_HobbiesForm(request.POST,request.FILES,instance = skill_hobbies)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Skill_Hobbies_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            if pk:
                Skill_Hobbies.objects.get(id=pk).delete()
                data['message_type'] = success
                data['message_title'] = 'Successfully deleted.'
            else:
                data['message_type'] = error
                data['message_title'] = 'Error Connection Lost.'
        return JsonResponse(data)

# non_academic

class Main_Profile_Non_Academic_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        data['profile_non_academic_template'] = render_to_string('main/components/list_profile_non_academic.html')
        return JsonResponse(data)

class Main_Profile_Non_Academic_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Non_Academic.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
        except KeyError:
            filter = None
        if filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(profile_id = self.request.user.profile.id).count()
            profile = self.queryset.filter(profile_id = self.request.user.profile.id).order_by('description')[:int(filter)]
            data['profile_table'] = render_to_string('main/components/list_profile_non_academic_table.html',{'profile':profile})
        return JsonResponse(data)

class Main_Profile_Non_Academic_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = Non_AcademicForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('main/forms/profile_non_academic_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Non_AcademicForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Main_Profile_Non_Academic_Update_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        non_academic = Non_Academic.objects.get(id=pk)
        form = Non_AcademicForm(instance=non_academic)
        context = {
            'form': form,
            'is_Create': False,
            'non_academic': non_academic,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/profile_non_academic_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        non_academic = Non_Academic.objects.get(id=pk)
        if request.method == 'POST':
            form = Non_AcademicForm(request.POST,request.FILES,instance = non_academic)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Non_Academic_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            if pk:
                Non_Academic.objects.get(id=pk).delete()
                data['message_type'] = success
                data['message_title'] = 'Successfully deleted.'
            else:
                data['message_type'] = error
                data['message_title'] = 'Error Connection Lost.'
        return JsonResponse(data)

# member organization

class Main_Profile_Member_Organization_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        data['profile_member_organization_template'] = render_to_string('main/components/list_profile_member_organization.html')
        return JsonResponse(data)

class Main_Profile_Member_Organization_Table_AJAXView(LoginRequiredMixin,View):
    queryset = Member_Organization.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
        except KeyError:
            filter = None
        if filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(profile_id = self.request.user.profile.id).count()
            profile = self.queryset.filter(profile_id = self.request.user.profile.id).order_by('description')[:int(filter)]
            data['profile_table'] = render_to_string('main/components/list_profile_member_organization_table.html',{'profile':profile})
        return JsonResponse(data)

class Main_Profile_Member_Organization_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = Member_OrganizationForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('main/forms/profile_member_organization_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Member_OrganizationForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

class Main_Profile_Member_Organization_Update_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        member_organization = Member_Organization.objects.get(id=pk)
        form = Member_OrganizationForm(instance=member_organization)
        context = {
            'form': form,
            'is_Create': False,
            'member_organization': member_organization,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('main/forms/profile_member_organization_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        member_organization = Member_Organization.objects.get(id=pk)
        if request.method == 'POST':
            form = Member_OrganizationForm(request.POST,request.FILES,instance = member_organization)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully updated.'
        return JsonResponse(data)

class Main_Profile_Member_Organization_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            if pk:
                Member_Organization.objects.get(id=pk).delete()
                data['message_type'] = success
                data['message_title'] = 'Successfully deleted.'
            else:
                data['message_type'] = error
                data['message_title'] = 'Error Connection Lost.'
        return JsonResponse(data)

# children
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

class Main_Profile_Children_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            if pk:
                Children.objects.get(id=pk).delete()
                data['message_type'] = success
                data['message_title'] = 'Successfully deleted.'
            else:
                data['message_type'] = error
                data['message_title'] = 'Error Connection Lost.'
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

class Main_Profile_Educational_Background_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            if pk:
                Educational_Background.objects.get(id=pk).delete()
                data['message_type'] = success
                data['message_title'] = 'Successfully deleted.'
            else:
                data['message_type'] = error
                data['message_title'] = 'Error Connection Lost.'
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

class Main_Profile_Eligibility_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            if pk:
                Eligibility.objects.get(id=pk).delete()
                data['message_type'] = success
                data['message_title'] = 'Successfully deleted.'
            else:
                data['message_type'] = error
                data['message_title'] = 'Error Connection Lost.'
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

class Main_Profile_Work_Experience_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            if pk:
                Work_Experience.objects.get(id=pk).delete()
                data['message_type'] = success
                data['message_title'] = 'Successfully deleted.'
            else:
                data['message_type'] = error
                data['message_title'] = 'Error Connection Lost.'
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

class Main_Profile_Voluntary_Work_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            if pk:
                Voluntary_Work.objects.get(id=pk).delete()
                data['message_type'] = success
                data['message_title'] = 'Successfully deleted.'
            else:
                data['message_type'] = error
                data['message_title'] = 'Error Connection Lost.'
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

class Main_Profile_Learning_Development_Delete_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            if pk:
                Learning_Development.objects.get(id=pk).delete()
                data['message_type'] = success
                data['message_title'] = 'Successfully deleted.'
            else:
                data['message_type'] = error
                data['message_title'] = 'Error Connection Lost.'
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
        profile = Profile.objects.get(id=pk)
        children = Children.objects.filter(profile_id=pk).all().order_by('date_of_birth')
        educational_background = Educational_Background.objects.filter(profile_id=pk).all().order_by('level')
        eligibility = Eligibility.objects.filter(profile_id=pk).all()
        learning_development = Learning_Development.objects.filter(profile_id=pk).all().order_by('-date_from')
        work_experience = Work_Experience.objects.filter(profile_id=pk).order_by('-date_from')
        voluntary_work = Voluntary_Work.objects.filter(profile_id=pk).order_by('-date_from')
        try:
            family_background = Family_Background.objects.filter(profile_id=pk).first()
            q34 = Q34.objects.filter(profile_id=pk).first()
            q35 = Q35.objects.filter(profile_id=pk).first()
            q36 = Q36.objects.filter(profile_id=pk).first()
            q37 = Q37.objects.filter(profile_id=pk).first()
            q38 = Q38.objects.filter(profile_id=pk).first()
            q39 = Q39.objects.filter(profile_id=pk).first()
            q40 = Q40.objects.filter(profile_id=pk).first()
            references1 = References1.objects.filter(profile_id=pk).first()
            references2 = References2.objects.filter(profile_id=pk).first()
            references3 = References3.objects.filter(profile_id=pk).first()
            government_other_info = Government_Other_Info.objects.filter(profile_id=pk).first()
        except KeyError:
            family_background = None
            q34 = None
            q35 = None
            q36 = None
            q37 = None
            q38 = None
            q39 = None
            q40 = None
            references1 = None
            references2 = None
            references3 = None
            government_other_info = None
        params = {
            'now':now,
            'profile': profile,
            'children': children,
            'family_background': family_background,
            'educational_background': educational_background,
            'eligibility': eligibility,
            'learning_development': learning_development,
            'work_experience': work_experience,
            'voluntary_work': voluntary_work,
            'q34':q34,
            'q35':q35,
            'q36':q36,
            'q37':q37,
            'q38':q38,
            'q39':q39,
            'q40':q40,
            'references1':references1,
            'references2':references2,
            'references3':references3,
            'government_other_info':government_other_info,
        }
        pdf = Render.render('pdf/personal_data_sheet.html', params)
        return pdf

class Self_Print_Personal_Data_Sheet_Report(LoginRequiredMixin,View):
    def get(self, request):
        now = timezone.now()
        limit = (now - relativedelta(years=5)).year
        profile = Profile.objects.get(id=self.request.user.profile.id)
        children = Children.objects.filter(profile_id=self.request.user.profile.id).all().order_by('date_of_birth')
        educational_background = Educational_Background.objects.filter(profile_id=self.request.user.profile.id).all().order_by('level')
        eligibility = Eligibility.objects.filter(profile_id=self.request.user.profile.id).all()
        learning_development = Learning_Development.objects.filter(profile_id=self.request.user.profile.id).all().order_by('-date_from')
        work_experience = Work_Experience.objects.filter(profile_id=self.request.user.profile.id).order_by('-date_from')
        voluntary_work = Voluntary_Work.objects.filter(profile_id=self.request.user.profile.id).order_by('-date_from')
        try:
            family_background = Family_Background.objects.filter(profile_id=self.request.user.profile.id).first()
            q34 = Q34.objects.filter(profile_id=self.request.user.profile.id).first()
            q35 = Q35.objects.filter(profile_id=self.request.user.profile.id).first()
            q36 = Q36.objects.filter(profile_id=self.request.user.profile.id).first()
            q37 = Q37.objects.filter(profile_id=self.request.user.profile.id).first()
            q38 = Q38.objects.filter(profile_id=self.request.user.profile.id).first()
            q39 = Q39.objects.filter(profile_id=self.request.user.profile.id).first()
            q40 = Q40.objects.filter(profile_id=self.request.user.profile.id).first()
            references1 = References1.objects.filter(profile_id=self.request.user.profile.id).first()
            references2 = References2.objects.filter(profile_id=self.request.user.profile.id).first()
            references3 = References3.objects.filter(profile_id=self.request.user.profile.id).first()
            government_other_info = Government_Other_Info.objects.filter(profile_id=self.request.user.profile.id).first()
        except KeyError:
            family_background = None
            q34 = None
            q35 = None
            q36 = None
            q37 = None
            q38 = None
            q39 = None
            q40 = None
            references1 = None
            references2 = None
            references3 = None
            government_other_info = None
        params = {
            'now':now,
            'profile': profile,
            'children': children,
            'family_background': family_background,
            'educational_background': educational_background,
            'eligibility': eligibility,
            'learning_development': learning_development,
            'work_experience': work_experience,
            'voluntary_work': voluntary_work,
            'q34':q34,
            'q35':q35,
            'q36':q36,
            'q37':q37,
            'q38':q38,
            'q39':q39,
            'q40':q40,
            'references1':references1,
            'references2':references2,
            'references3':references3,
            'government_other_info':government_other_info,
        }
        pdf = Render.render('pdf/personal_data_sheet.html', params)
        return pdf

class Print_SALN_Report(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request,pk):
        now = timezone.now()
        profile = Profile.objects.get(id=pk)
        params = {
            'now': now,
            'profile': profile,
        }
        pdf = Render.render('pdf/saln.html', params)
        return pdf

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

from model_hris.transaction.models import (
    Deducted_Transaction,
    Deducted_Action_Transaction,
    Rejected_Transaction,
    Generated_Transaction,
)

from model_hris.info_profile.models import (
    Profile,
    Notification
)

from model_hris.designation.models import (
    Designation,
    Contractual
)

from model_hris.transaction.forms import (
    Deducted_TransactionForm,
    User_Deducted_Contractual_TransactionForm,
    User_Deducted_TransactionForm,
    Deducted_Action_TransactionForm,
    Rejected_TransactionForm,
    Generated_TransactionForm,
    Batch_Generated_TransactionForm,
)
from django.utils import timezone
#datetime
import datetime
from time import strptime

success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

from django.contrib.auth.models import User
from model_hris.transaction.render import Render
import calendar
from django.contrib.auth.mixins import LoginRequiredMixin
from app_hris.decorators import LogoutIfNotAdministratorHRISMixin
from django.shortcuts import render
from django.utils import timezone


# user ==================
class Profile_History_Leave_AJAXView(LoginRequiredMixin,View):
    queryset = Deducted_Transaction.objects.all()

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
            data['profile_table'] = render_to_string('main/components/table_history_leave.html',{'profile':profile})
        return JsonResponse(data)

class Profile_History_Leave_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        try:
            print(self.request.user.profile.designation)
            form = User_Deducted_TransactionForm()
        except Exception as e:
            form = User_Deducted_Contractual_TransactionForm()
        context = {
            'form':form,
            'is_Create': True,
            'btn_name' : 'primary',
            'btn_title' : 'Submit',
        }
        data['html_form'] = render_to_string('main/forms/apply_leave_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            if self.request.user.profile:
                form = User_Deducted_TransactionForm(request.POST,request.FILES)
            else:
                form = User_Deducted_Contractual_TransactionForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.profile_id = self.request.user.profile.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully created.'
                data['form_is_valid'] = True
                data['url'] = reverse('main_history_leave')
            else:
                data['form_is_valid'] = False
                data['message_type'] = error
                data['message_title'] = 'An error occurred.'
        return JsonResponse(data)

class Profile_History_Leave_Delete_Save_AJAXView(LoginRequiredMixin,View):
    def post(self, request,pk):
        data =  dict()
        leave = Deducted_Transaction.objects.get(id=pk)
        if request.method == 'POST':
            Deducted_Transaction.objects.filter(id=pk).delete()
            Notification.objects.create(profile_id = leave.profile_id,detail="Request leave removed.",user_id = self.request.user.id)
            data['message_type'] = success
            data['message_title'] = 'Successfully saved.'
        return JsonResponse(data)

# administrator ==================

class Transaction_Request_Pending_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = Deducted_Transaction.objects.all()

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
            data['counter'] = self.queryset.annotate(fullname = Concat('profile__surname',Value(', '),'profile__firstname'),fullname_back = Concat('profile__firstname',Value(' '),'profile__surname')).filter(Q(fullname__icontains = search)|Q(fullname_back__icontains = search)|Q(profile__surname__icontains = search)|Q(profile__firstname__icontains = search),status=1).count()
            profile = self.queryset.annotate(fullname = Concat('profile__surname',Value(', '),'profile__firstname'),fullname_back = Concat('profile__firstname',Value(' '),'profile__surname')).filter(Q(fullname__icontains = search)|Q(fullname_back__icontains = search)|Q(profile__surname__icontains = search)|Q(profile__firstname__icontains = search),status=1).order_by('-date_created')[:int(filter)]
            data['profile_table'] = render_to_string('administrator/ajax-filter-table/table_transaction_request_pending.html',{'profile':profile})
        return JsonResponse(data)

class Transaction_Request_Pending_Create_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        form = Deducted_TransactionForm()
        context = {
            'form':form,
            'is_Create': True,
            'btn_name' : 'primary',
            'btn_title' : 'Submit',
        }
        data['html_form'] = render_to_string('administrator/transaction/transaction_request_pending_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Deducted_TransactionForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully created.'
                data['form_is_valid'] = True
                data['url'] = reverse('transaction')
            else:
                data['form_is_valid'] = False
                data['message_type'] = error
                data['message_title'] = 'An error occurred.'
        return JsonResponse(data)

class Transaction_Approved_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = Deducted_Transaction.objects.all()

    def get(self, request):
        data = dict()
        try:
            search = self.request.GET.get('search')
            filter = self.request.GET.get('filter')
            datepicker1 = self.request.GET.get('datepicker1')
            datepicker2 = self.request.GET.get('datepicker2')
        except KeyError:
            search = None
            filter = None
            datepicker1 = None
            datepicker2 = None
        start =datetime.datetime.strptime(datepicker1+' 00:00:00', "%Y-%m-%d %H:%M:%S")
        end =datetime.datetime.strptime(datepicker2+' 23:59:59', "%Y-%m-%d %H:%M:%S")
        if search or filter or start or end:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.annotate(fullname = Concat('profile__surname',Value(', '),'profile__firstname'),fullname_back = Concat('profile__firstname',Value(' '),'profile__surname')).filter(Q(fullname__icontains = search)|Q(fullname_back__icontains = search)|Q(profile__surname__icontains = search)|Q(profile__firstname__icontains = search),status = 2,date_created__range = [start,end]).count()
            profile = self.queryset.annotate(fullname = Concat('profile__surname',Value(', '),'profile__firstname'),fullname_back = Concat('profile__firstname',Value(' '),'profile__surname')).filter(Q(fullname__icontains = search)|Q(fullname_back__icontains = search)|Q(profile__surname__icontains = search)|Q(profile__firstname__icontains = search),status = 2,date_created__range = [start,end]).order_by('-date_created')[:int(filter)]
            data['profile_table'] = render_to_string('administrator/ajax-filter-table/table_transaction_approved.html',{'profile':profile})
        return JsonResponse(data)

class Transaction_Approved_Create_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            request_pending_id = self.request.GET.get('request_pending_id')
        except KeyError:
            request_pending_id = None
        form = Deducted_Action_TransactionForm()
        deducted_transaction = Deducted_Transaction.objects.get(id=request_pending_id)
        profile = Profile.objects.get(id=deducted_transaction.profile_id)
        context = {
            'form':form,
            'profile':profile,
            'deducted_transaction':deducted_transaction,
            'request_pending_id':request_pending_id,
            'is_Create': True,
            'btn_name' : 'primary',
            'btn_title' : 'Submit',
        }
        data['html_form'] = render_to_string('administrator/transaction/transaction_approved_forms.html',context)
        return JsonResponse(data)
class Transaction_Approved_Create_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def post(self, request,pk):
        data =  dict()
        now = timezone.now()
        if request.method == 'POST':
            deducted_transaction = Deducted_Transaction.objects.get(id=pk)
            profile = Profile.objects.get(id=deducted_transaction.profile_id)
            form = Deducted_Action_TransactionForm(request.POST,request.FILES)
            # SICKLEAVE
            if deducted_transaction.leave_type == '1':
                if form.is_valid():
                    if float(form.instance.days) <= float(profile.sl):
                        form.instance.deducted_transaction_id = pk
                        form.instance.user_id = self.request.user.id
                        Profile.objects.filter(id=profile.id).update(sl=F('sl')-form.instance.days)
                        Notification.objects.create(profile_id = profile.id,detail="Approved sick leave",user_id = self.request.user.id)
                        form.save()
                        Deducted_Transaction.objects.filter(id=pk).update(status = 2)
                        data['message_type'] = success
                        data['message_title'] = 'Successfully created.'
                        data['form_is_valid'] = True
                        data['url'] = reverse('transaction')
                    else:
                        data['form_is_valid'] = False
                        data['message_type'] = error
                        data['message_title'] = 'Insufficient Sick Leave'
                else:
                    if float(form.instance.days) == 0:
                        data['form_is_valid'] = False
                        data['message_type'] = error
                        data['message_title'] = 'Zero is not allowed.'
                    else:
                        data['form_is_valid'] = False
                        data['message_type'] = error
                        data['message_title'] = 'An error occurred.'
            # VACATIONLEAVE
            elif deducted_transaction.leave_type == '2':
                if form.is_valid():
                    if float(form.instance.days) <= float(profile.vl):
                        form.instance.deducted_transaction_id = pk
                        form.instance.user_id = self.request.user.id
                        Profile.objects.filter(id=profile.id).update(vl=F('vl')-form.instance.days)
                        Notification.objects.create(profile_id = profile.id,detail="Approved vacation leave",user_id = self.request.user.id)
                        form.save()
                        Deducted_Transaction.objects.filter(id=pk).update(status = 2)
                        data['message_type'] = success
                        data['message_title'] = 'Successfully created.'
                        data['form_is_valid'] = True
                        data['url'] = reverse('transaction')
                    else:
                        data['form_is_valid'] = False
                        data['message_type'] = error
                        data['message_title'] = 'Insufficient Vacation Leave'
                else:
                    if float(form.instance.days) == 0:
                        data['form_is_valid'] = False
                        data['message_type'] = error
                        data['message_title'] = 'Zero is not allowed.'
                    else:
                        data['form_is_valid'] = False
                        data['message_type'] = error
                        data['message_title'] = 'An error occurred.'
            # SPECIALLEAVE
            elif deducted_transaction.leave_type == '3':
                special_leave = Deducted_Action_Transaction.objects.filter(deducted_transaction__profile_id = profile.id,deducted_transaction__leave_type = 3,deducted_transaction__date_from__year = now.year).aggregate(dsum=Coalesce(Sum('days'), Value(0)))['dsum']
                number_of_days = self.request.POST.get('days')
                if form.is_valid():
                    if (float(special_leave) + float(form.instance.days)) > 3:
                        data['form_is_valid'] = False
                        data['message_type'] = error
                        data['message_title'] = 'Insufficient Special Leave.'
                    else:
                        form.instance.deducted_transaction_id = pk
                        form.instance.user_id = self.request.user.id
                        form.save()
                        Deducted_Transaction.objects.filter(id=pk).update(status = 2)
                        Notification.objects.create(profile_id = profile.id,detail="Approved special leave",user_id = self.request.user.id)
                        data['message_type'] = success
                        data['message_title'] = 'Successfully created.'
                        data['form_is_valid'] = True
                        data['url'] = reverse('transaction')
                else:
                    if float(form.instance.days) == 0:
                        data['form_is_valid'] = False
                        data['message_type'] = error
                        data['message_title'] = 'Zero is not allowed.'
                    else:
                        data['form_is_valid'] = False
                        data['message_type'] = error
                        data['message_title'] = 'An error occurred.'
            # OFFSETLEAVE
            elif deducted_transaction.leave_type == '4':
                if form.is_valid():
                    if float(form.instance.days) <= float(profile.overtime):
                        form.instance.deducted_transaction_id = pk
                        form.instance.user_id = self.request.user.id
                        Profile.objects.filter(id=profile.id).update(overtime=F('overtime')-form.instance.days)
                        Notification.objects.create(profile_id = profile.id,detail="Approved offset/overtime",user_id = self.request.user.id)
                        form.save()
                        Deducted_Transaction.objects.filter(id=pk).update(status = 2)
                        data['message_type'] = success
                        data['message_title'] = 'Successfully created.'
                        data['form_is_valid'] = True
                        data['url'] = reverse('transaction')
                    else:
                        data['form_is_valid'] = False
                        data['message_type'] = error
                        data['message_title'] = 'Insufficient Overtime'
                else:
                    if float(form.instance.days) == 0:
                        data['form_is_valid'] = False
                        data['message_type'] = error
                        data['message_title'] = 'Zero is not allowed.'
                    else:
                        data['form_is_valid'] = False
                        data['message_type'] = error
                        data['message_title'] = 'An error occurred.'
            # MATERNITYLEAVE
            elif deducted_transaction.leave_type == '5' or deducted_transaction.leave_type == '6':
                    if form.is_valid():
                        form.instance.deducted_transaction_id = pk
                        form.instance.user_id = self.request.user.id
                        form.save()
                        Deducted_Transaction.objects.filter(id=pk).update(status = 2)
                        if deducted_transaction.leave_type == '5':
                            Notification.objects.create(profile_id = profile.id,detail="Approved maternity leave",user_id = self.request.user.id)
                        else:
                            Notification.objects.create(profile_id = profile.id,detail="Approved faternity leave",user_id = self.request.user.id)
                        data['message_type'] = success
                        data['message_title'] = 'Successfully created.'
                        data['form_is_valid'] = True
                        data['url'] = reverse('transaction')
                    else:
                        if float(form.instance.days) == 0:
                            data['form_is_valid'] = False
                            data['message_type'] = error
                            data['message_title'] = 'Zero is not allowed.'
                        else:
                            data['form_is_valid'] = False
                            data['message_type'] = error
                            data['message_title'] = 'An error occurred.'
        return JsonResponse(data)

class Transaction_Rejected_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = Deducted_Transaction.objects.all()

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
            data['counter'] = self.queryset.annotate(fullname = Concat('profile__surname',Value(', '),'profile__firstname'),fullname_back = Concat('profile__firstname',Value(' '),'profile__surname')).filter(Q(fullname__icontains = search)|Q(fullname_back__icontains = search)|Q(profile__surname__icontains = search)|Q(profile__firstname__icontains = search),status=3).count()
            profile = self.queryset.annotate(fullname = Concat('profile__surname',Value(', '),'profile__firstname'),fullname_back = Concat('profile__firstname',Value(' '),'profile__surname')).filter(Q(fullname__icontains = search)|Q(fullname_back__icontains = search)|Q(profile__surname__icontains = search)|Q(profile__firstname__icontains = search),status=3).order_by('-date_created')[:int(filter)]
            data['profile_table'] = render_to_string('administrator/ajax-filter-table/table_transaction_rejected.html',{'profile':profile})
        return JsonResponse(data)

class Transaction_Rejected_Create_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            request_pending_id = self.request.GET.get('request_pending_id')
        except KeyError:
            request_pending_id = None
        form = Rejected_TransactionForm()
        context = {
            'form':form,
            'request_pending_id':request_pending_id,
            'is_Create': True,
            'btn_name' : 'primary',
            'btn_title' : 'Submit',
        }
        data['html_form'] = render_to_string('administrator/transaction/transaction_rejected_forms.html',context)
        return JsonResponse(data)
class Transaction_Rejected_Create_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def post(self, request,pk):
        data =  dict()
        if request.method == 'POST':
            deduction_profile = Deducted_Transaction.objects.get(id=pk)
            form = Rejected_TransactionForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.deducted_transaction_id = pk
                form.instance.user_id = self.request.user.id
                Notification.objects.create(profile_id = deduction_profile.profile_id,detail="Disapproved leave",user_id = self.request.user.id)
                form.save()
                Deducted_Transaction.objects.filter(id=pk).update(status = 3)
                data['message_type'] = success
                data['message_title'] = 'Successfully created.'
                data['form_is_valid'] = True
                data['url'] = reverse('transaction')
            else:
                data['form_is_valid'] = False
                data['message_type'] = error
                data['message_title'] = 'An error occurred.'
        return JsonResponse(data)

class Transaction_Generated_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = Generated_Transaction.objects.all()

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
            data['counter'] = self.queryset.annotate(fullname = Concat('profile__surname',Value(', '),'profile__firstname'),fullname_back = Concat('profile__firstname',Value(' '),'profile__surname')).filter(Q(fullname__icontains = search)|Q(fullname_back__icontains = search)|Q(profile__surname__icontains = search)|Q(profile__firstname__icontains = search)).count()
            profile = self.queryset.annotate(fullname = Concat('profile__surname',Value(', '),'profile__firstname'),fullname_back = Concat('profile__firstname',Value(' '),'profile__surname')).filter(Q(fullname__icontains = search)|Q(fullname_back__icontains = search)|Q(profile__surname__icontains = search)|Q(profile__firstname__icontains = search)).order_by('-date_created')[:int(filter)]
            data['profile_table'] = render_to_string('administrator/ajax-filter-table/table_transaction_generated.html',{'profile':profile})
        return JsonResponse(data)

class Transaction_Generated_Create_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            select_option_generated = self.request.GET.get('select_option_generated')
        except KeyError:
            select_option_generated = None
        if select_option_generated == '1':
            form = Generated_TransactionForm()
        else:
            form = Batch_Generated_TransactionForm()
        context = {
            'form':form,
            'btn_name' : 'primary',
            'btn_title' : 'Submit',
        }
        if select_option_generated == '1':
            data['html_form'] = render_to_string('administrator/transaction/transaction_generated_forms.html',context)
        else:
            data['html_form'] = render_to_string('administrator/transaction/transaction_batch_generated_forms.html',context)
        return JsonResponse(data)

class Transaction_Generated_Profile_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            leave_type = self.request.GET.get('leave_type')
        except KeyError:
            leave_type = None
        if leave_type == '1' or leave_type == '2' or leave_type == '3' or leave_type == '5':
            profile = Profile.objects.filter(id__in = Designation.objects.values('profile_id'))
        elif leave_type == '4':
            profile = Profile.objects.all()
        else:
            profile = Profile.objects.none()
        context = {
            'profile':profile,
        }
        data['profile_data'] = render_to_string('administrator/transaction/profile_droplist.html',context)
        return JsonResponse(data)

class Transaction_Generated_Create_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Generated_TransactionForm(request.POST,request.FILES)
            if form.is_valid():
                if form.instance.leave_type == '1':
                    Profile.objects.filter(id = form.instance.profile_id).update(sl=F('sl')+form.instance.days)
                    Notification.objects.create(profile_id = form.instance.profile_id,detail="Generate sick leave",user_id = self.request.user.id)
                elif form.instance.leave_type == '2':
                    Profile.objects.filter(id = form.instance.profile_id).update(vl=F('vl')+form.instance.days)
                    Notification.objects.create(profile_id = form.instance.profile_id,detail="Generate vacation leave",user_id = self.request.user.id)
                elif form.instance.leave_type == '4':
                    Profile.objects.filter(id = form.instance.profile_id).update(overtime=F('overtime')+form.instance.days)
                    Notification.objects.create(profile_id = form.instance.profile_id,detail="Generate offset/overtime",user_id = self.request.user.id)
                form.instance.user_id = self.request.user.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully created.'
                data['form_is_valid'] = True
                data['url'] = reverse('transaction')
            else:
                data['form_is_valid'] = False
                data['message_type'] = error
                data['message_title'] = 'An error occurred.'
        return JsonResponse(data)

class Transaction_Batch_Generated_Create_Save_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def post(self, request):
        data =  dict()
        profile = Profile.objects.filter(id__in = Designation.objects.values('profile_id'))
        if request.method == 'POST':
            form = Batch_Generated_TransactionForm(request.POST,request.FILES)
            if form.is_valid():
                Profile.objects.filter(id__in = Designation.objects.values('profile_id')).update(sl=F('sl')+1.25,vl=F('vl')+1.25)
                for p in profile:
                    Generated_Transaction.objects.create(profile_id=p.id,remarks=form.instance.remarks,leave_type=1,days = 1.25,is_batch=True,user_id=self.request.user.id)
                    Generated_Transaction.objects.create(profile_id=p.id,remarks=form.instance.remarks,leave_type=2,days = 1.25,is_batch=True,user_id=self.request.user.id)
                    Notification.objects.create(profile_id = p.id,detail="Generate sick & vacation leave",user_id = self.request.user.id)
                form.instance.user_id = self.request.user.id
                form.save()
                data['message_type'] = success
                data['message_title'] = 'Successfully created.'
                data['form_is_valid'] = True
                data['url'] = reverse('transaction')
            else:
                data['form_is_valid'] = False
                data['message_type'] = error
                data['message_title'] = 'An error occurred.'
        return JsonResponse(data)

class Print_Leave_Report(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        now = timezone.now()
        profile = Profile.objects.get(id=self.request.user.profile.id)
        params = {
            'now': now,
            'profile': profile,
        }
        pdf = Render.render('pdf/leave.html', params)
        return pdf

class Print_Leave_Profile_Report(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request,pk):
        now = timezone.now()
        transaction = Deducted_Transaction.objects.filter(status=2,profile_id=pk)
        profile = Profile.objects.get(id=pk)
        params = {
            'now': now,
            'profile': profile,
            'transaction': transaction,
        }
        pdf = Render.render('pdf/leave.html', params)
        return pdf

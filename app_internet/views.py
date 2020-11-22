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

from .models import (
    Voucher,
    Generate_Ticket,
    Mikrotik
)
from .forms import (
    VoucherForm,
    Generate_TicketForm,
)

from app_info_profile.models import (
    Profile
)

from time import strptime

success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

import calendar
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from django.utils import timezone
import routeros_api
import random
from .render import (
    Render
)

class Main_Voucher_AJAXView(LoginRequiredMixin,View):
    queryset = Voucher.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
        except KeyError:
            filter = None
        if filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(profile_id = self.request.user.profile.id).count()
            voucher = self.queryset.filter(profile_id = self.request.user.profile.id).order_by('-date_created')[:int(filter)]
            data['voucher_table'] = render_to_string('main/components/list_voucher.html',{'voucher':voucher})
        return JsonResponse(data)


class Main_Voucher_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = VoucherForm()
        context = {
            'form': form,
            'btn_name': "primary",
            'btn_title': "Generate",
        }
        data['html_form'] = render_to_string('main/forms/voucher_forms.html',context)
        return JsonResponse(data)
    def post(self, request):
        data =  dict()
        now = timezone.now()
        validator = Voucher.objects.filter(profile_id = self.request.user.profile.id,date_created__day = now.day).count()
        if validator > 0:
            data['valid'] = False
            data['message_type'] = error
            data['message_title'] = "Limit 1 Voucher per day"
        else:
            if request.method == 'POST':
                voucher = str(random.randint(0000000000, 9999999999))
                connection = routeros_api.RouterOsApiPool('10.10.1.1', username='admin', password='password123*')
                print(connection)
                api = connection.get_api()
                list_queues = api.get_resource('/ip/hotspot/user')
                list_queues.add(name=voucher, profile="LIMIT 12HOURS",limit_uptime="10:00:00")
                form = VoucherForm(request.POST,request.FILES)
                if form.is_valid():
                    form.instance.voucher = voucher
                    form.instance.profile_id = self.request.user.profile.id
                    form.save()
                    data['valid'] = True
                    data['message_type'] = success
                    data['message_title'] = 'Successfully saved.'
                    data['url'] = reverse('main_voucher')
        return JsonResponse(data)

class Internet_Ticket_AJAXView(LoginRequiredMixin,View):
    queryset = Generate_Ticket.objects.all()

    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
        except KeyError:
            filter = None
        if filter:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.count()
            internet_ticket = self.queryset.order_by('-date_created')[:int(filter)]
            data['internet_ticket_table'] = render_to_string('administrator/ajax-filter-table/table_internet_ticket.html',{'internet_ticket':internet_ticket})
        return JsonResponse(data)

class Internet_Ticket_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = Generate_TicketForm()
        context = {
            'form': form,
            'btn_name': "primary",
            'btn_title': "Generate",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/internet_ticket_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Generate_TicketForm(request.POST,request.FILES)
            mikrotik = Mikrotik.objects.first()
            # MIKROTIK
            connection = routeros_api.RouterOsApiPool(mikrotik.ip_address, username=mikrotik.username, password=mikrotik.password)
            print(connection)
            try:
                api = connection.get_api()
                list_queues = api.get_resource('/ip/hotspot/user')
                # MIKROTIK CREATE USER
                if form.is_valid():
                    ticket = form.save()
                    for p in range(form.instance.no_ticket):
                        # GENERATE RANDOM TICKETS
                        voucher = str(random.randint(0000000, 9999999))
                        list_queues.add(name=voucher, profile=mikrotik.user_profile,limit_uptime=mikrotik.user_limit_uptime)
                        Voucher.objects.create(generate_ticket_id = ticket.id,voucher = voucher)
                    data['message_type'] = success
                    data['message_title'] = 'Successfully saved.'
                    data['url_print'] = reverse('internet_ticket_print',kwargs={'pk':ticket.id})
                    data['url'] = reverse('internet_ticket')
            except Exception as e:
                data['message_type'] = error
                data['message_title'] = 'Connection '+ str(e)

        return JsonResponse(data)

class Internet_Ticket_Print(LoginRequiredMixin,View):
    def get(self, request,pk):
        ticket = Voucher.objects.filter(generate_ticket_id = pk)
        context = {
            'ticket': ticket,
        }
        return render(request,'pdf/internet_ticket.html', context)

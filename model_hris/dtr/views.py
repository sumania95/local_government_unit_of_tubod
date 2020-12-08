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
from model_hris.designation.models import (
    Designation,
    Contractual,
)
from model_hris.dtr.forms import (
    Dtr_AssignForm,
)

from model_hris.dtr.models import (
    Dtr,
    Dtr_Assign,
    Scan_Attendace,
)
from model_hris.dtr.render import Render
from django.contrib.auth.mixins import LoginRequiredMixin
from app_hris.decorators import LogoutIfNotAdministratorHRISMixin


class Dtr_Assign_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    queryset = Dtr_Assign.objects.all()
    def get(self, request):
        data = dict()
        try:
            filter = self.request.GET.get('filter')
            search = self.request.GET.get('search')
        except KeyError:
            filter = None
            search = None
        print(search)
        if filter or search:
            data['form_is_valid'] = True
            data['counter'] = self.queryset.filter(Q(profile__surname__icontains = search)|Q(profile__firstname__icontains = search)).count()
            profile_assign = self.queryset.filter(Q(profile__surname__icontains = search)|Q(profile__firstname__icontains = search)).order_by('profile')[:int(filter)]
            data['profile_assign_table'] = render_to_string('administrator/ajax-filter-table/table_dtr_profile_assign.html',{'profile_assign':profile_assign})
        return JsonResponse(data)

class Dtr_Assign_Create_AJAXView(LoginRequiredMixin,View):
    def get(self, request):
        data = dict()
        form = Dtr_AssignForm()
        context = {
            'form': form,
            'is_Create': True,
            'btn_name': "primary",
            'btn_title': "Save",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/dtr_profile_assign_forms.html',context)
        return JsonResponse(data)

    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            form = Dtr_AssignForm(request.POST,request.FILES)
            try:
                if form.is_valid():
                    form.save()
                    data['valid'] = True
                    data['message_type'] = success
                    data['message_title'] = 'Successfully saved.'
                else:
                    data['valid'] = False
                    data['message_type'] = error
                    data['message_title'] = "Duplicated Biometric ID"
            except Exception as e:
                data['valid'] = False
                data['message_type'] = error
                data['message_title'] = str(e)

        return JsonResponse(data)

class Dtr_Assign_Update_AJAXView(LoginRequiredMixin,View):
    def get(self, request,pk):
        data = dict()
        dtr_profile_assign = Dtr_Assign.objects.get(id=pk)
        form = Dtr_AssignForm(instance=dtr_profile_assign)
        context = {
            'form': form,
            'is_Create': False,
            'dtr_profile_assign': dtr_profile_assign,
            'btn_name': "primary",
            'btn_title': "Update",
        }
        data['html_form'] = render_to_string('administrator/ajax-filter-components/dtr_profile_assign_forms.html',context)
        return JsonResponse(data)

    def post(self, request,pk):
        data =  dict()
        dtr_profile_assign = Dtr_Assign.objects.get(id=pk)
        if request.method == 'POST':
            try:
                form = Dtr_AssignForm(request.POST,request.FILES,instance = dtr_profile_assign)
                if form.is_valid():
                    form.save()
                    data['valid'] = True
                    data['message_type'] = success
                    data['message_title'] = 'Successfully updated.'
                else:
                    data['valid'] = False
                    data['message_type'] = error
                    data['message_title'] = "Duplicated Biometric ID"
            except Exception as e:
                data['valid'] = False
                data['message_type'] = error
                data['message_title'] = str(e)

        return JsonResponse(data)

# class Download_Attendance_Create_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorMixin,View):
#     def post(self,request):
#         data = dict()
#         ip = self.request.POST.get('ip')
#         print(ip)
#         if request.method == 'POST':
#             conn = None
#             zk = ZK(ip, port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
#             try:
#                 conn = zk.connect()
#                 conn.disable_device()
#                 attendances = conn.get_attendance()
#                 for attendance in attendances:
#                     print ('id : {}'.format(attendance.user_id))
#                     user_id = '{}'.format(attendance.user_id)
#                     timestamp = '{}'.format(attendance.timestamp)
#                     status = '{}'.format(attendance.status)
#                     punch = '{}'.format(attendance.punch)
#                     Attendance.objects.update_or_create(
#                         setassign_id = user_id,timestamp = timestamp,status = status,punch = punch,
#                         defaults={"setassign_id": user_id,"timestamp": timestamp,"status": status,"punch": punch}
#                     )
#                 conn.test_voice()
#                 conn.enable_device()
#                 data['message_type'] = success
#                 data['message_title'] = 'Successfully created.'
#                 data['form_is_valid'] = True
#                 return JsonResponse(data)
#             except Exception as e:
#                 print ("Process terminate : {}".format(e))
#                 data['message_type'] = error
#                 data['message_title'] = 'Error Connection Lost'
#                 data['form_is_valid'] = False
#                 return JsonResponse(data)
#             finally:
#                 if conn:
#                     conn.disconnect()
#         return JsonResponse(data)

class Daily_Time_Records_Print(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        try:
            month = self.request.GET.get('month')
            year = self.request.GET.get('year')
        except Exception as e:
            month = None
            year = None
        print(month)
        print(year)
        profile = Dtr_Assign.objects.exclude(id__in = Dtr.objects.values('user_id').filter(timestamp__month = month,timestamp__year = year)).order_by('profile__lastname','profile__surname')
        attendances = []
        for p in profile:
            attendance = {
            'profile' : Profile.objects.get(id=p.profile.id),
            'day1': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 1,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day2': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 2,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day3': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 3,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day4': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 4,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day5': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 5,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day6': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 6,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day7': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 7,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day8': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 8,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day9': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 9,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day10': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 10,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day11': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 11,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day12': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 12,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day13': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 13,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day14': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 14,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day15': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 15,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day16': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 16,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day17': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 17,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day18': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 18,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day19': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 19,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day20': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 20,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day21': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 21,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day22': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 22,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day23': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 23,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day24': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 24,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day25': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 25,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day26': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 26,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day27': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 27,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day28': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 28,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day29': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 29,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day30': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 30,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            'day31': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 31,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4],
            }
            attendances.append(attendance)
        params = {
            'final': attendances,

        }
        pdf = Render.render('pdf/dtr.html', params)
        return pdf

class QR_Daily_Time_Records_Print(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data =  dict()
        try:
            datepicker1 = self.request.GET.get('datepicker1')
            datepicker2 = self.request.GET.get('datepicker2')
        except Exception as e:
            datepicker1 = None
            datepicker2 = None
        data['form_is_valid'] = True
        data['url'] = reverse('dtr_qr_code_print')
        profile = Profile.objects.filter(id__in = Scan_Attendace.objects.values('profile_id').filter(timestamp__month = 11,timestamp__year = 2020)).order_by('surname','firstname')
        attendances = []
        for p in profile:
            attendance = {
            'profile' : Profile.objects.get(id=p.id),
            'day1': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 1,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day2': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 2,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day3': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 3,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day4': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 4,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day5': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 5,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day6': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 6,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day7': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 7,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day8': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 8,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day9': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 9,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day10': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 10,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day11': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 11,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day12': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 12,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day13': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 13,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day14': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 14,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day15': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 15,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day16': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 16,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day17': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 17,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day18': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 18,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day19': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 19,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day20': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 20,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day21': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 21,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day22': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 22,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day23': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 23,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day24': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 24,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day25': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 25,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day26': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 26,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day27': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 27,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day28': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 28,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day29': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 29,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day30': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 30,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            'day31': Scan_Attendace.objects.filter(profile_id = p.id,timestamp__day = 31,timestamp__month = 11,timestamp__year = 2020).order_by('timestamp__hour','timestamp__minute')[:4],
            }
            attendances.append(attendance)
        params = {
            'final': attendances,

        }
        pdf = Render.render('pdf/dtr.html', params)
        return pdf
        # if datepicker1.month == datepicker2.month:
        #     if datepicker1.day > datepicker2.day:
        #         data['message_type'] = error
        #         data['message_title'] = 'Invalid date!'
        #         data['form_is_valid'] = False
        #         return JsonResponse(data)
        #     else:
        #         data['form_is_valid'] = True
        #         data['url'] = reverse('dtr_qr_code_print')
        #         profile = Dtr_Assign.objects.exclude(id__in = Dtr.objects.values('user_id').filter(timestamp__month = month,timestamp__year = year)).order_by('profile__lastname','profile__surname')
        #         attendances = []
        #         for p in profile:
        #             attendance = {
        #             'profile' : Profile.objects.get(id=p.profile.id),
        #             'day1': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 1,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day2': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 2,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day3': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 3,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day4': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 4,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day5': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 5,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day6': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 6,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day7': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 7,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day8': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 8,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day9': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 9,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day10': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 10,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day11': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 11,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day12': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 12,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day13': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 13,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day14': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 14,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day15': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 15,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day16': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 16,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day17': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 17,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day18': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 18,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day19': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 19,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day20': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 20,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day21': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 21,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day22': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 22,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day23': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 23,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day24': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 24,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day25': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 25,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day26': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 26,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day27': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 27,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day28': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 28,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day29': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 29,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day30': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 30,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             'day31': Dtr.objects.filter(user_id = p.profile_id,timestamp__day = 31,timestamp__month = datepicker1.month,timestamp__year = datepicker1.year).order_by('timestamp__hour','timestamp__minute')[:4],
        #             }
        #             attendances.append(attendance)
        #         params = {
        #             'final': attendances,
        #
        #         }
        #         pdf = Render.render('pdf/dtr.html', params)
        #         return pdf
        # else:
        #     data['message_type'] = error
        #     data['message_title'] = 'Invalid date!'
        #     data['form_is_valid'] = False
        #     return JsonResponse(data)

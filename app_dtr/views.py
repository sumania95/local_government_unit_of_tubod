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
from app_designation.models import (
    Designation,
    Contractual,
)

from .models import (
    Dtr,
    Dtr_Assign,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from app_user_type.decorators import LogoutIfNotAdministratorHRISMixin
from .render import Render

class Daily_Time_Records_AJAXView(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        data = dict()
        try:
            id = self.request.GET.get('id')
        except KeyError:
            id = None

        month = 3
        year = 2020
        #
        attendance = []
        designation = Designation.objects.values('profile_id')
        contractual = Contractual.objects.values('profile_id')
        profile = Profile.objects.filter(id__in = [designation,contractual]).all()
        print(profile)
        #
        # for p in profile:
        #     day1 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 1,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day2 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 2,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day3 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 3,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day4 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 4,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day5 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 5,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day6 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 6,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day7 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 7,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day8 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 8,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day9 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 9,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day10 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 10,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day11 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 11,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day12 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 12,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day13 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 13,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day14 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 14,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day15 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 15,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day16 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 16,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day17 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 17,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day18 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 18,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day19 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 19,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day20 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 20,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day21 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 21,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day22 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 22,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day23 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 23,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day24 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 24,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day25 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 25,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day26 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 26,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day27 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 27,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day28 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 28,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day29 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 29,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day30 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 30,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     day31 = Dtr.objects.filter(user_id = p.dtr_assign.id,timestamp__day = 31,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        #     attendance.append(day1)
        #     attendance.append(day2)
        #     attendance.append(day3)
        #     attendance.append(day4)
        #     attendance.append(day5)
        #     attendance.append(day6)
        #     attendance.append(day7)
        #     attendance.append(day8)
        #     attendance.append(day9)
        #     attendance.append(day10)
        #     attendance.append(day11)
        #     attendance.append(day12)
        #     attendance.append(day13)
        #     attendance.append(day14)
        #     attendance.append(day15)
        #     attendance.append(day16)
        #     attendance.append(day17)
        #     attendance.append(day18)
        #     attendance.append(day19)
        #     attendance.append(day20)
        #     attendance.append(day21)
        #     attendance.append(day22)
        #     attendance.append(day23)
        #     attendance.append(day24)
        #     attendance.append(day25)
        #     attendance.append(day26)
        #     attendance.append(day27)
        #     attendance.append(day28)
        #     attendance.append(day29)
        #     attendance.append(day30)
        #     attendance.append(day31)
        print(attendance)
        context = {
            'attendance': attendance,
            # 'day1': day1,
            # 'day2': day2,
            # 'day3': day3,
            # 'day4': day4,
            # 'day5': day5,
            # 'day6': day6,
            # 'day7': day7,
            # 'day8': day8,
            # 'day9': day9,
            # 'day10': day10,
            # 'day11': day11,
            # 'day12': day12,
            # 'day13': day13,
            # 'day14': day14,
            # 'day15': day15,
            # 'day16': day16,
            # 'day17': day17,
            # 'day18': day18,
            # 'day19': day19,
            # 'day20': day20,
            # 'day21': day21,
            # 'day22': day22,
            # 'day23': day23,
            # 'day24': day24,
            # 'day25': day25,
            # 'day26': day26,
            # 'day27': day27,
            # 'day28': day28,
            # 'day29': day29,
            # 'day30': day30,
            # 'day31': day31,
        }
        data['profile_table'] = render_to_string('pdf/dtr_table.html',context)
        return JsonResponse(data)

class Daily_Time_Records_Print(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        profile = Profile.objects.all()
        month = 12
        year = 2019
        attendance = []
        profile_attendance = []
        final = []
        designation = Designation.objects.values('profile_id')
        contractual = Contractual.objects.values('profile_id')
        profile = Designation.objects.filter(profile_id__in = Dtr_Assign.objects.values('profile_id'))
        for p in profile:
            profile_attendance1 = Profile.objects.get(id=p.profile.id)
            day1 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 1,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day2 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 2,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day3 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 3,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day4 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 4,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day5 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 5,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day6 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 6,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day7 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 7,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day8 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 8,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day9 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 9,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day10 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 10,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day11 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 11,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day12 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 12,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day13 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 13,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day14 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 14,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day15 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 15,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day16 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 16,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day17 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 17,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day18 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 18,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day19 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 19,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day20 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 20,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day21 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 21,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day22 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 22,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day23 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 23,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day24 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 24,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day25 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 25,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day26 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 26,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day27 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 27,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day28 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 28,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day29 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 29,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day30 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 30,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            day31 = { 'day_attendance' : Dtr.objects.filter(user_id = p.profile.dtr_assign.profile_id,timestamp__day = 31,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]}
            attendance.append(day1)
            attendance.append(day2)
            attendance.append(day3)
            attendance.append(day4)
            attendance.append(day5)
            attendance.append(day6)
            attendance.append(day7)
            attendance.append(day8)
            attendance.append(day9)
            attendance.append(day10)
            attendance.append(day11)
            attendance.append(day12)
            attendance.append(day13)
            attendance.append(day14)
            attendance.append(day15)
            attendance.append(day16)
            attendance.append(day17)
            attendance.append(day18)
            attendance.append(day19)
            attendance.append(day20)
            attendance.append(day21)
            attendance.append(day22)
            attendance.append(day23)
            attendance.append(day24)
            attendance.append(day25)
            attendance.append(day26)
            attendance.append(day27)
            attendance.append(day28)
            attendance.append(day29)
            attendance.append(day30)
            attendance.append(day31)
            final1 = {
                'profile' : profile_attendance1,
                'attendance' : attendance
            }
            final.append(final1)
        print(final)
        params = {
            'final': final,

        }
        pdf = Render.render('pdf/dtr.html', params)
        return pdf

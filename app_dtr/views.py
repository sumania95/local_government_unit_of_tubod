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
    Dtr,
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
        day1 = Dtr.objects.filter(user_id = id,timestamp__day = 1,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day2 = Dtr.objects.filter(user_id = id,timestamp__day = 2,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day3 = Dtr.objects.filter(user_id = id,timestamp__day = 3,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day4 = Dtr.objects.filter(user_id = id,timestamp__day = 4,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day5 = Dtr.objects.filter(user_id = id,timestamp__day = 5,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day6 = Dtr.objects.filter(user_id = id,timestamp__day = 6,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day7 = Dtr.objects.filter(user_id = id,timestamp__day = 7,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day8 = Dtr.objects.filter(user_id = id,timestamp__day = 8,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day9 = Dtr.objects.filter(user_id = id,timestamp__day = 9,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day10 = Dtr.objects.filter(user_id = id,timestamp__day = 10,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day11 = Dtr.objects.filter(user_id = id,timestamp__day = 11,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day12 = Dtr.objects.filter(user_id = id,timestamp__day = 12,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day13 = Dtr.objects.filter(user_id = id,timestamp__day = 13,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day14 = Dtr.objects.filter(user_id = id,timestamp__day = 14,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day15 = Dtr.objects.filter(user_id = id,timestamp__day = 15,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day16 = Dtr.objects.filter(user_id = id,timestamp__day = 16,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day17 = Dtr.objects.filter(user_id = id,timestamp__day = 17,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day18 = Dtr.objects.filter(user_id = id,timestamp__day = 18,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day19 = Dtr.objects.filter(user_id = id,timestamp__day = 19,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day20 = Dtr.objects.filter(user_id = id,timestamp__day = 20,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day21 = Dtr.objects.filter(user_id = id,timestamp__day = 21,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day22 = Dtr.objects.filter(user_id = id,timestamp__day = 22,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day23 = Dtr.objects.filter(user_id = id,timestamp__day = 23,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day24 = Dtr.objects.filter(user_id = id,timestamp__day = 24,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day25 = Dtr.objects.filter(user_id = id,timestamp__day = 25,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day26 = Dtr.objects.filter(user_id = id,timestamp__day = 26,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day27 = Dtr.objects.filter(user_id = id,timestamp__day = 27,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day28 = Dtr.objects.filter(user_id = id,timestamp__day = 28,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day29 = Dtr.objects.filter(user_id = id,timestamp__day = 29,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day30 = Dtr.objects.filter(user_id = id,timestamp__day = 30,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day31 = Dtr.objects.filter(user_id = id,timestamp__day = 31,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        context = {
            'day1': day1,
            'day2': day2,
            'day3': day3,
            'day4': day4,
            'day5': day5,
            'day6': day6,
            'day7': day7,
            'day8': day8,
            'day9': day9,
            'day10': day10,
            'day11': day11,
            'day12': day12,
            'day13': day13,
            'day14': day14,
            'day15': day15,
            'day16': day16,
            'day17': day17,
            'day18': day18,
            'day19': day19,
            'day20': day20,
            'day21': day21,
            'day22': day22,
            'day23': day23,
            'day24': day24,
            'day25': day25,
            'day26': day26,
            'day27': day27,
            'day28': day28,
            'day29': day29,
            'day30': day30,
            'day31': day31,
        }
        data['profile_table'] = render_to_string('pdf/dtr_table.html',context)
        return JsonResponse(data)

class Daily_Time_Records_Print(LoginRequiredMixin,LogoutIfNotAdministratorHRISMixin,View):
    def get(self, request):
        profile = Profile.objects.all()
        month = 12
        year = 2019
        day1 = Dtr.objects.filter(timestamp__day = 1,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day2 = Dtr.objects.filter(timestamp__day = 2,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day3 = Dtr.objects.filter(timestamp__day = 3,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day4 = Dtr.objects.filter(timestamp__day = 4,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day5 = Dtr.objects.filter(timestamp__day = 5,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day6 = Dtr.objects.filter(timestamp__day = 6,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day7 = Dtr.objects.filter(timestamp__day = 7,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day8 = Dtr.objects.filter(timestamp__day = 8,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day9 = Dtr.objects.filter(timestamp__day = 9,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day10 = Dtr.objects.filter(timestamp__day = 10,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day11 = Dtr.objects.filter(timestamp__day = 11,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day12 = Dtr.objects.filter(timestamp__day = 12,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day13 = Dtr.objects.filter(timestamp__day = 13,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day14 = Dtr.objects.filter(timestamp__day = 14,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day15 = Dtr.objects.filter(timestamp__day = 15,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day16 = Dtr.objects.filter(timestamp__day = 16,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day17 = Dtr.objects.filter(timestamp__day = 17,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day18 = Dtr.objects.filter(timestamp__day = 18,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day19 = Dtr.objects.filter(timestamp__day = 19,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day20 = Dtr.objects.filter(timestamp__day = 20,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day21 = Dtr.objects.filter(timestamp__day = 21,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day22 = Dtr.objects.filter(timestamp__day = 22,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day23 = Dtr.objects.filter(timestamp__day = 23,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day24 = Dtr.objects.filter(timestamp__day = 24,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day25 = Dtr.objects.filter(timestamp__day = 25,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day26 = Dtr.objects.filter(timestamp__day = 26,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day27 = Dtr.objects.filter(timestamp__day = 27,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day28 = Dtr.objects.filter(timestamp__day = 28,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day29 = Dtr.objects.filter(timestamp__day = 29,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day30 = Dtr.objects.filter(timestamp__day = 30,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        day31 = Dtr.objects.filter(timestamp__day = 31,timestamp__month = month,timestamp__year = year).order_by('timestamp__hour','timestamp__minute')[:4]
        params = {
            'profile': profile,
            'day1': day1,
            'day2': day2,
            'day3': day3,
            'day4': day4,
            'day5': day5,
            'day6': day6,
            'day7': day7,
            'day8': day8,
            'day9': day9,
            'day10': day10,
            'day11': day11,
            'day12': day12,
            'day13': day13,
            'day14': day14,
            'day15': day15,
            'day16': day16,
            'day17': day17,
            'day18': day18,
            'day19': day19,
            'day20': day20,
            'day21': day21,
            'day22': day22,
            'day23': day23,
            'day24': day24,
            'day25': day25,
            'day26': day26,
            'day27': day27,
            'day28': day28,
            'day29': day29,
            'day30': day30,
            'day31': day31,
        }
        pdf = Render.render('pdf/dtr.html', params)
        return pdf

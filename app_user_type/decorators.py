from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.mixins import AccessMixin
from .models import Hr_Administrator

class LogoutIfNotAdministratorHRISMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        administrator = Hr_Administrator.objects.filter(user = self.request.user).count()
        if administrator == 0:
            return redirect('main_home')
        return super(LogoutIfNotAdministratorHRISMixin, self).dispatch(request, *args, **kwargs)

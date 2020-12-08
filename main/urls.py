"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

from django.views.static import serve
from model_hris.info_profile.views import (
    Login,
    Logout,
)

# import random

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('login', Login.as_view(), name = 'login'),
    path('logout', Logout.as_view(), name = 'logout'),
    path('admin/', admin.site.urls),
    path('x/',include('app_hris.urls')),
    path('',include('app_hris_user.urls')),
    # path('p/',include('app_procurement.urls')),
    path('p/',include('app_profiling.urls')),
    path('api/',include('model_hris.dtr.api.urls')),
    url(r'^imagefit/', include('imagefit.urls')),
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

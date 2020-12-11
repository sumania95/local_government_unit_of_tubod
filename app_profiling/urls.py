from django.urls import path
from .import views

from .views import (
    Tips_Dashboard_Page,
    Tips_Person_Page
)

from model_profiling.tips_person.views import (
    Tips_Person_Create_AJAXView,
)
from model_profiling.tips_address.views import (
    Tips_Province_AJAXView,
    Tips_City_Municipality_AJAXView,
    Tips_Barangay_AJAXView,
)

urlpatterns = [
    path('', Tips_Dashboard_Page.as_view(), name = 'tips_home'),
    path('person', Tips_Person_Page.as_view(), name = 'tips_person'),
    path('api/person/create', Tips_Person_Create_AJAXView.as_view(), name = 'api_tips_person_create'),

    # address api
    path('api/province', Tips_Province_AJAXView.as_view(), name = 'api_province'),
    path('api/city-municipality', Tips_City_Municipality_AJAXView.as_view(), name = 'api_city_municipality'),
    path('api/barangay', Tips_Barangay_AJAXView.as_view(), name = 'api_barangay'),
]

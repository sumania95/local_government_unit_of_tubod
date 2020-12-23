from django.urls import path
from .import views

from .views import (
    Tips_Dashboard_Page,
    Tips_Person_Page,
    Tips_Person_Detail_Create_Page,
    Tips_Person_Detail_Update_Page,
    Tips_Person_Detail_Page,
    Tips_Services_Assistance_Logs_Page,
)

from model_profiling.tips_person.views import (
    Tips_Person_Search_AJAXView,
    Tips_Person_Search_Result_AJAXView,
    Tips_Person_Create_AJAXView,
    Tips_Person_Update_AJAXView,
    Tips_Person_Create_Update_Category_AJAXView,
)
from model_profiling.tips_address.views import (
    Tips_Province_AJAXView,
    Tips_City_Municipality_AJAXView,
    Tips_Barangay_AJAXView,
)

from model_profiling.tips_nature_of_services.views import (
    Tips_Services_Assistance_Logs_AJAXView,
    Tips_Recommended_Services_AJAXView,
    Tips_Recommended_Services_Create_AJAXView,
    Tips_Recommended_Services_Create_Save_AJAXView,
    Tips_Sub_Category_AJAXView,
)

urlpatterns = [
    path('', Tips_Dashboard_Page.as_view(), name = 'tips_home'),
    path('person', Tips_Person_Page.as_view(), name = 'tips_person'),
    path('person/create', Tips_Person_Detail_Create_Page.as_view(), name = 'tips_person_create'),
    path('person/update/<int:pk>', Tips_Person_Detail_Update_Page.as_view(), name = 'tips_person_update'),
    path('api_person/search', Tips_Person_Search_AJAXView.as_view(), name = 'api_tips_person_search'),
    path('api_person/search/result', Tips_Person_Search_Result_AJAXView.as_view(), name = 'api_tips_person_search_result'),
    path('api/person/create', Tips_Person_Create_AJAXView.as_view(), name = 'api_tips_person_create'),
    path('api/person/update/<int:pk>', Tips_Person_Update_AJAXView.as_view(), name = 'api_tips_person_update'),
    path('person/detail/<int:pk>', Tips_Person_Detail_Page.as_view(), name = 'tips_person_detail'),
    path('api/person/detail/category/<int:pk>', Tips_Person_Create_Update_Category_AJAXView.as_view(), name = 'api_tips_person_create_update_category'),
    path('api/person/detail/recommended-services/', Tips_Recommended_Services_AJAXView.as_view(), name = 'api_tips_person_detail_recommended_services'),
    path('api/person/detail/recommended-services/create', Tips_Recommended_Services_Create_AJAXView.as_view(), name = 'api_tips_person_detail_recommended_services_create'),
    path('api/person/detail/recommended-services/create/save/<int:pk>', Tips_Recommended_Services_Create_Save_AJAXView.as_view(), name = 'api_tips_person_detail_recommended_services_create_save'),
    path('services-assistance/logs', Tips_Services_Assistance_Logs_Page.as_view(), name = 'tips_services_assistance_logs'),
    path('api/services-assistance/logs', Tips_Services_Assistance_Logs_AJAXView.as_view(), name = 'api_tips_services_assistance_logs'),


    # address api
    path('api/province', Tips_Province_AJAXView.as_view(), name = 'api_province'),
    path('api/city-municipality', Tips_City_Municipality_AJAXView.as_view(), name = 'api_city_municipality'),
    path('api/barangay', Tips_Barangay_AJAXView.as_view(), name = 'api_barangay'),
    path('api/sub-category', Tips_Sub_Category_AJAXView.as_view(), name = 'api_sub_category'),
]

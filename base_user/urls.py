from django.urls import path
from .import views

from .views import (
    Home_Page,
    History_Leave_Page,
    History_Leave_Create,
    Earn_Rewards_Page,
    Voucher_Page,
    Voucher_Create,
    Profile_Info_Page,
    Security_Page,
)

from app_post.views import (
    Post_AJAXView,
    Post_Create_AJAXView,
    Post_Like_AJAXView,
    Post_Comment_AJAXView,
)
from app_info_profile.views import (
    Main_Profile_Sidebar_AJAXView,
    Main_Profile_Basic_Info_AJAXView,
    Main_Notification_Template_AJAXView,
    Main_Notification_AJAXView,
    Main_Security_AJAXView,
)

from app_rewards_recognitions.views import (
    Earn_Rewards_AJAXView,
)

from app_internet.views import (
    Main_Voucher_AJAXView,
    Main_Voucher_Create_AJAXView,
)

from app_transaction.views import (
    Profile_History_Leave_AJAXView,
    Profile_History_Leave_Create_AJAXView,
)
from app_201_pds.views import (
    Main_Profile_Family_Background_AJAXView,
    Main_Profile_Children_AJAXView,
    Main_Profile_Children_Table_AJAXView,
    Main_Profile_Educational_Background_AJAXView,
    Main_Profile_Educational_Background_Table_AJAXView,
    Main_Profile_Eligibility_AJAXView,
    Main_Profile_Eligibility_Table_AJAXView,
)

urlpatterns = [
    path('', Home_Page.as_view(), name = 'main_home'),
    path('api/post', Post_AJAXView.as_view(), name = 'api_main_post'),
    path('api/main/sidebar', Main_Profile_Sidebar_AJAXView.as_view(), name = 'api_main_sidebar'),
    path('api/post/create', Post_Create_AJAXView.as_view(), name = 'api_main_post_create'),
    path('api/post/like/<int:pk>', Post_Like_AJAXView.as_view(), name = 'api_main_post_like'),
    path('api/post/comment/<int:pk>', Post_Comment_AJAXView.as_view(), name = 'api_main_post_comment'),
    path('history-leave', History_Leave_Page.as_view(), name = 'main_history_leave'),
    path('api/history-leave', Profile_History_Leave_AJAXView.as_view(), name = 'api_main_history_leave'),
    path('history-leave/create', History_Leave_Create.as_view(), name = 'main_history_leave_create'),
    path('api/history-leave/create', Profile_History_Leave_Create_AJAXView.as_view(), name = 'api_main_history_leave_create'),
    path('earn-rewards', Earn_Rewards_Page.as_view(), name = 'main_earn_rewards'),
    path('api/earn-rewards', Earn_Rewards_AJAXView.as_view(), name = 'api_main_earn_rewards'),
    path('voucher', Voucher_Page.as_view(), name = 'main_voucher'),
    path('api/voucher', Main_Voucher_AJAXView.as_view(), name = 'api_main_voucher'),
    path('voucher/create', Voucher_Create.as_view(), name = 'main_voucher_create'),
    path('api/voucher/create', Main_Voucher_Create_AJAXView.as_view(), name = 'api_main_voucher_create'),
    path('profile-info', Profile_Info_Page.as_view(), name = 'main_profile_info'),
    path('api/basic-info', Main_Profile_Basic_Info_AJAXView.as_view(), name = 'api_main_basic_info'),
    path('api/family-background', Main_Profile_Family_Background_AJAXView.as_view(), name = 'api_main_family_background'),
    path('api/children', Main_Profile_Children_AJAXView.as_view(), name = 'api_main_children'),
    path('api/children-list', Main_Profile_Children_Table_AJAXView.as_view(), name = 'api_main_children_list'),
    path('api/education-background', Main_Profile_Educational_Background_AJAXView.as_view(), name = 'api_main_education_background'),
    path('api/education-background-list', Main_Profile_Educational_Background_Table_AJAXView.as_view(), name = 'api_main_education_background_list'),
    path('api/eligibility', Main_Profile_Eligibility_AJAXView.as_view(), name = 'api_main_eligibility'),
    path('api/eligibility-list', Main_Profile_Eligibility_Table_AJAXView.as_view(), name = 'api_main_eligibility_list'),
    # NOTIFICATION
    path('api/notification/notification', Main_Notification_Template_AJAXView.as_view(), name = 'api_main_notification_notification'),
    path('api/notification/notification/content', Main_Notification_AJAXView.as_view(), name = 'api_main_notification_notification_content'),
    # security
    path('security', Security_Page.as_view(), name = 'main_security'),
    path('api/security/update', Main_Security_AJAXView.as_view(), name = 'api_main_security'),


]

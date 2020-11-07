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
    Main_Profile_Leave_Remaining_Template_AJAXView,
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
    Main_Profile_Children_Create_AJAXView,
    Main_Profile_Children_Update_AJAXView,
    Main_Profile_Children_Delete_AJAXView,
    Main_Profile_Educational_Background_AJAXView,
    Main_Profile_Educational_Background_Table_AJAXView,
    Main_Profile_Educational_Background_Create_AJAXView,
    Main_Profile_Educational_Background_Update_AJAXView,
    Main_Profile_Educational_Background_Delete_AJAXView,
    Main_Profile_Eligibility_AJAXView,
    Main_Profile_Eligibility_Table_AJAXView,
    Main_Profile_Eligibility_Create_AJAXView,
    Main_Profile_Eligibility_Update_AJAXView,
    Main_Profile_Eligibility_Delete_AJAXView,
    Main_Profile_Work_Experience_AJAXView,
    Main_Profile_Work_Experience_Table_AJAXView,
    Main_Profile_Work_Experience_Create_AJAXView,
    Main_Profile_Work_Experience_Update_AJAXView,
    Main_Profile_Work_Experience_Delete_AJAXView,
    Main_Profile_Voluntary_Work_AJAXView,
    Main_Profile_Voluntary_Work_Table_AJAXView,
    Main_Profile_Voluntary_Work_Create_AJAXView,
    Main_Profile_Voluntary_Work_Update_AJAXView,
    Main_Profile_Voluntary_Work_Delete_AJAXView,
    Main_Profile_Learning_Development_AJAXView,
    Main_Profile_Learning_Development_Table_AJAXView,
    Main_Profile_Learning_Development_Create_AJAXView,
    Main_Profile_Learning_Development_Update_AJAXView,
    Main_Profile_Learning_Development_Delete_AJAXView,
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
    path('api/leave-remaining', Main_Profile_Leave_Remaining_Template_AJAXView.as_view(), name = 'api_main_leave_remaining'),
    path('history-leave/create', History_Leave_Create.as_view(), name = 'main_history_leave_create'),
    path('api/history-leave/create', Profile_History_Leave_Create_AJAXView.as_view(), name = 'api_main_history_leave_create'),
    path('earn-rewards', Earn_Rewards_Page.as_view(), name = 'main_earn_rewards'),
    path('api/earn-rewards', Earn_Rewards_AJAXView.as_view(), name = 'api_main_earn_rewards'),
    path('voucher', Voucher_Page.as_view(), name = 'main_voucher'),
    path('api/voucher', Main_Voucher_AJAXView.as_view(), name = 'api_main_voucher'),
    # path('voucher/create', Voucher_Create.as_view(), name = 'main_voucher_create'),
    # path('api/voucher/create', Main_Voucher_Create_AJAXView.as_view(), name = 'api_main_voucher_create'),
    path('profile-info', Profile_Info_Page.as_view(), name = 'main_profile_info'),
    path('api/basic-info', Main_Profile_Basic_Info_AJAXView.as_view(), name = 'api_main_basic_info'),
    path('api/family-background', Main_Profile_Family_Background_AJAXView.as_view(), name = 'api_main_family_background'),
    # CHILDREN
    path('api/children', Main_Profile_Children_AJAXView.as_view(), name = 'api_main_children'),
    path('api/children-list', Main_Profile_Children_Table_AJAXView.as_view(), name = 'api_main_children_list'),
    path('api/children/create', Main_Profile_Children_Create_AJAXView.as_view(), name = 'api_main_children_create'),
    path('api/children/update/<int:pk>', Main_Profile_Children_Update_AJAXView.as_view(), name = 'api_main_children_update'),
    path('api/children/delete/<int:pk>', Main_Profile_Children_Delete_AJAXView.as_view(), name = 'api_main_children_delete'),
    # EDUCATIONAL BACKGROUND
    path('api/education-background', Main_Profile_Educational_Background_AJAXView.as_view(), name = 'api_main_education_background'),
    path('api/education-background-list', Main_Profile_Educational_Background_Table_AJAXView.as_view(), name = 'api_main_education_background_list'),
    path('api/educational-background/create', Main_Profile_Educational_Background_Create_AJAXView.as_view(), name = 'api_main_educational_background_create'),
    path('api/educational-background/update/<int:pk>', Main_Profile_Educational_Background_Update_AJAXView.as_view(), name = 'api_main_educational_background_update'),
    path('api/educational-background/delete/<int:pk>', Main_Profile_Educational_Background_Delete_AJAXView.as_view(), name = 'api_main_educational_background_delete'),
    # ELIGIBILITY
    path('api/eligibility', Main_Profile_Eligibility_AJAXView.as_view(), name = 'api_main_eligibility'),
    path('api/eligibility-list', Main_Profile_Eligibility_Table_AJAXView.as_view(), name = 'api_main_eligibility_list'),
    path('api/eligibility/create', Main_Profile_Eligibility_Create_AJAXView.as_view(), name = 'api_main_eligibility_create'),
    path('api/eligibility/update/<int:pk>', Main_Profile_Eligibility_Update_AJAXView.as_view(), name = 'api_main_eligibility_update'),
    path('api/eligibility/delete/<int:pk>', Main_Profile_Eligibility_Delete_AJAXView.as_view(), name = 'api_main_eligibility_delete'),
    # WORK EXPERIENCE
    path('api/work-experience', Main_Profile_Work_Experience_AJAXView.as_view(), name = 'api_main_work_experience'),
    path('api/work-experience-list', Main_Profile_Work_Experience_Table_AJAXView.as_view(), name = 'api_main_work_experience_list'),
    path('api/work-experience/create', Main_Profile_Work_Experience_Create_AJAXView.as_view(), name = 'api_main_work_experience_create'),
    path('api/work-experience/update/<int:pk>', Main_Profile_Work_Experience_Update_AJAXView.as_view(), name = 'api_main_work_experience_update'),
    path('api/work-experience/delete/<int:pk>', Main_Profile_Work_Experience_Delete_AJAXView.as_view(), name = 'api_main_work_experience_delete'),
    # VOULUNTARY WORK
    path('api/voluntary-work', Main_Profile_Voluntary_Work_AJAXView.as_view(), name = 'api_main_voluntary_work'),
    path('api/voluntary-work-list', Main_Profile_Voluntary_Work_Table_AJAXView.as_view(), name = 'api_main_voluntary_work_list'),
    path('api/voluntary-work/create', Main_Profile_Voluntary_Work_Create_AJAXView.as_view(), name = 'api_main_voluntary_work_create'),
    path('api/voluntary-work/update/<int:pk>', Main_Profile_Voluntary_Work_Update_AJAXView.as_view(), name = 'api_main_voluntary_work_update'),
    path('api/voluntary-work/delete/<int:pk>', Main_Profile_Voluntary_Work_Delete_AJAXView.as_view(), name = 'api_main_voluntary_work_delete'),
    # LEARNING DEVELOPMENT
    path('api/learning-development', Main_Profile_Learning_Development_AJAXView.as_view(), name = 'api_main_learning_development'),
    path('api/learning-development-list', Main_Profile_Learning_Development_Table_AJAXView.as_view(), name = 'api_main_learning_development_list'),
    path('api/learning-development/create', Main_Profile_Learning_Development_Create_AJAXView.as_view(), name = 'api_main_learning_development_create'),
    path('api/learning-development/update/<int:pk>', Main_Profile_Learning_Development_Update_AJAXView.as_view(), name = 'api_main_learning_development_update'),
    path('api/learning-development/delete/<int:pk>', Main_Profile_Learning_Development_Delete_AJAXView.as_view(), name = 'api_main_learning_development_delete'),
    # NOTIFICATION
    path('api/notification/notification', Main_Notification_Template_AJAXView.as_view(), name = 'api_main_notification_notification'),
    path('api/notification/notification/content', Main_Notification_AJAXView.as_view(), name = 'api_main_notification_notification_content'),
    # security
    path('security', Security_Page.as_view(), name = 'main_security'),
    path('api/security/update', Main_Security_AJAXView.as_view(), name = 'api_main_security'),


]

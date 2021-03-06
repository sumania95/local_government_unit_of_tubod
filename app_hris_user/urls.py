from django.urls import path
from .import views

from .views import (
    Home_Page,
    History_Leave_Page,
    History_Leave_Create,
    Earn_Rewards_Page,
    Document_Page,
    Accomplishment_Page,
    Profile_Info_Page,
    Security_Page,
)

from model_hris.performance_management.views import (
    Main_Accomplishment_AJAXView,
    # Main_Complied_Create_AJAXView,
    # Main_Accomplished_AJAXView,
    Main_Accomplishment_Create_AJAXView,
    Main_Accomplishment_Update_AJAXView,
)

from model_hris.post.views import (
    Post_AJAXView,
    Post_Create_AJAXView,
    Post_Like_AJAXView,
    Post_Comment_AJAXView,
)
from model_hris.info_profile.views import (
    Main_Profile_Leave_Remaining_Template_AJAXView,
    Main_Profile_Sidebar_AJAXView,
    Main_Profile_Basic_Info_AJAXView,
    Main_Notification_Template_AJAXView,
    Main_Notification_AJAXView,
    Main_Security_AJAXView,
)

from model_hris.rewards_recognitions.views import (
    Earn_Rewards_AJAXView,
)

from model_hris.document.views import (
    Main_Document_AJAXView,
)


from model_hris.transaction.views import (
    Profile_History_Leave_AJAXView,
    Profile_History_Leave_Create_AJAXView,
    Profile_History_Leave_Delete_Save_AJAXView,
    Self_Print_Leave_Form_Report,
)
from model_hris.pds.views import (
    Main_Profile_Family_Background_AJAXView,
    Main_Profile_Q34_AJAXView,
    Main_Profile_Q35_AJAXView,
    Main_Profile_Q36_AJAXView,
    Main_Profile_Q37_AJAXView,
    Main_Profile_Q38_AJAXView,
    Main_Profile_Q39_AJAXView,
    Main_Profile_Q40_AJAXView,
    Main_Profile_References1_AJAXView,
    Main_Profile_References2_AJAXView,
    Main_Profile_References3_AJAXView,
    Main_Profile_Government_Other_Info_AJAXView,
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
    # skill & hobbies
    Main_Profile_Skill_Hobbies_AJAXView,
    Main_Profile_Skill_Hobbies_Table_AJAXView,
    Main_Profile_Skill_Hobbies_Create_AJAXView,
    Main_Profile_Skill_Hobbies_Update_AJAXView,
    Main_Profile_Skill_Hobbies_Delete_AJAXView,
    # non academic
    Main_Profile_Non_Academic_AJAXView,
    Main_Profile_Non_Academic_Table_AJAXView,
    Main_Profile_Non_Academic_Create_AJAXView,
    Main_Profile_Non_Academic_Update_AJAXView,
    Main_Profile_Non_Academic_Delete_AJAXView,
    # member organization
    Main_Profile_Member_Organization_AJAXView,
    Main_Profile_Member_Organization_Table_AJAXView,
    Main_Profile_Member_Organization_Create_AJAXView,
    Main_Profile_Member_Organization_Update_AJAXView,
    Main_Profile_Member_Organization_Delete_AJAXView,


    # PRINT PDS
    Self_Print_Personal_Data_Sheet_Report,
)

from model_hris.saln.views import (
    Main_Profile_Saln_Business_Interest_Financial_Connections_AJAXView,
    Main_Profile_Saln_Business_Interest_Financial_Connections_Table_AJAXView,
    Main_Profile_Saln_Business_Interest_Financial_Connections_Create_AJAXView,
    Main_Profile_Saln_Business_Interest_Financial_Connections_Update_AJAXView,
    Main_Profile_Saln_Business_Interest_Financial_Connections_Delete_AJAXView,

    # LIABILITIES
    Main_Profile_Saln_Liabilities_AJAXView,
    Main_Profile_Saln_Liabilities_Table_AJAXView,
    Main_Profile_Saln_Liabilities_Create_AJAXView,
    Main_Profile_Saln_Liabilities_Update_AJAXView,
    Main_Profile_Saln_Liabilities_Delete_AJAXView,

    # PERSONAL PROPERTIES
    Main_Profile_Saln_Personal_Properties_AJAXView,
    Main_Profile_Saln_Personal_Properties_Table_AJAXView,
    Main_Profile_Saln_Personal_Properties_Create_AJAXView,
    Main_Profile_Saln_Personal_Properties_Update_AJAXView,
    Main_Profile_Saln_Personal_Properties_Delete_AJAXView,

    # Real PROPERTIES
    Main_Profile_Saln_Real_Properties_AJAXView,
    Main_Profile_Saln_Real_Properties_Table_AJAXView,
    Main_Profile_Saln_Real_Properties_Create_AJAXView,
    Main_Profile_Saln_Real_Properties_Update_AJAXView,
    Main_Profile_Saln_Real_Properties_Delete_AJAXView,

    # Relatives_In_The_Government_Service
    Main_Profile_Saln_Relatives_In_The_Government_Service_AJAXView,
    Main_Profile_Saln_Relatives_In_The_Government_Service_Table_AJAXView,
    Main_Profile_Saln_Relatives_In_The_Government_Service_Create_AJAXView,
    Main_Profile_Saln_Relatives_In_The_Government_Service_Update_AJAXView,
    Main_Profile_Saln_Relatives_In_The_Government_Service_Delete_AJAXView,

    # FILLING TYPE
    Main_Profile_Saln_Filling_AJAXView,
    #Print
    Self_Print_SALN_Report,
)

urlpatterns = [
    path('201-file/print/leave-form/<int:pk>', Self_Print_Leave_Form_Report.as_view(), name = 'main_self_print_leave_form'),
    path('201-file/print/pds', Self_Print_Personal_Data_Sheet_Report.as_view(), name = 'main_self_print_pds'),
    path('201-file/print/saln', Self_Print_SALN_Report.as_view(), name = 'main_self_print_saln'),
    path('', Home_Page.as_view(), name = 'main_home'),
    path('api/post', Post_AJAXView.as_view(), name = 'api_main_post'),
    path('api/main/sidebar', Main_Profile_Sidebar_AJAXView.as_view(), name = 'api_main_sidebar'),
    path('api/post/create', Post_Create_AJAXView.as_view(), name = 'api_main_post_create'),
    path('api/post/like/<int:pk>', Post_Like_AJAXView.as_view(), name = 'api_main_post_like'),
    path('api/post/comment/<int:pk>', Post_Comment_AJAXView.as_view(), name = 'api_main_post_comment'),
    path('history-leave', History_Leave_Page.as_view(), name = 'main_history_leave'),
    path('api/history-leave', Profile_History_Leave_AJAXView.as_view(), name = 'api_main_history_leave'),
    path('api/history-leave/delete/<int:pk>', Profile_History_Leave_Delete_Save_AJAXView.as_view(), name = 'api_main_history_leave_delete_save'),
    path('api/leave-remaining', Main_Profile_Leave_Remaining_Template_AJAXView.as_view(), name = 'api_main_leave_remaining'),
    path('history-leave/create', History_Leave_Create.as_view(), name = 'main_history_leave_create'),
    path('api/history-leave/create', Profile_History_Leave_Create_AJAXView.as_view(), name = 'api_main_history_leave_create'),
    path('earn-rewards', Earn_Rewards_Page.as_view(), name = 'main_earn_rewards'),
    path('api/earn-rewards', Earn_Rewards_AJAXView.as_view(), name = 'api_main_earn_rewards'),
    path('document', Document_Page.as_view(), name = 'main_document'),
    path('api/document', Main_Document_AJAXView.as_view(), name = 'api_main_document'),
    path('ipcr-opcr', Accomplishment_Page.as_view(), name = 'main_accomplishment'),
    path('api/ipcr-opcr', Main_Accomplishment_AJAXView.as_view(), name = 'api_main_accomplishment'),
    # path('api/accomplished', Main_Accomplished_AJAXView.as_view(), name = 'api_main_accomplished'),
    path('api/accomplishment/create', Main_Accomplishment_Create_AJAXView.as_view(), name = 'api_main_accomplishment_create'),
    path('api/accomplishment/update/<int:pk>', Main_Accomplishment_Update_AJAXView.as_view(), name = 'api_main_accomplishment_update'),
    # path('api/accomplied/create/<int:pk>', Main_Complied_Create_AJAXView.as_view(), name = 'api_main_complied_create'),
    path('profile-info', Profile_Info_Page.as_view(), name = 'main_profile_info'),
    path('api/basic-info', Main_Profile_Basic_Info_AJAXView.as_view(), name = 'api_main_basic_info'),
    path('api/family-background', Main_Profile_Family_Background_AJAXView.as_view(), name = 'api_main_family_background'),
    path('api/q34', Main_Profile_Q34_AJAXView.as_view(), name = 'api_main_q34'),
    path('api/q35', Main_Profile_Q35_AJAXView.as_view(), name = 'api_main_q35'),
    path('api/q36', Main_Profile_Q36_AJAXView.as_view(), name = 'api_main_q36'),
    path('api/q37', Main_Profile_Q37_AJAXView.as_view(), name = 'api_main_q37'),
    path('api/q38', Main_Profile_Q38_AJAXView.as_view(), name = 'api_main_q38'),
    path('api/q39', Main_Profile_Q39_AJAXView.as_view(), name = 'api_main_q39'),
    path('api/q40', Main_Profile_Q40_AJAXView.as_view(), name = 'api_main_q40'),
    path('api/references1', Main_Profile_References1_AJAXView.as_view(), name = 'api_main_references1'),
    path('api/references2', Main_Profile_References2_AJAXView.as_view(), name = 'api_main_references2'),
    path('api/references3', Main_Profile_References3_AJAXView.as_view(), name = 'api_main_references3'),
    path('api/government-other-info', Main_Profile_Government_Other_Info_AJAXView.as_view(), name = 'api_main_government_other_info'),
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
    # SKILLS & HOBBIES
    path('api/skill-hobbies', Main_Profile_Skill_Hobbies_AJAXView.as_view(), name = 'api_main_skill_hobbies'),
    path('api/skill-hobbies-list', Main_Profile_Skill_Hobbies_Table_AJAXView.as_view(), name = 'api_main_skill_hobbies_list'),
    path('api/skill-hobbies/create', Main_Profile_Skill_Hobbies_Create_AJAXView.as_view(), name = 'api_main_skill_hobbies_create'),
    path('api/skill-hobbies/update/<int:pk>', Main_Profile_Skill_Hobbies_Update_AJAXView.as_view(), name = 'api_main_skill_hobbies_update'),
    path('api/skill-hobbies/delete/<int:pk>', Main_Profile_Skill_Hobbies_Delete_AJAXView.as_view(), name = 'api_main_skill_hobbies_delete'),
    # NON ACADEMIC
    path('api/non-academic', Main_Profile_Non_Academic_AJAXView.as_view(), name = 'api_main_non_academic'),
    path('api/non-academic-list', Main_Profile_Non_Academic_Table_AJAXView.as_view(), name = 'api_main_non_academic_list'),
    path('api/non-academic/create', Main_Profile_Non_Academic_Create_AJAXView.as_view(), name = 'api_main_non_academic_create'),
    path('api/non-academic/update/<int:pk>', Main_Profile_Non_Academic_Update_AJAXView.as_view(), name = 'api_main_non_academic_update'),
    path('api/non-academic/delete/<int:pk>', Main_Profile_Non_Academic_Delete_AJAXView.as_view(), name = 'api_main_non_academic_delete'),
    # MEMBER ORGANIZATION
    path('api/member-organization', Main_Profile_Member_Organization_AJAXView.as_view(), name = 'api_main_member_organization'),
    path('api/member-organization-list', Main_Profile_Member_Organization_Table_AJAXView.as_view(), name = 'api_main_member_organization_list'),
    path('api/member-organization/create', Main_Profile_Member_Organization_Create_AJAXView.as_view(), name = 'api_main_member_organization_create'),
    path('api/member-organization/update/<int:pk>', Main_Profile_Member_Organization_Update_AJAXView.as_view(), name = 'api_main_member_organization_update'),
    path('api/member-organization/delete/<int:pk>', Main_Profile_Member_Organization_Delete_AJAXView.as_view(), name = 'api_main_member_organization_delete'),
    # NOTIFICATION
    path('api/notification/notification', Main_Notification_Template_AJAXView.as_view(), name = 'api_main_notification_notification'),
    path('api/notification/notification/content', Main_Notification_AJAXView.as_view(), name = 'api_main_notification_notification_content'),
    # security
    path('security', Security_Page.as_view(), name = 'main_security'),
    path('api/security/update', Main_Security_AJAXView.as_view(), name = 'api_main_security'),

    # SALN
    path('api/filling-type', Main_Profile_Saln_Filling_AJAXView.as_view(), name = 'api_main_saln_filling'),

    # Business Interest Fianancial Connections
    path('api/business-interest-financial-connections', Main_Profile_Saln_Business_Interest_Financial_Connections_AJAXView.as_view(), name = 'api_main_business_interest_financial_connections'),
    path('api/business-interest-financial-connections-list', Main_Profile_Saln_Business_Interest_Financial_Connections_Table_AJAXView.as_view(), name = 'api_main_business_interest_financial_connections_list'),
    path('api/business-interest-financial-connections/create', Main_Profile_Saln_Business_Interest_Financial_Connections_Create_AJAXView.as_view(), name = 'api_main_business_interest_financial_connections_create'),
    path('api/business-interest-financial-connections/update/<int:pk>', Main_Profile_Saln_Business_Interest_Financial_Connections_Update_AJAXView.as_view(), name = 'api_main_business_interest_financial_connections_update'),
    path('api/business-interest-financial-connections/delete/<int:pk>', Main_Profile_Saln_Business_Interest_Financial_Connections_Delete_AJAXView.as_view(), name = 'api_main_business_interest_financial_connections_delete'),
    # LIABILITIES
    path('api/liabilities', Main_Profile_Saln_Liabilities_AJAXView.as_view(), name = 'api_main_liabilities'),
    path('api/liabilities-list', Main_Profile_Saln_Liabilities_Table_AJAXView.as_view(), name = 'api_main_liabilities_list'),
    path('api/liabilities/create', Main_Profile_Saln_Liabilities_Create_AJAXView.as_view(), name = 'api_main_liabilities_create'),
    path('api/liabilities/update/<int:pk>', Main_Profile_Saln_Liabilities_Update_AJAXView.as_view(), name = 'api_main_liabilities_update'),
    path('api/liabilities/delete/<int:pk>', Main_Profile_Saln_Liabilities_Delete_AJAXView.as_view(), name = 'api_main_liabilities_delete'),

    # PERSONAL PROPERTIES
    path('api/personal-properties', Main_Profile_Saln_Personal_Properties_AJAXView.as_view(), name = 'api_main_personal_properties'),
    path('api/personal-properties-list', Main_Profile_Saln_Personal_Properties_Table_AJAXView.as_view(), name = 'api_main_personal_properties_list'),
    path('api/personal-properties/create', Main_Profile_Saln_Personal_Properties_Create_AJAXView.as_view(), name = 'api_main_personal_properties_create'),
    path('api/personal-properties/update/<int:pk>', Main_Profile_Saln_Personal_Properties_Update_AJAXView.as_view(), name = 'api_main_personal_properties_update'),
    path('api/personal-properties/delete/<int:pk>', Main_Profile_Saln_Personal_Properties_Delete_AJAXView.as_view(), name = 'api_main_personal_properties_delete'),

    # PERSONAL PROPERTIES
    path('api/real-properties', Main_Profile_Saln_Real_Properties_AJAXView.as_view(), name = 'api_main_real_properties'),
    path('api/real-properties-list', Main_Profile_Saln_Real_Properties_Table_AJAXView.as_view(), name = 'api_main_real_properties_list'),
    path('api/real-properties/create', Main_Profile_Saln_Real_Properties_Create_AJAXView.as_view(), name = 'api_main_real_properties_create'),
    path('api/real-properties/update/<int:pk>', Main_Profile_Saln_Real_Properties_Update_AJAXView.as_view(), name = 'api_main_real_properties_update'),
    path('api/real-properties/delete/<int:pk>', Main_Profile_Saln_Real_Properties_Delete_AJAXView.as_view(), name = 'api_main_real_properties_delete'),
    # Relatives in the government services
    path('api/relatives-in-the-government-service', Main_Profile_Saln_Relatives_In_The_Government_Service_AJAXView.as_view(), name = 'api_main_relatives_in_the_government_service'),
    path('api/relatives-in-the-government-service-list', Main_Profile_Saln_Relatives_In_The_Government_Service_Table_AJAXView.as_view(), name = 'api_main_relatives_in_the_government_service_list'),
    path('api/relatives-in-the-government-service/create', Main_Profile_Saln_Relatives_In_The_Government_Service_Create_AJAXView.as_view(), name = 'api_main_relatives_in_the_government_service_create'),
    path('api/relatives-in-the-government-service/update/<int:pk>', Main_Profile_Saln_Relatives_In_The_Government_Service_Update_AJAXView.as_view(), name = 'api_main_relatives_in_the_government_service_update'),
    path('api/relatives-in-the-government-service/delete/<int:pk>', Main_Profile_Saln_Relatives_In_The_Government_Service_Delete_AJAXView.as_view(), name = 'api_main_relatives_in_the_government_service_delete'),

]

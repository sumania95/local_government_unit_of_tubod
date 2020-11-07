from django.urls import path
from .import views

from .views import (
    Dashboard,
    Dashboard_Panels_AJAXView,
    Profile,
    Profile_Create,
    Profile_Update,
    Profile_Detail,
    Profile_Detail_Learning_Development_AJAXView,
    Profile_Detail_Security,
    Profile_Detail_Service_Create,
    Profile_Detail_Service_Update,
    Designation,
    Designation_Designated_Create,
    Designation_Contractual_Create,
    # Designation_Plantilla_Create,
    # Designation_Plantilla_Update,
    Learning_Development,
    Rewards_Recognitions,
    Rewards_Recognitions_Create,
    Rewards_Recognitions_Update,
    Retirables,
    Transaction,
    Transaction_Request_Pending_Create,
    Transaction_Approved_Create,
    Transaction_Rejected_Create,
    Transaction_Generated_Create,
    Settings,
    Activity_Logs,
)
from app_201_pds.views import (
    Learning_Development_AJAXView,
)

from app_info_profile.views import (
    Profile_AJAXView,
    Profile_Retirables_AJAXView,
    Profile_Create_AJAXView,
    Profile_Update_AJAXView,
    Profile_Update_Save_AJAXView,
    Profile_Detail_Security_AJAXView,
)
from app_designation.views import (
    Designated_AJAXView,
    Contractual_AJAXView,
    Designated_Create_AJAXView,
    Designated_Create_Save_AJAXView,
    Designated_Delete_Save_AJAXView,
    Contractual_Create_AJAXView,
    Contractual_Delete_Save_AJAXView,
    Print_Contract_Contractual_Report,
)

from app_201_pds.views import (
    Print_SALN_Report,
    Print_Personal_Data_Sheet_Report,
)

from app_201_service_records.views import (
    Service_Record_AJAXView,
    Service_Record_Create_AJAXView,
    Service_Record_Create_Save_AJAXView,
    Service_Record_Update_AJAXView,
    Service_Record_Update_Save_AJAXView,
    Service_Record_Delete_Save_AJAXView,
    Service_Record_Print,
)

from app_rewards_recognitions.views import (
    Rewards_Recognitions_AJAXView,
    Rewards_Recognitions_Create_AJAXView,
    Rewards_Recognitions_Update_AJAXView,
    Rewards_Recognitions_Update_Save_AJAXView,
)

from app_transaction.views import (
    Transaction_Request_Pending_AJAXView,
    Transaction_Request_Pending_Create_AJAXView,
    Transaction_Approved_AJAXView,
    Transaction_Approved_Create_AJAXView,
    Transaction_Approved_Create_Save_AJAXView,
    Transaction_Rejected_AJAXView,
    Transaction_Rejected_Create_AJAXView,
    Transaction_Rejected_Create_Save_AJAXView,
    Transaction_Generated_AJAXView,
    Transaction_Generated_Profile_AJAXView,
    Transaction_Generated_Create_AJAXView,
    Transaction_Generated_Create_Save_AJAXView,
    Transaction_Batch_Generated_Create_Save_AJAXView,
)

from app_dtr.views import (
    Daily_Time_Records_Print,
    Daily_Time_Records_AJAXView,
)

from model_settings.views import Settings_AJAXView

import random
import string


urlpatterns = [
    path('', Dashboard.as_view(), name = 'dashboard'),
    path('api', Dashboard_Panels_AJAXView.as_view(), name = 'api_dashboard'),
    path('profile', Profile.as_view(), name = 'profile'),
    path('profile', Profile.as_view(), name = 'profile'),
    path('profile/print/personal-data-sheet/<int:pk>', Print_Personal_Data_Sheet_Report.as_view(), name = 'print_profile_personal_data_sheet'),
    path('profile/print/saln/<int:pk>', Print_SALN_Report.as_view(), name = 'print_profile_saln'),
    path('profile/information/<int:pk>', Profile_Detail.as_view(), name = 'profile_detail'),
    path('api/profile', Profile_AJAXView.as_view(), name = 'api_profile'),
    path('profile/create', Profile_Create.as_view(), name = 'profile_create'),
    path('profile/update/<int:pk>', Profile_Update.as_view(), name = 'profile_update'),
    path('profile/security/<int:pk>', Profile_Detail_Security.as_view(), name = 'profile_detail_security'),
    path('api/profile/security', Profile_Detail_Security_AJAXView.as_view(), name = 'api_profile_detail_security'),
    path('api/profile/learning-development/<int:pk>', Profile_Detail_Learning_Development_AJAXView.as_view(), name = 'api_profile_detail_learning_development'),
    path('profile/service-record/create/<int:pk>', Profile_Detail_Service_Create.as_view(), name = 'profile_detail_service_record_create'),
    path('api/profile/service-record/create', Service_Record_Create_AJAXView.as_view(), name = 'api_profile_detail_service_record_create'),
    path('api/profile/service-record/create/<int:pk>', Service_Record_Create_Save_AJAXView.as_view(), name = 'api_profile_detail_service_record_create_save'),
    path('profile/service-record/update/<int:pk>', Profile_Detail_Service_Update.as_view(), name = 'profile_detail_service_record_update'),
    path('api/profile/service-record/update', Service_Record_Update_AJAXView.as_view(), name = 'api_profile_detail_service_record_update'),
    path('api/profile/service-record/update/<int:pk>', Service_Record_Update_Save_AJAXView.as_view(), name = 'api_profile_detail_service_record_update_save'),
    path('api/profile/service-record/delete/<int:pk>', Service_Record_Delete_Save_AJAXView.as_view(), name = 'api_profile_detail_service_record_delete_save'),
    path('profile/service-record/update/<int:pk>', Profile_Detail_Service_Update.as_view(), name = 'profile_detail_service_record_update'),
    path('api/profile/create', Profile_Create_AJAXView.as_view(), name = 'api_profile_create'),
    path('api/profile/update', Profile_Update_AJAXView.as_view(), name = 'api_profile_update'),
    path('api/profile/update/save/<int:pk>', Profile_Update_Save_AJAXView.as_view(), name = 'api_profile_update_save'),
    path('api/profile/service-record', Service_Record_AJAXView.as_view(), name = 'api_profile_service_record'),
    path('service-record/print/<int:pk>', Service_Record_Print.as_view(), name = 'service_record_print'),
    path('designation', Designation.as_view(), name = 'designation'),
    path('contractual/print', Print_Contract_Contractual_Report.as_view(), name = 'print_contractual'),
    path('designation/designated/create/<int:pk>', Designation_Designated_Create.as_view(), name = 'designation_designated_create'),
    path('api/designation/designated/create', Designated_Create_AJAXView.as_view(), name = 'api_designation_designated_create'),
    path('api/designation/designated/create/save/<int:pk>', Designated_Create_Save_AJAXView.as_view(), name = 'api_designation_designated_create_save'),
    path('api/designation/designated/delete/save/<int:pk>', Designated_Delete_Save_AJAXView.as_view(), name = 'api_designation_designated_delete_save'),
    path('designation/contractual/create', Designation_Contractual_Create.as_view(), name = 'designation_contractual_create'),
    path('api/designation/contractual/create', Contractual_Create_AJAXView.as_view(), name = 'api_designation_contractual_create'),
    path('api/designation/contractual/create/save/<int:pk>', Contractual_Delete_Save_AJAXView.as_view(), name = 'api_designation_contractual_delete_save'),
    path('api/designated', Designated_AJAXView.as_view(), name = 'api_designated'),
    path('api/contractual', Contractual_AJAXView.as_view(), name = 'api_contractual'),
    path('learning-development', Learning_Development.as_view(), name = 'learning_development'),
    path('api/learning-development', Learning_Development_AJAXView.as_view(), name = 'api_learning_development'),
    path('rewards-recognitions', Rewards_Recognitions.as_view(), name = 'rewards_recognitions'),
    path('api/rewards-recognitions', Rewards_Recognitions_AJAXView.as_view(), name = 'api_rewards_recognitions'),
    path('rewards-recognitions/create', Rewards_Recognitions_Create.as_view(), name = 'rewards_recognitions_create'),
    path('api/rewards-recognitions/create', Rewards_Recognitions_Create_AJAXView.as_view(), name = 'api_rewards_recognitions_create'),
    path('rewards-recognitions/update/<int:pk>', Rewards_Recognitions_Update.as_view(), name = 'rewards_recognitions_update'),
    path('api/rewards-recognitions/update', Rewards_Recognitions_Update_AJAXView.as_view(), name = 'api_rewards_recognitions_update'),
    path('api/rewards-recognitions/update_save/<int:pk>', Rewards_Recognitions_Update_Save_AJAXView.as_view(), name = 'api_rewards_recognitions_update_save'),
    path('retirables', Retirables.as_view(), name = 'retirables'),
    path('api/retirables', Profile_Retirables_AJAXView.as_view(), name = 'api_retirables'),
    path('transaction', Transaction.as_view(), name = 'transaction'),
    path('transaction/request/create', Transaction_Request_Pending_Create.as_view(), name = 'transaction_request_pending_create'),
    path('api/transaction/request-pending', Transaction_Request_Pending_AJAXView.as_view(), name = 'api_transaction_request_pending'),
    path('api/transaction/request-pending/create', Transaction_Request_Pending_Create_AJAXView.as_view(), name = 'api_transaction_request_pending_create'),
    path('transaction/approved/create/<int:pk>', Transaction_Approved_Create.as_view(), name = 'transaction_approved_create'),
    path('api/transaction/approved', Transaction_Approved_AJAXView.as_view(), name = 'api_transaction_approved'),
    path('api/transaction/approved/create', Transaction_Approved_Create_AJAXView.as_view(), name = 'api_transaction_approved_create'),
    path('api/transaction/approved/create/save/<int:pk>', Transaction_Approved_Create_Save_AJAXView.as_view(), name = 'api_transaction_approved_create_save'),
    path('transaction/rejected/create/<int:pk>', Transaction_Rejected_Create.as_view(), name = 'transaction_rejected_create'),
    path('api/transaction/rejected', Transaction_Rejected_AJAXView.as_view(), name = 'api_transaction_rejected'),
    path('api/transaction/rejected/create', Transaction_Rejected_Create_AJAXView.as_view(), name = 'api_transaction_rejected_create'),
    path('api/transaction/rejected/create/save/<int:pk>', Transaction_Rejected_Create_Save_AJAXView.as_view(), name = 'api_transaction_rejected_create_save'),
    path('transaction/generated/create/', Transaction_Generated_Create.as_view(), name = 'transaction_generated_create'),
    path('api/transaction/generated', Transaction_Generated_AJAXView.as_view(), name = 'api_transaction_generated'),
    path('api/transaction/generated/profile', Transaction_Generated_Profile_AJAXView.as_view(), name = 'api_transaction_generated_profile'),
    path('api/transaction/generated/create', Transaction_Generated_Create_AJAXView.as_view(), name = 'api_transaction_generated_create'),
    path('api/transaction/generated/create/save', Transaction_Generated_Create_Save_AJAXView.as_view(), name = 'api_transaction_generated_create_save'),
    path('api/transaction/batch-generated/create/save', Transaction_Batch_Generated_Create_Save_AJAXView.as_view(), name = 'api_transaction_batch_generated_create_save'),
    path('settings', Settings.as_view(), name = 'settings'),
    path('api/settings', Settings_AJAXView.as_view(), name = 'api_settings'),
    path('activity-logs', Activity_Logs.as_view(), name = 'activity_logs'),
    path('dtr/print', Daily_Time_Records_Print.as_view(), name = 'dtr_print'),
    path('api/dtr/print', Daily_Time_Records_AJAXView.as_view(), name = 'api_dtr_print'),

    # path(str(random.randint(0000000000, 9999999999)) + '/activity-logs', Activity_Logs.as_view(), name = 'activity_logs'),
]
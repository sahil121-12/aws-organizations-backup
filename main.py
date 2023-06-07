from EnabledAccounts import acc_detail
from EnabledPolices import ai_policies,backup_policies,SCP_pol_detail,tag_policies
from EnabledServices import enable_service

enable_service.list_enabled_services()
acc_detail.get_account_details()

ai_policies.list_ai_policies()
backup_policies.list_backup_policies()
SCP_pol_detail.list_scp_policies()
tag_policies.list_tag_policies()



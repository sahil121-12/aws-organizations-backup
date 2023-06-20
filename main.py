from enabledAccounts import accountDetail
from enabledPolices import aiPolicies,backupPolicies,scpPolicies,tagPolicies,enabledPolicy
from enabledServices import enableService
from delegatedAdmin import delegatedAdmin

#This function call will retrieve all the enabled services in the aws organization
enableService.list_enabled_services()



#This function call will retrieve all the accounts details in the aws organization
accountDetail.get_account_details()


#This function call will retrieve all the enabled policy type  in the aws organization
enabledPolicy.get_enabled_policy_types()


delegatedAdmin.list_delegated_administrators()


#This function main is used to retrieve all the policy the list all the policies
def main():
 aiPolicies.list_ai_policies()
 backupPolicies.list_backup_policies()
 scpPolicies.list_scp_policies()
 tagPolicies.list_tag_policies()
main()


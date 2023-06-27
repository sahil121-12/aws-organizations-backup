# from enabledAccounts import accountDetail
# from enabledPolices import aiPolicies,backupPolicies,scpPolicies,tagPolicies,enabledPolicy
# from enabledServices import enableService
# from delegatedAdmin import delegatedAdmin

# #This function call will retrieve all the enabled services in the aws organization
# enableService.list_enabled_services()



# #This function call will retrieve all the accounts details in the aws organization
# accountDetail.get_account_details()


# #This function call will retrieve all the enabled policy type  in the aws organization
# enabledPolicy.get_enabled_policy_types()


# delegatedAdmin.list_delegated_administrators()


# #This function main is used to retrieve all the policy the list all the policies
# def main():
#  aiPolicies.list_ai_policies()
#  backupPolicies.list_backup_policies()
#  scpPolicies.list_scp_policies()
#  tagPolicies.list_tag_policies()
# main()



from enabledAccounts import accountDetail
from enabledPolices import aiPolicies,backupPolicies,scpPolicies,tagPolicies,enabledPolicy
from enabledServices import enableService
from delegatedAdmin import delegatedAdmin

import click

@click.command()
@click.option('-all', is_flag=True, help='Get all data')
@click.option('-p', is_flag=True, help='Only get Policy JSONs')
@click.option('-s', is_flag=True, help='Only get Service enabled JSONs')
@click.option('-a', is_flag=True, help='Only get account detail JSONs')
@click.option('-t', is_flag=True, help='Only get policy type enabled JSONs')
def main(all, p,s,a,t):
    if all:
        # Handle the case of getting all data
        click.echo('Getting all data...')
        

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

    
    elif s:
       click.echo('Getting Service enabled...')

        #This function call will retrieve all the enabled services in the aws organization
       enableService.list_enabled_services()


    elif a:
    
       click.echo('Getting account detail...')
       #This function call will retrieve all the accounts details in the aws organization
       accountDetail.get_account_details()



    
    elif t:
    
       click.echo('Getting policy type enabled...')
       #This function call will retrieve all the enabled policy type  in the aws organization
       enabledPolicy.get_enabled_policy_types()
     
 
               

    elif p:
        # Handle the case of getting Policy JSONs
        click.echo('Getting Policy JSONs...')
        # Your logic here to process Policy JSONs
        def main():
         aiPolicies.list_ai_policies()
         backupPolicies.list_backup_policies()
         scpPolicies.list_scp_policies()
         tagPolicies.list_tag_policies()
        main()

    else:
        # Handle the case of no option provided
        click.echo('No valid option specified. Please use -all or -p.')



main()
    

from enabledAccounts import accountDetail
from enabledPolices import aiPolicies, backupPolicies, scpPolicies, tagPolicies, enabledPolicy
from enabledServices import enableService
from delegatedAdmin import delegatedAdmin


import click

@click.command()
@click.option('--account', is_flag=True, help='Run the account module')
@click.option('--service', is_flag=True, help='Run the service module')
@click.option('--policytype', is_flag=True, help='Run the policy module')
@click.option('--delegated', is_flag=True, help='Run the delegated module')
@click.option('--policies', multiple=True, type=click.Choice(['scp', 'tag', 'backup', 'ai']), default=[], help='Run specific policy modules')

@click.option('--all', is_flag=True, help='Run the all module')




def run_modules(account, service,policytype,delegated,policies,all):
    if account:
        click.echo("Running account module")
        account_module_function()
    
    if service:
        click.echo("Running service module")
        service_module_function()
    if policytype:
        click.echo("Running policytype module")
        policytype_module_function()
    if delegated:
        click.echo("Running delegated module")
        delegatedadmin_module_function()
    


    if policies:
        click.echo("Running policy modules: {}".format(', '.join(policies)))
        for policy in policies:
            if policy == 'scp':
                click.echo("Running SCP policy module")
                scp_policies_module_function()
            elif policy == 'tag':
                click.echo("Running Tag policy module")
                tag_policies_module_function()
            elif policy == 'backup':
                click.echo("Running Backup policy module")
                backup_policies_module_function()
            elif policy == 'ai':
                click.echo("Running AI policy module")
                ai_policies_module_function()
            else:
                click.echo(f"Unknown policy module: {policy}")

    
    
    if all:
        click.echo("Running all  module")
        account_module_function()
        service_module_function()
        policytype_module_function()
        delegatedadmin_module_function()
        allpolicies_module_function()



def account_module_function():
    click.echo("This is the account module")
    accountDetail.get_account_details()

def service_module_function():
    click.echo("This is the service module")
    enableService.list_enabled_services()
    


def policytype_module_function():
    click.echo("This is the account module")
    enabledPolicy.get_enabled_policy_types()

def delegatedadmin_module_function():
    click.echo('Running delegatedadmin...')
    delegatedAdmin.list_delegated_administrators()

def allpolicies_module_function():
    click.echo('Running all policies...')
    def main():
         aiPolicies.list_ai_policies()
         backupPolicies.list_backup_policies()
         scpPolicies.list_scp_policies()
         tagPolicies.list_tag_policies()
    main()

def scp_policies_module_function():
    
    scpPolicies.list_scp_policies()


def tag_policies_module_function():
    
    tagPolicies.list_tag_policies()
def backup_policies_module_function():
    
    backupPolicies.list_backup_policies()

def ai_policies_module_function():
    
    aiPolicies.list_ai_policies()
    
run_modules()



import boto3
import json
import os

def get_account_details():
    client = boto3.client('organizations')

    organization_info = client.describe_organization()
    master_account_id = organization_info['Organization']['MasterAccountId']

    # Set the input parameters
    params = {
        'MaxResults': 10  # Update the MaxResults value to a lower value within the range
    }

    # Create a paginator for the list_accounts API
    paginator = client.get_paginator('list_accounts')
    page_iterator = paginator.paginate(**params)

    # Create a list to store the account details
    account_details = []

    # Iterate over the pages of results
    for page in page_iterator:
        # Iterate over the accounts and extract the details
        for account in page['Accounts']:
            account_id = account['Id']
            account_name = account['Name']
            account_email = account['Email']
            account_status = account['Status']
            account_joined_method = account['JoinedMethod']

            # Determine the account type
            account_type = ''
            if account_id == master_account_id:
                account_type = 'Master Account'
            elif account_joined_method == 'INVITED':
                account_type = 'Invited'
            elif account_joined_method == 'CREATED':
                account_type = 'Created'
            else:
                account_type = 'Unknown'

            # Create a dictionary for the account details
            account_info = {
                'Account ID': account_id,
                'Account Name': account_name,
                'Account Email': account_email,
                'Account Type': account_type
            }

            # Add the account details to the list
            account_details.append(account_info)

    # Find the output folder path
    current_directory = os.getcwd()
    output_folder = os.path.join(current_directory, 'output')

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Specify the output file path
    account_details_folder = os.path.join(output_folder, 'accountDetails')
    output_file = os.path.join(account_details_folder, 'account_details.json')

    # Create the Account details folder if it doesn't exist
    if not os.path.exists(account_details_folder):
        os.makedirs(account_details_folder)

    # Write the account details to a JSON file in the specified folder
    with open(output_file, 'w') as file:
        json.dump(account_details, file, indent=4)

    print("JSON file generated successfully with account details.")


import boto3
import json
import os

def list_delegated_administrators():
    # Create an Organizations client
    client = boto3.client('organizations')

    # Create a list to store the delegated administrators and their associated services
    delegated_admins = []
    

    # Paginator for list_delegated_administrators API
    paginator = client.get_paginator('list_delegated_administrators')

      # Set the pagination parameters
    pagination_config = {'MaxItems': 10}  
    page_iterator = paginator.paginate(PaginationConfig=pagination_config)

    # Iterate through each page of delegated administrators
    for page in page_iterator:
        admins = page['DelegatedAdministrators']

        # Iterate through each delegated administrator in the page
        for admin in admins:
            account_id = admin['Id']
            account_name = admin['Name']

            delegated_services_response = client.list_delegated_services_for_account(AccountId=account_id)

            # Extract the service names from the response
            service_names = [service['ServicePrincipal'] for service in delegated_services_response['DelegatedServices']]

            # Create a dictionary for the delegated administrator and associated services
            admin_data = {
                'Delegated Administrator Account ID': account_id,
                'Delegated Administrator Account Name': account_name,
                'Services': service_names
            }

            delegated_admins.append(admin_data)

    # Convert the data to JSON format
    json_data = json.dumps(delegated_admins, indent=4)

    # Specify the output file path
    output_folder = os.path.join('output', 'delegatedAdmin')
    file_path = os.path.join(output_folder, 'delegatedAdmin.json')

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save the JSON data to a file
    with open(file_path, 'w') as file:
        file.write(json_data)

    print("JSON file generated successfully with delegated administrators and their associated services.")



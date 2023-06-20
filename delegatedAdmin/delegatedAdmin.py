# import boto3

# def list_delegated_administrators():
#     # Create an Organizations client
#     client = boto3.client('organizations')

#     # List delegated administrators
#     response = client.list_delegated_administrators()

#     # Iterate through each delegated administrator
#     for admin in response['DelegatedAdministrators']:
#         account_id = admin['Id']
#         account_name = admin['Name']
        
#         if 'ServicePrincipal' in admin:
#             service_principal = admin['ServicePrincipal']
#             service_name = get_service_name(service_principal)
#         else:
#             service_name = "N/A"
        
#         # Print the delegated administrator and their associated service
#         print(f"Delegated Administrator Account ID: {account_id}")
#         print(f"Delegated Administrator Account Name: {account_name}")
#         print(f"Service: {service_name}")
#         print("")

# def get_service_name(service_principal):
#     # Extract the service name from the service principal
#     parts = service_principal.split('.')
#     service_name = parts[0].split('/')[-1]

#     return service_name

# # Call the function to list delegated administrators and their associated services
# list_delegated_administrators()

# import boto3

# def list_delegated_administrators(service_name):
#     # Create an Organizations client
#     client = boto3.client('organizations')

#     # List delegated administrators
#     response = client.list_delegated_administrators()

#     # Iterate through each delegated administrator
#     for admin in response['DelegatedAdministrators']:
#         account_id = admin['Id']
#         account_name = admin['Name']
        
#         if 'ServicePrincipal' in admin:
#             service_principal = admin['ServicePrincipal']
#             current_service_name = get_service_name(service_principal)
            
#             if current_service_name == service_name:
#                 # Print the delegated administrator for the specified service
#                 print(f"Delegated Administrator Account ID: {account_id}")
#                 print(f"Delegated Administrator Account Name: {account_name}")
#                 print(f"Service: {service_name}")
#                 print("")
        
#         else:
#             # Print the delegated administrator without service information
#             print(f"Delegated Administrator Account ID: {account_id}")
#             print(f"Delegated Administrator Account Name: {account_name}")
#             print("Service: N/A")
#             print("")

# def get_service_name(service_principal):
#     # Extract the service name from the service principal
#     parts = service_principal.split('.')
#     service_name = parts[0].split('/')[-1]

#     return service_name

# # Specify the service name to check for delegated administrators
# service_name = "guardduty"

# # Call the function to list delegated administrators for the specified service
# list_delegated_administrators(service_name)


# import boto3

# def list_delegated_administrators():
#     # Create an Organizations clientcd
    
#     client = boto3.client('organizations')

#     # List delegated administrators
#     response = client.list_delegated_administrators()

#     # Iterate through each delegated administrator
#     for admin in response['DelegatedAdministrators']:
#         account_id = admin['Id']
#         account_name = admin['Name']

       
#         delegated_services_response = client.list_delegated_services_for_account(AccountId=account_id)

#         # Extract the service names from the response
#         service_names = [service['ServicePrincipal'] for service in delegated_services_response['DelegatedServices']]

#         # Print the delegated administrator and associated services
#         print(f"Delegated Administrator Account ID: {account_id}")
#         print(f"Delegated Administrator Account Name: {account_name}")
#         print(f"Services: {', '.join(service_names)}")
#         print("")

# # Call the function to list delegated administrators and their associated services
# list_delegated_administrators()




# import boto3
# import json
# import os

# def list_delegated_administrators():
#     # Create an Organizations client
#     client = boto3.client('organizations')

#     # List delegated administrators
#     response = client.list_delegated_administrators()

#     # Create a list to store the delegated administrators and their associated services
#     delegated_admins = []

#     # Iterate through each delegated administrator
#     for admin in response['DelegatedAdministrators']:
#         account_id = admin['Id']
#         account_name = admin['Name']

#         delegated_services_response = client.list_delegated_services_for_account(AccountId=account_id)

#         # Extract the service names from the response
#         service_names = [service['ServicePrincipal'] for service in delegated_services_response['DelegatedServices']]

#         # Create a dictionary for the delegated administrator and associated services
#         admin_data = {
#             'Delegated Administrator Account ID': account_id,
#             'Delegated Administrator Account Name': account_name,
#             'Services': service_names
#         }

#         delegated_admins.append(admin_data)
#     current_directory = os.getcwd()
#     output_folder = os.path.join(current_directory, 'output')

#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)


#     # Convert the data to JSON format
#     json_data = json.dumps(delegated_admins, indent=4)

#     # Specify the output folder path
#     output_folder = os.path.join('output', 'delegatedAdminOutput')
#     file_path = os.path.join(output_folder, 'delegatedAdmin.json')

#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Save the JSON data to a file
    
#     with open(file_path, 'w') as file:
#         file.write(json_data)

#     print("JSON file generated successfully with delegated administrators and their associated services.")

# # Call the function to list delegated administrators and their associated services
# list_delegated_administrators()


# import boto3
# import json
# import os

# def list_delegated_administrators():
#     # Create an Organizations client
#     client = boto3.client('organizations')

#     # List delegated administrators
#     response = client.list_delegated_administrators()

#     # Create a list to store the delegated administrators and their associated services
#     delegated_admins = []

#     # Iterate through each delegated administrator
#     for admin in response['DelegatedAdministrators']:
#         account_id = admin['Id']
#         account_name = admin['Name']

#         delegated_services_response = client.list_delegated_services_for_account(AccountId=account_id)

#         # Extract the service names from the response
#         service_names = [service['ServicePrincipal'] for service in delegated_services_response['DelegatedServices']]

#         # Create a dictionary for the delegated administrator and associated services
#         admin_data = {
#             'Delegated Administrator Account ID': account_id,
#             'Delegated Administrator Account Name': account_name,
#             'Services': service_names
#         }

#         delegated_admins.append(admin_data)

#     # Convert the data to JSON format
#     json_data = json.dumps(delegated_admins, indent=4)

#     # Specify the output file path
#     output_folder = os.path.join('output', 'delegatedAdmin')
#     file_path = os.path.join(output_folder, 'delegatedAdmin.json')

#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Save the JSON data to a file
#     with open(file_path, 'w') as file:
#         file.write(json_data)

#     print("JSON file generated successfully with delegated administrators and their associated services.")


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



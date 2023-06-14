# import boto3
# import json
# import os

# def get_enabled_policy_types():
#     # Create an Organizations client
#     client = boto3.client('organizations')

#     # Create a paginator for listing roots
#     paginator = client.get_paginator('list_roots')

#     # Set the pagination parameters
#     pagination_config = {'MaxItems': 1}  # Update the MaxItems value as desired

#     # Retrieve the list of roots
#     response_iterator = paginator.paginate(PaginationConfig=pagination_config)

#     # Create a dictionary to store enabled policy types
#     enabled_policy_types = {}

#     # Iterate over the pages of roots
#     for response in response_iterator:
#         roots = response['Roots']
#         for root in roots:
#             policy_types = root['PolicyTypes']
#             for policy_type in policy_types:
#                 policy_type_name = policy_type['Type']
#                 policy_type_status = policy_type['Status']

#                 if policy_type_status == 'ENABLED':
#                     enabled_policy_types[policy_type_name] = 'enabled'

#     # Convert the output to JSON format
#     output = json.dumps(enabled_policy_types, indent=4)

#     # Specify the output folder path
#     current_directory = os.getcwd()
#     output_folder = os.path.join(current_directory, 'output', 'enabledPolicies')

#     # Create the output folder if it doesn't exist
#     os.makedirs(output_folder, exist_ok=True)

#     # Save the output to a JSON file in the output folder
#     file_path = os.path.join(output_folder, 'enabled_policy_types.json')

#     with open(file_path, 'w') as file:
#         file.write(output)

# # Call the function to get enabled policy types and save the output in a JSON file
   

import boto3
import json
import os
import csv

def get_enabled_policy_types():
    # Create an Organizations client
    client = boto3.client('organizations')

    # Create a paginator for listing roots
    paginator = client.get_paginator('list_roots')

    # Set the pagination parameters
    pagination_config = {'MaxItems': 10}  # Update the MaxItems value as desired

    # Retrieve the list of roots
    response_iterator = paginator.paginate(PaginationConfig=pagination_config)

    # Create a dictionary to store enabled policy types
    enabled_policy_types = {}

    # Iterate over the pages of roots
    for response in response_iterator:
        roots = response['Roots']
        for root in roots:
            policy_types = root['PolicyTypes']
            for policy_type in policy_types:
                policy_type_name = policy_type['Type']
                policy_type_status = policy_type['Status']

                if policy_type_status == 'ENABLED':
                    enabled_policy_types[policy_type_name] = 'enabled'

    # Convert the output to JSON format
    output = json.dumps(enabled_policy_types, indent=4)

    # Specify the output folder path
    current_directory = os.getcwd()
    output_folder = os.path.join(current_directory, 'output', 'enabledPolicies')

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Save the output to a JSON file in the output folder
    json_file_path = os.path.join(output_folder, 'enabled_policy_types.json')
    with open(json_file_path, 'w') as file:
        file.write(output)

    print("JSON file generated successfully with enabled policy types.")

    # Convert JSON to CSV
    csv_file_path = os.path.join(output_folder, 'enabled_policy_types.csv')
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    csv_data = []
    header = ["Policy Type", "Status"]
    csv_data.append(header)

    for key, value in data.items():
        row = [key, value]
        csv_data.append(row)

    with open(csv_file_path, 'w', newline='\n') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_data)

    print("CSV file generated successfully from JSON.")







import boto3
import json
import os
from datetime import datetime

def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

def list_enabled_services():
    org_client = boto3.client('organizations')

    # Create a paginator for the ListAWSServiceAccessForOrganization API
    paginator = org_client.get_paginator('list_aws_service_access_for_organization')
    page_iterator = paginator.paginate()

    # Create a list to store the enabled service objects
    service_objects = []

    # Iterate over the pages of results
    for page in page_iterator:
        # Extract the enabled services and their details from the page
        enabled_services = page['EnabledServicePrincipals']

        # Populate the list with the service objects
        for service in enabled_services:
            service_principal = service['ServicePrincipal'].split(".")[0]
            date_enabled = service['DateEnabled']
            service_object = {
                'ServicePrincipal': service_principal,
                'DateEnabled': date_enabled
            }
            service_objects.append(service_object)

    # Create a dictionary with the list of service objects
    data = {
        'EnabledServices': service_objects
    }

    # Convert datetime objects to string representation
    data_serialized = json.dumps(data, indent=4, default=serialize_datetime)

    # Find the output folder path
    current_directory = os.getcwd()
    output_folder = None
    for root, dirs, files in os.walk(current_directory):
        if 'output' in dirs:
            output_folder = os.path.join(root, 'output')
            break

    # Create the output folder if it doesn't exist
    if output_folder is None:
        raise Exception("Output folder not found.")

    # Specify the output file path
    service_enabled_folder = os.path.join(output_folder, 'serviceEnabled')
    output_file = os.path.join(service_enabled_folder, 'enabled_services.json')

    # Create the Service_enabled folder if it doesn't exist
    if not os.path.exists(service_enabled_folder):
        os.makedirs(service_enabled_folder)

    # Write the enabled services to a JSON file in the specified folder
    with open(output_file, 'w') as file:
        file.write(data_serialized)

    print("JSON file generated successfully with enabled services.")


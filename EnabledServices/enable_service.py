# import boto3
# import json

# def list_enabled_services():
#     org_client = boto3.client('organizations')

#     # Call the ListAWSServiceAccessForOrganization API to retrieve the enabled services
#     list_services_output = org_client.list_aws_service_access_for_organization()

#     # Extract the enabled services from the response
#     enabled_services = list_services_output['EnabledServicePrincipals']

#     # Create a list to store the enabled services
#     enabled_service_list = []

#     # Iterate over the enabled services and extract the service principal
#     for service in enabled_services:
#         service_principal = service['ServicePrincipal']
#         enabled_service_list.append(service_principal)

#     # Write the enabled services to a JSON file
#     with open('enabled_services.json', 'w') as file:
        
#         json.dump(enabled_service_list, file, indent=4)

#     print("JSON file generated successfully with enabled services.")



# list_enabled_services()

# import boto3
# import json
# from datetime import datetime

# def serialize_datetime(obj):
#     if isinstance(obj, datetime):
#         return obj.isoformat()
#     raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

# def list_enabled_services():
#     org_client = boto3.client('organizations')

#     # Call the ListAWSServiceAccessForOrganization API to retrieve the enabled services
#     list_services_output = org_client.list_aws_service_access_for_organization()

#     # Extract the enabled services from the response
#     enabled_services = list_services_output['EnabledServicePrincipals']

#     # Create a dictionary to store the enabled services
#     data = {
#         'EnabledServices': enabled_services
#     }

#     # Convert datetime objects to string representation
#     data_serialized = json.dumps(data, indent=4, default=serialize_datetime)

#     # Write the enabled services to a JSON file
#     with open('enabled_services.json', 'w') as file:
#         file.write(data_serialized)

#     print("JSON file generated successfully with enabled services.")



import boto3
import json
from datetime import datetime

def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

def list_enabled_services():
    org_client = boto3.client('organizations')

    # Call the ListAWSServiceAccessForOrganization API to retrieve the enabled services
    list_services_output = org_client.list_aws_service_access_for_organization()

    # Extract the enabled services from the response
    enabled_services = list_services_output['EnabledServicePrincipals']

    # Create a dictionary to store the enabled services
    data = {
        'EnabledServices': enabled_services
    }

    # Convert datetime objects to string representation
    data_serialized = json.dumps(data, indent=4, default=serialize_datetime)

    # Specify the path to the output folder and file name
    output_folder = '/home/sahil/Documents/All_detail/output/Service_enabled'
    output_file = f'{output_folder}/enabled_services.json'

    # Write the enabled services to a JSON file in the specified folder
    with open(output_file, 'w') as file:
        file.write(data_serialized)

    print("JSON file generated successfully with enabled services.")

import boto3
import json
import os

def get_enabled_policy_types():
    # Create an Organizations client
    client = boto3.client('organizations')

    # List the roots
    response = client.list_roots()

    # Get the policy types
    policy_types = response['Roots'][0]['PolicyTypes']

    # Create a dictionary to store enabled policy types
    enabled_policy_types = {}

    # Iterate over the policy types
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
    file_path = os.path.join(output_folder, 'enabled_policy_types.json')

    with open(file_path, 'w') as file:
        file.write(output)

# Call the function to get enabled policy types and save the output in a JSON file


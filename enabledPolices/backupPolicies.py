import boto3
import json
import os

def list_backup_policies():
    # Create a Boto3 client for AWS Organizations
    client = boto3.client('organizations')

    # Create a paginator for listing policies
    paginator = client.get_paginator('list_policies')

    # Set the pagination parameters
    pagination_config = {'MaxItems': 10}  # Update the MaxItems value as desired

    # Retrieve the list of backup policies
    response_iterator = paginator.paginate(Filter='BACKUP_POLICY', PaginationConfig=pagination_config)

    # Find the output folder path
    current_directory = os.getcwd()
    output_folder = os.path.join(current_directory, 'output', 'Policies', 'backupPolicies')

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the details of each backup policy
    for response in response_iterator:
        backup_policies = response['Policies']
        for backup_policy in backup_policies:
            policy_id = backup_policy['Id']
            policy_name = backup_policy['Name']

            # Retrieve the policy content
            policy_response = client.describe_policy(PolicyId=policy_id)
            policy_content_str = policy_response['Policy']['Content']

            # Create a separate JSON file for each backup policy in the output folder
            policy_file_name = os.path.join(output_folder, f"{policy_name}.json")

            # Load the policy content as JSON to format it
            policy_content = json.loads(policy_content_str)

            # Write the formatted policy content to the JSON file
            with open(policy_file_name, 'w') as file:
                json.dump(policy_content, file, indent=4)

            print(f"JSON file generated for policy '{policy_name}'.")


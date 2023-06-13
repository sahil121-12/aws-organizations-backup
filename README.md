# AWS Organization Dependency

## Problem Statement

This project aims to solve the following problem:

The project aims to provide a comprehensive solution for managing AWS Organization dependencies, such as retrieving account details, listing and retrieving policy information, and enabling specific AWS services. By leveraging the provided scripts and directories, users can gain insights into their organization's configuration and take necessary actions based on the collected information.

## Permissions Required (Json Policy)



To successfully execute the scripts and access the necessary resources, the following AWS Identity and Access Management (IAM) permissions should be assigned to the user or role executing the project:

    organizations:ListAccounts - Required to retrieve the list of enabled AWS accounts within the organization.
    organizations:DescribeAccount - Needed to fetch detailed information about individual AWS accounts.
    organizations:ListPolicies - Required to list the various types of policies within the organization.
    organizations:DescribePolicy - Needed to retrieve the content and details of specific policies.
    organizations:EnableAWSServiceAccess - Required to enable specific AWS services within the organization.
    Additional permissions may be necessary depending on the specific actions performed by the scripts.

Ensure that the user or role executing the scripts has the appropriate permissions assigned to successfully interact with the AWS Organizations service and access the required resources.



## Getting Started

To use this project, follow these steps:

1. Clone the repository to your local machine.
```bash
git clone https://github.com/sahil1202-12/aws-org-dependency-analyzer
```
2. Install the required dependencies listed in `requirement.txt`.
            
```bash
pip3 install -r requirement.txt
```
3. Make sure you run the above command before running the `main.py`.
4. Modify the scripts or add new functionality as needed.
5. Execute `main.py` to run the project.
6. Check the output files in the `output` directory for the generated results.

Feel free to explore each directory and file for more detailed information about their respective contents and functionalities.


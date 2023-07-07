# AWS Organizations Backup

## Introduction

AWS Organizations is a service provided by Amazon Web Services (AWS) that allows you to centrally manage and govern multiple AWS accounts. It provides a way to organize your accounts into a hierarchical structure and apply policies across the organization.

 #### About AWS Organizations Backup

 


AWS Organizations Backup is a tool designed to capture and backup important details of your AWS accounts. It allows you to retrieve and store information such as:

- Retrieve account details.
- Enable services.
- Manage policies.
- Delegate administrative access.


  
## Permissions Required 

To successfully execute the scripts and access the necessary resources, the following AWS Identity and Access Management (IAM) permissions should be assigned to the user or role executing the project:

Ensure that the user or role executing the scripts has the appropriate permissions assigned to successfully interact with the AWS Organizations service and access the required resources.

You have two options for granting the necessary permissions:
1. Grant the user or role the built-in AWS managed policy called "AWSOrganizationsReadOnlyAccess."
2. Create a custom IAM policy with the required permissions mentioned above.

If you choose to create a custom IAM policy, you can use the following JSON policy document as a reference:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "organizations:DescribeOrganization",
                "organizations:ListAccounts",
                "organizations:ListAWSServiceAccessForOrganization",
                "organizations:ListRoots",
                "organizations:DescribePolicyType",
                "organizations:ListPolicies",
                "organizations:DescribePolicy",
                "organizations:ListTargetsForPolicy",
                "organizations:ListDelegatedAdministrators",
                "organizations:ListDelegatedServicesForAccount"
            ],
            "Resource": "*"
        }
    ]
}

```









## Getting Started


Check out the following GIF to see the complete procedure of getting AWS Organizations Backup. 


![GIF](https://github.com/sahil121-12/aws-organizations-backup/blob/integration/File1.gif)


To use this project, follow these steps:

1. Clone the repository to your local machine.
```bash
git clone https://github.com/sahil121-12/aws-organizations-backup
cd aws-organizations-backup
```
2. Install the required dependencies listed in `requirement.txt`.
            
```bash
pip3 install -r requirement.txt
```

3. Execute `main.py` to run the project.Choose one of the following options:
    - To retrieve all details:
    ```bash
         python3 main.py --all 
    ```
    - To retrieve account details:
    ```bash
         python3 main.py --account
    ```
     - To retrieve enabled services:
    ```bash
         python3 main.py --service
    ```
     - To retrieve policy type enabled :
    ```bash
         python3 main.py --policytype
    ```
     - To retrieve policies like SCP, AI, backup, and tag:
      ```bash
         python3 main.py --policies scp
    ```
      
     - To retrieve delegated admin details :
    ```bash
         python3 main.py --delegated
    ```
Note: You can use multiple arguments for the --policies option, separated by commas. For example:
    python3 main.py --policies scp,ai

5. Check the output files in the `output` directory for the generated results.




# AWS Organization Dependency
## Overview 
: By using this reposi

- **enabledAccounts**: Contains the code related to retrieving details of enabled accounts.
    - accountDetail.py: Python script for retrieving account details.

- **enabledPolicies**: Contains the code related to different types of enabled policies.
    - aiPolicies.py: Python script for retrieving AI policies.
    - backupPolicies.py: Python script for retrieving backup policies.
    - enabledPolicy.py: Python script for retrieving enabled policy types.
    - scpPolicies.py: Python script for retrieving SCP policies.
    - tagPolicies.py: Python script for retrieving tag policies.

- **enabledServices**: Contains the code related to enabling services.
    - enableService.py: Python script for enabling services.

- **output**: Contains the output files generated by the scripts.
    - accountDetails: Folder for storing account details.
    - enabledPolicies: Folder for storing enabled policies.
    - Policies: Folder for storing policy-specific output files.
        - aiPolicies: Folder for storing AI policy files.
        - backupPolicies: Folder for storing backup policy files.
        - scpPolicies: Folder for storing SCP policy files.
        - tagPolicies: Folder for storing tag policy files.
    - serviceEnabled: Folder for storing service-enabled files.

- **main.py**: The main Python script that executes the main logic of the project.

- **requirement.txt**: File listing the required Python packages and their versions.

## Getting Started

To use this project, follow these steps:

1. Clone the repository to your local machine.
```bash
git clone https://github.com/sahil1202-12/aws-org-dependency-analyzer
```
3. Install the required dependencies listed in `requirement.txt`.
4.   Make sure you run this command before running the `main.py`.
            
```bash
pip3 install -r requirement.txt
```

5. Modify the scripts or add new functionality as needed.
6. Execute `main.py` to run the project.
7. Check the output files in the `output` directory for the generated results.

Feel free to explore each directory and file for more detailed information about their respective contents and functionalities.


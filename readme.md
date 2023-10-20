# AWS CloudFormation Resource Checker

## Overview

The AWS CloudFormation Resource Checker is a Python script that allows you to interactively select an AWS region, retrieve information about CloudFormation stacks and their associated resources in that region, and then compare these resources with global AWS resources in the selected region.

This script is useful for users who want to:

- Understand and manage resources created by CloudFormation in a specific AWS region.
- Identify resources that may not be managed by CloudFormation.

The program uses the Boto3 library to interact with AWS services and the `tqdm` library to display a progress bar for better user experience.

## Prerequisites

Before using this script, make sure you have the following:

- Python 3.x installed
- AWS CLI configured with the necessary credentials
- The Boto3 library installed 
- The tqdm library installed
- you can install the required packages using:  (`pip install -r requirements.txt`)

## How to Use

1. Clone or download the repository to your local machine.

2. Open a terminal and navigate to the directory where the script is located.

3. Run the script by executing the following command: 
- `pithon cf-resources-check.py`

4. You will be prompted to select an AWS region from a list of available regions. Enter the number corresponding to your desired region.

5. The script will retrieve information about CloudFormation stacks and their associated resources in the selected region and display a progress bar using `tqdm`.

6. After processing is complete, the script will create a JSON file that lists the CloudFormation-managed resources by type, and the results will be written to a file with the format: `<account_id>_resources_<selected_region>.json`.

## Example Output

Here's an example of the output JSON file format:
```json
{
 "AWS::EC2::Instance": ["i-1234567890abcdef0", "i-0987654321fedcba0"],
 "AWS::S3::Bucket": ["my-bucket", "another-bucket"]
}

License
This project is licensed under the MIT License. See the LICENSE file for details.

Feedback and Contributions
We welcome feedback, bug reports, and contributions from the community. Feel free to open issues and pull requests on the project's GitHub repository.

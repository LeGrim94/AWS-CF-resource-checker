import boto3
import json
from tqdm import tqdm  # Import tqdm

# Get the AWS account name
sts_client = boto3.client('sts')
account_id = sts_client.get_caller_identity()['Account']

# Get the list of AWS account-enabled regions
session = boto3.session.Session()
available_regions = session.get_available_regions('cloudformation')

# Show the user the list of available regions and let them choose one
print("List of available regions:")
for i, region in enumerate(available_regions, 1):
    print(f"{i}. {region}")

region_index = int(input("Select the number corresponding to the desired region: ")) - 1

if region_index < 0 or region_index >= len(available_regions):
    print("Invalid selection.")
    exit(1)

selected_region = available_regions[region_index]
print(f"You have selected the region: {selected_region}")

# Initialize the CloudFormation client for the selected region
cf_client = boto3.client('cloudformation', region_name=selected_region)

# Check if there are any stacks in the selected region
stacks = cf_client.list_stacks(StackStatusFilter=['CREATE_COMPLETE', 'UPDATE_COMPLETE'])
if not stacks['StackSummaries']:
    print("No stacks found in the selected region.")
    exit(0)

# Initialize the dictionary to group resources by type
resource_groups = {}

# Use tqdm to monitor progress
total_stacks = len(stacks['StackSummaries'])
for stack in tqdm(stacks['StackSummaries'], desc="Processing stacks", ascii=True):
    stack_name = stack['StackName']
    # Get the resources associated with each stack
    resources = cf_client.list_stack_resources(StackName=stack_name)
    
    # Iterate through all the resources in the stack
    for resource in resources['StackResourceSummaries']:
        resource_type = resource['ResourceType']
        resource_id = resource['PhysicalResourceId']
        
        # Add the resource to the dictionary grouped by type
        if resource_type in resource_groups:
            resource_groups[resource_type].append(resource_id)
        else:
            resource_groups[resource_type] = [resource_id]

# Check if there are any resources in the selected region
if not resource_groups:
    print("No resources found in the selected region.")
    exit(0)

# JSON file name with the account name included
output_file_name = f"{account_id}_resources_{selected_region}.json"

# Write the result to a JSON file with the account name included
with open(output_file_name, 'w') as json_file:
    json.dump(resource_groups, json_file, indent=4)

print(f"The results have been written to the file: {output_file_name}")

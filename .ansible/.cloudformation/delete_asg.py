import boto3, os
from time import sleep

client = boto3.client('autoscaling', region_name=os.getenv('AWS_REGION'))

responses = client.describe_auto_scaling_groups()
for response in responses['AutoScalingGroups']:
    for tag in response['Tags']:
        if tag['Value'] == 'Green':
            green_asg_arn = response['AutoScalingGroupName']

response = client.delete_auto_scaling_group(
    AutoScalingGroupName=green_asg_arn,
    ForceDelete=True
)

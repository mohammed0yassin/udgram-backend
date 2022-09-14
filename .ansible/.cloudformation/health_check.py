import boto3, os, sys
from time import sleep
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
client = boto3.client('autoscaling', region_name=os.getenv('AWS_REGION'))
HEALTHY = 'Healthy'
all_good = ['Unhealthy']
NO = 0
sleep_cntr = 0
while len(all_good) != NO:
    responses = client.describe_auto_scaling_groups()
    for response in responses['AutoScalingGroups']:
        for tag in response['Tags']:
            if tag['Value'] == 'Blue':
                blue_asg = response
    instances = blue_asg['Instances']
    all_good = []
    for instance in instances:
        if instance['HealthStatus'] != HEALTHY:
            all_good.append("Unhealthy")

    logging.info("Some instances are still Unhealthy...")
    sleep(10)
    sleep_cntr+=1
    if sleep_cntr >= 30:
        logging.error("FAILED: Took too long to be Healty")
        exit(1)

logging.info("SUCCESS: All instances are Healthy")
exit(0)
    
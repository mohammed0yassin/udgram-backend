import boto3
from time import sleep

client = boto3.client('autoscaling')
HEALTHY = 'Healthy'
all_good = []
YES = 0
sleep_cntr = 0
while len(all_good) == YES:
    responses = client.describe_auto_scaling_groups()
    for response in responses['AutoScalingGroups']:
        for tag in response['Tags']:
            if tag['Value'] == 'Blue':
                blue_asg = response
    
    instances = blue_asg['Instances']
    print(instances)
    all_good = []
    for instance in instances:
        if instance['HealthStatus'] != HEALTHY:
            all_good.append("Unhealthy")

    print("Some instances are still Unhealthy...")
    sleep(10)
    sleep_cntr+=1
    if sleep_cntr >= 10:
        print("FAILED: Took too long to be Healty")
        exit(1)

print("SUCCESS: All instances are Healthy")
exit(0)
    
import boto3
from datetime import datetime

aws_console = boto3.session.Session(profile_name="sanya")
ec2_console = aws_console.client('ec2',region_name="eu-north-1")


def createInstance():

    response = ec2_console.run_instances(
        ImageId='ami-0fe8bec493a81c7da',
        InstanceType='t3.micro',
        MaxCount= 1,
        MinCount=1
    )

    return response


def terminateInstance():
    response = ec2_console.stop_instances(
        InstanceIds=['i-00cc4599abb373468']
    )
    return response

def startInstance():

    response = ec2_console.start_instances(
            InstanceIds=['i-00cc4599abb373468']
        )
    print("Instance started running")
    return response

def upTime():
    instance_id = 'i-00cc4599abb373468'
    response = ec2_console.describe_instances(InstanceIds=[instance_id])
    launch_time = response['Reservations'][0]['Instances'][0]['LaunchTime']
    current_time = datetime.now(launch_time.tzinfo)
    uptime = current_time - launch_time
    print(f"The instance {instance_id} has been running for {uptime}")

def checkStatus(instance_id):

    response = ec2_console.describe_instances(InstanceIds=[instance_id])
    instance_state = response['Reservations'][0]['Instances'][0]['State']['Name']

    print(f"The instance {instance_id} is in the '{instance_state}' state.")

    if instance_state == 'stopped':
        startInstance()


# startInstance()
# upTime()
# terminateInstance()
checkStatus('i-00cc4599abb373468')
import datetime as dt
import boto3
from scheduler import Scheduler
client = boto3.client('ec2')
instances = client.describe_instance_status()

def check_instances_status():
    for instance in instances["InstanceStatuses"]:
        instance_id = instance["InstanceState"]["InstanceId"]
        state = instance["InstanceState"]["Name"]
        instance_status = instance["InstanceState"]["InstanceStatus"]["Status"]
        system_status = instance["InstanceState"]["SystemStatus"]["Status"]
        print(f"The {instance_id} is {state} and his status are {instance_status} and {system_status} ")
        print("#######################################################")



schedule = Scheduler()

schedule.minutely(dt.time(second=5),check_instances_status)

while True:
    schedule.exec_jobs()
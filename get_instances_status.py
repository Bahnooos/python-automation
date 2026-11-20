import boto3

client = boto3.client('ec2')
instances = client.describe_instance_status()

for instance in instances["InstanceStatuses"]:
    instance_id = instance["InstanceState"]["InstanceId"]
    state = instance["InstanceState"]["Name"]
    instance_status = instance["InstanceState"]["InstanceStatus"]["Status"]
    system_status = instance["InstanceState"]["SystemStatus"]["Status"]
    print(f"The {instance_id} is {state} and his status are {instance_status} and {system_status} ")


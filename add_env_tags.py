import boto3

client = boto3.client("ec2", region_name="eu-north-1")
ec2 = boto3.resource("ec2", region_name="eu-north-1")

# جلب كل السيرفرات (Running & Stopped)
reservations = client.describe_instances()["Reservations"]


def add_tags_to_instances(reservations_list):
    ec2_ids = []
    for reservation in reservations_list:
        for instance in reservation["Instances"]:
            ec2_ids.append(instance["InstanceId"])

    if not ec2_ids:
        print("No EC2 instances found in eu-north-1.")
        return

    response = ec2.create_tags(
        Resources=ec2_ids,
        Tags=[
            {
                "Key": "environment",
                "Value": "dev",
            },
        ],
    )
    print(f"Tagged instances: {ec2_ids}")
    return response


add_tags_to_instances(reservations)
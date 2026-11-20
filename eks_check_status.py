import boto3
from scheduler import Scheduler
import datetime as dt


client = boto3.client('eks')

clusters = client.list_clusters()["clusters"]

def check_eks_status():
    for cluster in clusters:
        name = cluster["name"]
        endpoint = cluster["endpoint"]
        version = cluster["version"]
        status = cluster["status"]
        print(f"Cluster Name: {name} \nVersion: {version} \nEndpoint: {endpoint} \nStatus: {status}")
        print("##########################################")


schedule = Scheduler()

schedule.daily(dt.time(hour=5),check_eks_status)

while True:
    schedule.exec_jobs()
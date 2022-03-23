#!/usr/bin/python3.8

from pywebio.input import input, PASSWORD
from pywebio.output import put_text, popup, toast
import boto3
import botocore.exceptions
from pprint import pprint
import pywebio


def show_sg():
    #popup('popup title', 'popup text content')
    #toast('New message 🔔')
    k_id = input('What is your access key id?\n')
    s_key = input('What is your secret access key key?\n', type = PASSWORD)
    re_name = "us-east-1"
    try:
        client = boto3.client('ec2', region_name = re_name, aws_access_key_id = k_id, aws_secret_access_key = s_key)
        response = client.describe_network_interfaces()
        info_list = response['NetworkInterfaces']
        for n in info_list:
            put_text(f"Account: {n['Attachment']['InstanceOwnerId']}")
            put_text(f"Instance ID: {n['Attachment']['InstanceId']}")
            put_text(f"Availability Zone: {n['AvailabilityZone']}")
            put_text(f"Private IP: {n['PrivateIpAddress']}")
            put_text(f"VPC ID: {n['VpcId']}")
            new_list = n['Groups']
            for n1 in new_list:
                put_text(f"Security Group ID:{n1['GroupId']}")
            put_text('-'*50)
    except:
        popup('You did not enter valid credentials')



if __name__ == '__main__':
    pywebio.start_server(show_sg, port = 8080)

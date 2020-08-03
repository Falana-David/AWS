import boto3

def lambda_handler(event, context):
    client = boto3.client('ec2')
    response = client.modify_instance_attribute(InstanceId='i-028c12f8914597753',InstanceType={ 'Value': 'c4.large',},)
    print(response)

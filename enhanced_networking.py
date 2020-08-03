import boto3

def lambda_handler(event, context):
    client = boto3.client('ec2')
    response = client.modify_instance_attribute(
    EnaSupport={
        'Value': True,
    },
    InstanceId='i-097ae5c0d808c2fde',
)

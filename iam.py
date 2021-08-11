import boto3

iam = boto3.resource('iam')
user = iam.User('gangi')

import json
import boto3
def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('sns')
    response = client.subscribe(
    TopicArn='arn:aws:sns:ap-south-1:436342194478:subscribe',
    Protocol='email',
    Endpoint=event['email']
    )
    print(response)
    
    return {"message":"please confirm email subscription"}
import boto3
import json
from botocore.vendored import requests
def lambda_handler(event, context):
    url = "https://api.chucknorris.io/jokes/random"
    joke = requests.request("GET", url)
    
    joke = json.loads(joke.text)
    
    client = boto3.client('sns')
    response = client.publish(
    TopicArn='arn:aws:sns:ap-south-1:436342194478:subscribe',
    Message=joke['value'],
    Subject='Suscription Mail'
    )   
    print(response)
    return ("Mail Sent ")
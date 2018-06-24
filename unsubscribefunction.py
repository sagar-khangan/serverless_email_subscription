import boto3

def lambda_handler(event, context):
    client = boto3.client('sns')
    response = client.list_subscriptions_by_topic(
    TopicArn='arn:aws:sns:ap-south-1:436342194478:subscribe'
    )
    for i in response['Subscriptions']:
        if i['Endpoint'] == event['email']:
            unsub = client.unsubscribe(
            SubscriptionArn=i['SubscriptionArn']
            )
            print(unsub)
    
    return {"message":"unsubscribed"}
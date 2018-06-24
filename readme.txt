- api gateway having 2 resources for subscribe and unsubscribe
- post api with body {"email":"email@email.com"}
- 3 lambda functions 1 for subscrobe 1 for unsubscribe and 1 for sending mail daily.
- cloudwatch event to trigger lambda to send mail daily at 7 AM UTC
- sns topic to create subscription


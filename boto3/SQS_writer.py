import boto3
import uuid

session = boto3.Session(      aws_access_key_id="your-access-key",
							  aws_secret_access_key="your-secret-access-key"
							  aws_session_token="your-token")

	
sqs = session.resource("sqs")

queue2 = sqs.get_queue_by_name(QueueName="test_mdm_gateway_inbound_retry")
response = queue2.send_message(MessageBody='hello world from boto' + str(uuid.uuid1()))


# The response is NOT a resource, but gives you a message ID and MD5
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))

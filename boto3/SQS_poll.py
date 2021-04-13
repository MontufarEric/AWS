session = boto3.Session(      aws_access_key_id="your-access-key",
							  aws_secret_access_key="your-secret-access-key"
							  aws_session_token="your-token")

								
sqs = session.resource("sqs")
queue = sqs.get_queue_by_name(QueueName="mdm_gateway_source1")


messages = queue.receive_messages()
for message in messages:
    process_message(message.body)
#     message.delete()

message_content = json.loads((json.loads(message.body)['Message']))

print(json.dumps(message_content, indent=4))


# https://perandrestromhaug.com/posts/writing-an-sqs-consumer-in-python/
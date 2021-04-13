client = boto3.client('s3',
    aws_access_key_id="your-access-key",
    aws_secret_access_key="your-secret-access-key"
    aws_session_token="your-token")
	
	client.list_buckets()
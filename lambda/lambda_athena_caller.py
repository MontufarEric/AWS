import time
import boto3

query = "SELECT *  FROM myDatabase.MyTable"
DATABASE = 'MyDatabase'
Table = "MyTable"
output='s3://my-s3-bucket'


def lambda_handler(event, context):
    query = "SELECT *  FROM myDatabase.MyTable"
    client = boto3.client('athena')

    # Execution
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': DATABASE
        },
        ResultConfiguration={
            'OutputLocation': output,
        }
    )
    return response
    return
	
#	https://aws.amazon.com/premiumsupport/knowledge-center/schedule-query-athena/

# create role (athenaFull, CloudwatchFull, S3Full)
#create lambda and add trigger --> couldwatch cron
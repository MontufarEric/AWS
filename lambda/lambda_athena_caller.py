import time
import boto3

query = "SELECT *  FROM myDatabase.MyTable"
DATABASE = 'MyDatabase'
Table = "MyTable"
output='s3://my-s3-bucket'

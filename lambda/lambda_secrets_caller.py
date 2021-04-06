import json
import boto3
import base64
from botocore.exceptions import ClientError

secret_name = "your/secret/name"
region_name = "us-west-1"

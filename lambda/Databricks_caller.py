DOMAIN = <Databrciks_cluster>
TOKEN = <Databrciks_user_token>
JOB = <Databrciks_job_id>
response = requests.post( 
    'https://%s/api/2.0/jobs/run-now' % (DOMAIN), 
    headers={'Authorization': b"Basic " + base64.standard_b64encode(b"token:" + TOKEN)}, 
    json={ "job_id": JOB}
)
if response.status_code == 200: print(response.json())
else: print("Error launching cluster: %s" % (response.json()))

#https://databricks.com/blog/2016/10/11/using-aws-lambda-with-databricks-for-etl-automation-and-ml-model-serving.html?_ga=2.34112865.1767610906.1617235120-1531116094.1601927735
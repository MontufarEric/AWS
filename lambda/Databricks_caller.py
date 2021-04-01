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
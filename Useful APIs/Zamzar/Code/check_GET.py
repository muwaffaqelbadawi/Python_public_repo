import requests
from requests.auth import HTTPBasicAuth

job_id = 25
api_key = '470e306c2c5177ef072f1151cc210d81b1af8fd2'
endpoint = "https://sandbox.zamzar.com/v1/jobs/{}".format(job_id)

response = requests.get(endpoint, auth=HTTPBasicAuth(api_key, ''))

print(response.json())
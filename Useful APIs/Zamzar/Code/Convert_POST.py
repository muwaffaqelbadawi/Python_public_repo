import requests
from requests.auth import HTTPBasicAuth

api_key = '470e306c2c5177ef072f1151cc210d81b1af8fd2'
endpoint = "https://sandbox.zamzar.com/v1/jobs"
source_file = "../Source_Folder/Tom Taulli - The Robotic Process Automation Handbook_ A Guide to Implementing RPA Systems (2020, Apress) - libgen.li.azw3"
target_format = "pdf"

file_content = {'source_file': open(source_file, 'rb')}
data_content = {'target_format': target_format}
res = requests.post(endpoint, data=data_content, files=file_content, auth=HTTPBasicAuth(api_key, ''))

print(res.json())
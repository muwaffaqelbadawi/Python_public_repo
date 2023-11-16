import requests
from requests.auth import HTTPBasicAuth

file_id = 146835918
local_filename = '../[Matthew_Fradd]_The_Porn_Myth__Exposing_the_Realit(z-lib.org).pdf'
api_key = '470e306c2c5177ef072f1151cc210d81b1af8fd2'
endpoint = "https://sandbox.zamzar.com/v1/files/{}/content".format(file_id)

response = requests.get(endpoint, stream=True, auth=HTTPBasicAuth(api_key, ''))

try:
  with open(local_filename, 'wb') as f:
    for chunk in response.iter_content(chunk_size=1217656):
      if chunk:
        f.write(chunk)
        f.flush()

    print("File downloaded")

except IOError:
  print("Error")
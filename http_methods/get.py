# Libraries
import json
import requests
import connection as i
import sys  # access to the variables
import os
sys.path.append(os.getcwd())


def get_method(url):
    # request
    req = requests.get(url, auth=i.login, headers=i.header, verify=False)
    # response
    if req.status_code in [200, 201, 202, 204]:
        print(f"Successful. GET Method. Status code: {req.status_code}")
        res = req.json()
        print(json.dumps(res, indent=4))
    else:
        print(f"Error retrieving data. Status code: {req.status_code}")

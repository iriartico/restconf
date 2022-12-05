# Libraries
import json
import requests
import connection as i
import sys  # access to the variables
import os
sys.path.append(os.getcwd())


def delete_method(url):
    # request
    req = requests.delete(url, auth=i.login, headers=i.header, verify=False)
    # response
    if req.status_code in [200, 201, 202, 204]:
        print(f"Successful. DELETE Method. Status code: {req.status_code}")
    else:
        print(f"Error retrieving data. Status code: {req.status_code}")

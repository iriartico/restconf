# Libraries
import json
import requests
import basic_info as i
import sys  # access to the variables
sys.path.append(".")


def get_method(url):
    # request
    req = requests.delete(url, auth=i.login, headers=i.header, verify=False)
    # response
    if req.status_code in [200, 201, 202, 204]:
        print(f"Successful. DELETE Method. Status code: {req.status_code}")
    else:
        print(f"Error retrieving data. Status code: {req.status_code}")

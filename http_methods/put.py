# Libraries
import os
import requests
import sys  # access to the variables
sys.path.append(os.getcwd())
import connection as i


def put_method(url, yangConfig):
    # request
    req = requests.put(url, auth=i.login, headers=i.header,
                       data=yangConfig, verify=False)
    # response
    if req.status_code in [200, 201, 202, 204]:
        print(f"Successful. PUT Method. Status code: {req.status_code}")
    else:
        print(f"Error retrieving data. Status code: {req.status_code}")

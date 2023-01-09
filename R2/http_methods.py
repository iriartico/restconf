# Libraries
import json
import os
import requests
import sys
import connection as i
sys.path.append(os.getcwd())


def get(url):
    # request
    req = requests.get(url, auth=i.login, headers=i.header, verify=False)
    # response
    if req.status_code in [200, 201, 202, 204]:
        print(f"Successful. GET Method. Status code: {req.status_code}")
        res = req.json()
        print(json.dumps(res, indent=4))
    else:
        print(f"Error retrieving data. Status code: {req.status_code}")


def patch(url, yangConfig):
    # request
    req = requests.patch(url, auth=i.login, headers=i.header,
                         data=yangConfig, verify=False)
    # response
    if req.status_code in [200, 201, 202, 204]:
        print(f"Successful. PATCH Method. Status code: {req.status_code}")
    else:
        print(f"Error retrieving data. Status code: {req.status_code}")


def put(url, yangConfig):
    # request
    req = requests.put(url, auth=i.login, headers=i.header,
                       data=yangConfig, verify=False)
    # response
    if req.status_code in [200, 201, 202, 204]:
        print(f"Successful. PUT Method. Status code: {req.status_code}")
    else:
        print(f"Error retrieving data. Status code: {req.status_code}")


def delete(url):
    # request
    req = requests.delete(url, auth=i.login, headers=i.header, verify=False)
    # response
    if req.status_code in [200, 201, 202, 204]:
        print(f"Successful. DELETE Method. Status code: {req.status_code}")
    else:
        print(f"Error retrieving data. Status code: {req.status_code}")

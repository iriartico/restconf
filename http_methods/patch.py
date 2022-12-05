# Libraries
import connection as i
import requests
import sys  # access to the variables
import os
sys.path.append(os.getcwd())


def patch_method(url, yangConfig):
    # request
    req = requests.patch(url, auth=i.login, headers=i.header,
                         data=yangConfig, verify=False)
    # response
    if req.status_code in [200, 201, 202, 204]:
        print(f"Successful. PATCH Method. Status code: {req.status_code}")
    else:
        print(f"Error retrieving data. Status code: {req.status_code}")

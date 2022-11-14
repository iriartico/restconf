# Libraries
import sys
import os
sys.path.append(os.getcwd())
import get_method as get
import delete_method as delete
import basic_info as i

url = f"https://{i.server}/{i.rest_path}/data/ietf-interfaces:interfaces/interface=Loopback1"
print(url)

delete.delete_method
get.get_method(url)

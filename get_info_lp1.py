# Libraries
import sys
import os
sys.path.append(os.getcwd())
import get_method as get
import basic_info as i

url = f"https://{i.server}/{i.rest_path}/data/ietf-interfaces:interfaces/interface=Loopback1"
print(url)

get.get_method(url)

# Libraries
import sys
import os
sys.path.append(os.getcwd())
import http_methods.get as get
import http_methods.connection as i

url = f"https://{i.server}/{i.rest_path}/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"
print(url)

get.get_method(url)

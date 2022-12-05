# Libraries
import sys
import os
sys.path.append(os.getcwd())
import http_methods.get as get
import http_methods.delete as delete
import http_methods.connection as i

url = f"https://{i.server}/{i.rest_path}/data/ietf-interfaces:interfaces/interface=Loopback1"
print(url)

delete.delete_method
get.get_method(url)

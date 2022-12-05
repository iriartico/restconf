# Libraries
import sys
import os
sys.path.append(os.getcwd())
import http_methods.connection as i
import http_methods.get as get

url = f"https://{i.server}/{i.rest_path}/data/ietf-routing:routing-state"
print(url)

get.get_method(url)

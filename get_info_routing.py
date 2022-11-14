# Libraries
import sys
import os
sys.path.append(os.getcwd())
import basic_info as i
import get_method as get

url = f"https://{i.server}/{i.rest_path}/data/ietf-routing:routing-state"
print(url)

get.get_method(url)

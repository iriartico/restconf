# Libraries
import sys
import os
sys.path.append(os.getcwd())
from http_methods import get
from http_methods import delete
import connection as i

url = f"https://{i.server}/{i.rest_path}/data/ietf-interfaces:interfaces/interface=Loopback1"
print(url)

delete(url)
get(url)

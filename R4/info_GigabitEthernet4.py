# Libraries
from http_methods import get
import connection as i

url = f"https://{i.server}/{i.rest_path}/data/ietf-interfaces:interfaces/interface=GigabitEthernet4"
print(url)

get(url)

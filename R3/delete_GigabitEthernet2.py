# Libraries
from http_methods import get
from http_methods import delete
import connection as i

url = f"https://{i.server}/{i.rest_path}/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"
print(url)

delete(url)
get(url)

# Libraries
import connection as i
from http_methods import get

url = f"https://{i.server}/{i.rest_path}/data/ietf-routing:routing-state"
print(url)

get(url)

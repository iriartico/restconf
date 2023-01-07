# Libraries
import connection as i
from http_methods import get

url = f"https://{i.server}/{i.rest_path}/data/ietf-restconf-monitoring:restconf-state/"
print(url)

get(url)

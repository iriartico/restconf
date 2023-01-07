# Libraries
from http_methods import get
import connection as i

url = f"https://{i.server}/{i.rest_path}"
print(url)

get(url)

# Libraries
import get_method as get
import basic_info as i
import sys
sys.path.append("/home/c4rtelos/Desktop/repos/restconf")

url = f"https://{i.server}/{i.rest_path}"
print(url)

get.get_method(url)

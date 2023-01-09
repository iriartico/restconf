# Libraries
from requests.auth import HTTPBasicAuth
import urllib3  # SSL certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Variables
user = "admin"
password = "admin"
format = "application/yang-data+json"
server = "10.10.10.30"
port = 443
rest_path = "restconf"

# Authentication
login = HTTPBasicAuth(user, password)

# Headers
header = {"Accept": format, "Content-Type": format}

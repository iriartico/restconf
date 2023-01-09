# Libraries
from http_methods import get
from http_methods import patch
import connection as i

# URL
url = f"https://{i.server}/{i.rest_path}/data/ietf-interfaces:interfaces/interface=GigabitEthernet5"
print(url)

# PAYLOAD
yangConfig = """
{
  "ietf-interfaces:interface": {
    "enabled": true,
    "description": "To WEB Server",
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "200.87.100.1",
          "netmask": "255.255.255.240"
        }
      ]
    }
  }
}
"""
patch(url, yangConfig)
get(url)

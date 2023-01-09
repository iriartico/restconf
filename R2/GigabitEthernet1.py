# Libraries
from http_methods import get
from http_methods import patch
import connection as i

# URL
url = f"https://{i.server}/{i.rest_path}/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"
print(url)

# PAYLOAD
yangConfig = """
{
  "ietf-interfaces:interface": {
    "enabled": true,
    "description": "LAN 1",
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "192.168.100.1",
          "netmask": "255.255.255.0"
        }
      ]
    }
  }
}
"""
patch(url, yangConfig)
get(url)

# Libraries
from http_methods import get
from http_methods import patch
import connection as i

# URL
url = f"https://{i.server}/{i.rest_path}/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"
print(url)

# PAYLOAD
yangConfig = """
{
  "ietf-interfaces:interface": {
    "enabled": true,
    "description": "To R1",
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "10.10.10.1",
          "netmask": "255.255.255.252"
        }
      ]
    }
  }

}
"""
patch(url, yangConfig)
get(url)
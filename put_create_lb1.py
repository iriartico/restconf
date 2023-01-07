# Libraries
from http_methods import get
from http_methods import put
import connection as i

# URL
url = f"https://{i.server}/{i.rest_path}/data/ietf-interfaces:interfaces/interface=Loopback1"
print(url)

# PAYLOAD
yangConfig = """
{
  "ietf-interfaces:interface": {
    "name": "Loopback1",
    "description": "loopack 1",
    "type": "iana-if-type:softwareLoopback",
    "enabled": true,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "20.20.20.1",
          "netmask": "255.255.255.0"
        }
      ]
    },
    "ietf-ip:ipv6": {}
  }
}
"""
put(url, yangConfig)
get(url)

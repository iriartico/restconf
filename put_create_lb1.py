# Libraries
import sys
import os
sys.path.append(os.getcwd())
import get_method as get
import put_method as put
import basic_info as i

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
put.put_method(url, yangConfig)
get.get_method(url)

# Libraries
import sys
import os
sys.path.append(os.getcwd())
import get_method as get
import put_method as put
import basic_info as i

# URL
url = f"https://{i.server}/{i.rest_path}/data/ietf-routing:routing/routing-instance=default/routing-protocols/routing-protocol=static,1"
print(url)

# PAYLOAD
yangConfig = """
{
  "ietf-routing:routing-protocol": {
    "type": "ietf-routing:static",
    "name": "1",
    "static-routes": {
      "ietf-ipv4-unicast-routing:ipv4": {
        "route": [
          {
            "destination-prefix": "192.168.3.0/24",
            "next-hop": {
              "next-hop-address": "10.10.10.2"
            }
          }
        ]
      }
    }
  }
}
"""
put.put_method(url, yangConfig)
get.get_method(url)

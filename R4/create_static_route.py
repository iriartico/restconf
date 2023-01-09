# Libraries
from http_methods import get
from http_methods import put
import connection as i

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
            "destination-prefix": "10.0.0.0/30",
            "next-hop": {
              "next-hop-address": "10.0.0.14"
            }
          },
          {
            "destination-prefix": "192.168.100.0/24",
            "next-hop": {
              "next-hop-address": "10.0.0.14"
            }
          },
          {
            "destination-prefix": "10.0.0.4/30",
            "next-hop": {
              "next-hop-address": "10.0.0.9"
            }
          },
          {
            "destination-prefix": "192.168.100.0/24",
            "next-hop": {
              "next-hop-address": "10.0.0.9"
            }
          }        
        ]
      }
    }
  }
}
"""
put(url, yangConfig)
get(url)

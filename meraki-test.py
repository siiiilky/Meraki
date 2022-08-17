import requests
import json
import config

# Set header
headers = {
   "X-Cisco-Meraki-API-Key": config.APIKEY
}

url = "https://api.meraki.com/api/v1/organizations"

# Send request and get response
response = requests.request(
   "GET",
   url,
   headers=headers
)

# Print organization output
my_orgs = json.loads(response.text)
for org in my_orgs:
    print(org)

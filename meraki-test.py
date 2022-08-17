import requests
import json
import config

url = "https://api.meraki.com/api/v1/organizations"

# Send request and get response
response = requests.request(
   "GET",
   config.url,
   headers=config.headers
)

# Print organization output
my_orgs = json.loads(response.text)
for org in my_orgs:
    print(org)

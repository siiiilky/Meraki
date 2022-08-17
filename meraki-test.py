import requests
import json

# Set api key. The below api key is for the Meraki Sandbox
# Replace it with your API key
api_key = '9c1196c0836dcd0ce0e3cdc3fc5615c29e54fd98'

# Set header parameters
headers = {
   "X-Cisco-Meraki-API-Key" : api_key
}

url = "https://api.meraki.com/api/v1/organizations"

# Send request and get response
response = requests.request(
   "GET",
   url,
   headers=headers
)

# Print organization id and name
my_orgs = json.loads(response.text)
for org in my_orgs:
    print (org)
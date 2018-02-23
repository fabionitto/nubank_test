#!/usr/bin/env python
import json
import requests
import requests.auth
import getpass

CLIENT_ID = 'other.conta' # Fill this in with your client ID
CLIENT_SECRET = 'yQPeLzoHuJzlMMSAjC-LgNUJdUecx8XO' # Fill this in with your client secret
DISCOVER_URL = 'https://prod-auth.nubank.com.br/api/discovery'

username = raw_input('User: ')
password = getpass.getpass()

# Discover urls
urls = requests.get(DISCOVER_URL)

token_url = urls.json()['token']

# nubank requires that authorization parameters be sent as JSON payload
payload =  {"grant_type": "password", "username": username, "password": password, "client_id":CLIENT_ID, "client_secret":CLIENT_SECRET}
post_data = json.dumps(payload)

headers = {"Content-type": "application/json"}
response = requests.post(token_url, auth=False, data=post_data, headers=headers)

print response.status_code
print response.json()

access_token = response.json()['access_token']
refresh_token = response.json()['refresh_token']

# transaction_r is the result of a GET on the specific transaction link
#
# To update a transaction category you need to PATCH with mcc key and value as new category
# new_cat = '{"mcc": "supermercado"}
# token_header = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json;charset=UTF-8' }
# category_link = transaction_r.json()['transaction']['_links']['category']['href']
# result = requests.patch(category_link, headers=headers_token, data=new_cat)
#
#
#
#

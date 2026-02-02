import sys
from os import getenv
from pprint import pprint
from __init__ import username, password, event
import requests

BASE_URL = "https://api.peregrinefrc.com/"


# Log into the server using username / password stored in environment variables
#username = "Alava"
#password = "heyisaac"
print(f"Username: {username}")

payload = {"username": username, "password": password}
r = requests.post(BASE_URL + "authenticate", json=payload)
if r.status_code != 200:
    print(r.status_code)
    print(r.text)
    sys.exit(1)
access_token = r.json()["accessToken"]
refresh_token = r.json()["refreshToken"]
print(f"Access Token: {access_token}")
print(f"Refresh Token: {refresh_token}")
security_header = {"Authorization": f"Bearer {access_token}"}

# Get the available years on the server

#event = "2025wass"

payload = {"event": event}
r = requests.get(BASE_URL + "reports", params=payload, headers=security_header)
print(r.status_code)
pprint(r.json())

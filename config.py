import requests

token="RNV2VpwQrlKV0DwNURjK"

endpoint="https://the-one-api.dev/v2/"
headers = {"Authorization": "Bearer RNV2VpwQrlKV0DwNURjK"}

movies=requests.get(f"{endpoint}character",headers=headers)
all_chars=movies.json()['docs']
print(all_chars)




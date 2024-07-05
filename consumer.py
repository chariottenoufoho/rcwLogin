import requests

url = 'https://rcw.azurewebsites.net/RCW_API'

data = {
    "first_name" : 'Steve',
    'last_name' : 'Ataky'
}

response = requests.post(url, json=data)

if response.status_code==200:
    print(response.json())
else:
    print(f"Failed to connect to thw API. Status code: {response.status_code}")

import requests

request = requests.get('https://api.magicthegathering.io/v1/cards/')
response = request.json()

print(response)
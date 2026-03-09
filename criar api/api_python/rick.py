import requests
import pprint

site_api = "https://rickandmortyapi.com/api/character"


site = requests.get(site_api)

print(site.status_code)
pprint.pprint(site.content)
site.json()



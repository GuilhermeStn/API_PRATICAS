import requests

site = " https://reqres.in/api/users"

key = "reqres_13ef0ebba8944df8b87ce9de10f0936c"

resposta = requests.get(site,params=key)

print(resposta.status_code)
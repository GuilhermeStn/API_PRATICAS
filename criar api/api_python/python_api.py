import requests 
import pprint
# usar para pegar informações = get

# API de Clima 

## WEATHER6981

api_key ="bb6d4e27073a43fbbdd134305260803"

### chave para conexão 

parametros = {
    "key":api_key, 
    "q":"Paris",
    "lang":"fr",
}

## required the key of your api , and others if you want to get others stuffs

## resposta de api json or xml 

link_api = "http://api.weatherapi.com/v1/current.json"

### base da api 

resposta = requests.get(link_api, params=parametros)
## pega as informações da api

print(resposta.status_code)

if resposta.status_code == 200:
    print("conexão aceita ")
    dados_request = resposta.json()
    pprint.pprint(dados_request)
    temperature = dados_request["current"]["temp_c"]
    # dentro de current eu vou pegar a temperatura 
    describe = dados_request["current"]["condition"]["text"]
    # dentro de current > dentro de condição  eu vou pegar o texto que mostra a condição
    pprint.pprint(temperature)
    pprint.pprint(describe)

## status_code => 

# 200 = requisição aceita 
# 300 = requisição redirecionada 
# 401 = requisição proibida 
# 500 = server fora do ar 

# mandar a chave de API para ter 

print(resposta.content)

## resposta da nossa requisição 



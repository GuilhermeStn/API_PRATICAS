import requests 
import pprint 


url = "https://pokeapi.co/api/v2/pokemon/"

base = requests.get(url)

if base.status_code:
    print(f"Site aceitou conexão na porta : {base.status_code}")
    nome = str(input("Type the PokemonName: "))
    print(nome)
    base = "https://pokeapi.co/api/v2/pokemon/" + nome 
    print(base)
    resposta = requests.get(base)
    if resposta == 200:
        print("DADOS OBTIDOS COM SUCESSO ")
        pokemon_response = resposta.json()
        print(pokemon_response.content())
        

    





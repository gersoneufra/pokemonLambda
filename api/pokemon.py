import requests

def all():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto/")
    return response.content

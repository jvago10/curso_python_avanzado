import requests
import json
import webbrowser

BASE_URL = 'https://pokeapi.co/api/v2/pokemon/'


def get_pokemon_info(pokemon_name):
    api_url = BASE_URL + pokemon_name
    response = requests.get(api_url)

    try:
        pokemon_data = json.loads(response.text)
        sprites = pokemon_data['sprites']
        pokemon_image = sprites['front_default']
        webbrowser.open(pokemon_image)

    except ValueError:
        print('No se encontró el pokemon')


if __name__ == '__main__':
    search_pokemon_name = input('Ingrese el nombre del pokemon: ')
    get_pokemon_info(search_pokemon_name)

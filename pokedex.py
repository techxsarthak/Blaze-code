import requests

def fetch_pokemon_stats(pokemon_name):
    # Define the base URL for the PokeAPI
    uri_host = 'https://pokeapi.co/api/v2/pokemon/'
    
    # Send a GET request to the API
    response = requests.get(uri_host + pokemon_name.lower())
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        pokemon_data = response.json()
        
        # Extract relevant stats
        stats = {
            'name': pokemon_data['name'],
            'height': pokemon_data['height'],
            'weight': pokemon_data['weight'],
            'base_stats': {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}
        }
        
        return stats
    else:
        return f"Error: Pokémon '{pokemon_name}' not found."

# Example usage
pokemon_name = 'pikachu'
stats = fetch_pokemon_stats(pokemon_name)
print(stats)

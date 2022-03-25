
#Question 1

#In this session you used the Pokémon API to retrieve a single Pokémon.

#I want a program that can retrieve multiple Pokémon and save their names and moves to a file.

#Use a list to store about 6 Pokémon IDs. Then in a for loop call the API to retrieve the data for

#each Pokémon. Save their names and moves into a file called 'pokemon.txt'

#import dependencies
import random
import requests
import json
from pprint import pprint as pp

#create empty list called 'pokemon_numbers'
pokemon_numbers = []

#draw 6 random pokemon numbers and add them to the list pokemon_numbers
for number in range(0, 6):
   pokemon_number = random.randint(1, 898)
   pokemon_numbers.append(pokemon_number)

#create new file called 'pokemon.txt'. For each number in pokemon_numbers, pull the details of the corresponding pokemon
#from the pokemon api. Then write the name of each pokemon to the text file.
with open('pokemon.txt', 'w') as text_file:
   for pokemon_number in pokemon_numbers:
       url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon_number)
       response = requests.get(url)
       pokemon = response.json()


       text_file.write(pokemon['name'] + '\n')

## HW03 - find public API and use Python to get data
    # How many films in this API?
    # What is the planet in each films, explain all the planet name, diameter, population

import requests
import time

# get total film => 6 films
url = "https://swapi.dev/api/films/"
resp = requests.get(url)
film_count = resp.json()["count"]

for i in range(1, film_count + 1):
    url_film = f"https://swapi.dev/api/films/{i}"
    resp_film = requests.get(url_film)
    film_data = resp_film.json()
    print(f"Title: {film_data['title']}, Episode id: {film_data['episode_id']}")

    planets = []

    for url_planet in film_data["planets"]:
        resp_planet = requests.get(url_planet)
        planet_data = resp_planet.json()
        planets.append(
            {"Name": planet_data["name"], "Diameter": planet_data["diameter"], "Population": planet_data["population"]}
        )

    for planet in planets:
        print(planet)

    # break for a second
    time.sleep(1)


### This is a  result:
Title: A New Hope, Episode id: 4
{'Name': 'Tatooine', 'Diameter': '10465', 'Population': '200000'}
{'Name': 'Alderaan', 'Diameter': '12500', 'Population': '2000000000'}
{'Name': 'Yavin IV', 'Diameter': '10200', 'Population': '1000'}
Title: The Empire Strikes Back, Episode id: 5
{'Name': 'Hoth', 'Diameter': '7200', 'Population': 'unknown'}
{'Name': 'Dagobah', 'Diameter': '8900', 'Population': 'unknown'}
{'Name': 'Bespin', 'Diameter': '118000', 'Population': '6000000'}
{'Name': 'Ord Mantell', 'Diameter': '14050', 'Population': '4000000000'}
Title: Return of the Jedi, Episode id: 6
{'Name': 'Tatooine', 'Diameter': '10465', 'Population': '200000'}
{'Name': 'Dagobah', 'Diameter': '8900', 'Population': 'unknown'}
{'Name': 'Endor', 'Diameter': '4900', 'Population': '30000000'}
{'Name': 'Naboo', 'Diameter': '12120', 'Population': '4500000000'}
{'Name': 'Coruscant', 'Diameter': '12240', 'Population': '1000000000000'}
Title: The Phantom Menace, Episode id: 1
{'Name': 'Tatooine', 'Diameter': '10465', 'Population': '200000'}
{'Name': 'Naboo', 'Diameter': '12120', 'Population': '4500000000'}
{'Name': 'Coruscant', 'Diameter': '12240', 'Population': '1000000000000'}
Title: Attack of the Clones, Episode id: 2
{'Name': 'Tatooine', 'Diameter': '10465', 'Population': '200000'}
{'Name': 'Naboo', 'Diameter': '12120', 'Population': '4500000000'}
{'Name': 'Coruscant', 'Diameter': '12240', 'Population': '1000000000000'}
{'Name': 'Kamino', 'Diameter': '19720', 'Population': '1000000000'}
{'Name': 'Geonosis', 'Diameter': '11370', 'Population': '100000000000'}
Title: Revenge of the Sith, Episode id: 3
{'Name': 'Tatooine', 'Diameter': '10465', 'Population': '200000'}
{'Name': 'Alderaan', 'Diameter': '12500', 'Population': '2000000000'}
{'Name': 'Dagobah', 'Diameter': '8900', 'Population': 'unknown'}
{'Name': 'Naboo', 'Diameter': '12120', 'Population': '4500000000'}
{'Name': 'Coruscant', 'Diameter': '12240', 'Population': '1000000000000'}
{'Name': 'Utapau', 'Diameter': '12900', 'Population': '95000000'}
{'Name': 'Mustafar', 'Diameter': '4200', 'Population': '20000'}
{'Name': 'Kashyyyk', 'Diameter': '12765', 'Population': '45000000'}
{'Name': 'Polis Massa', 'Diameter': '0', 'Population': '1000000'}
{'Name': 'Mygeeto', 'Diameter': '10088', 'Population': '19000000'}
{'Name': 'Felucia', 'Diameter': '9100', 'Population': '8500000'}
{'Name': 'Cato Neimoidia', 'Diameter': '0', 'Population': '10000000'}
{'Name': 'Saleucami', 'Diameter': '14920', 'Population': '1400000000'}

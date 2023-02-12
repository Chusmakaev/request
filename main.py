from pprint import pprint
import requests
import json

def heroes():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url=url)
    super_hero = []
    for item in response.json():
        intelligence = item
        try:
            for power_stats in intelligence['results']:
                super_hero.append({
                    'name': power_stats['name'],
                    'intelligence': power_stats['powerstats']['intelligence']
                })
        except KeyError:
            print(f"Надо проверить ссылку")
    intelligence_super_man = 0
    name = ''
    for intelligence_super in super_hero:
        if intelligence_super_man < int(intelligence_super['intelligence']):
            intelligence_super_man = int(intelligence_super['intelligence'])
            name = intelligence_super['name']
    print(f"Самый умный {name}, интелект: {intelligence_super_man}")
heroes()


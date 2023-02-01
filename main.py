from pprint import pprint
import requests

def super_heroes():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url=url)
    pprint(response.json())

if __name__ == '__main__':
    print(super_heroes())

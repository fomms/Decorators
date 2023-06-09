from tools import logger1
import requests


@logger1
def find_smartest():
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    names = []
    response = requests.get(url)
    for name in response.json():
        if name['name'] in ['Hulk', 'Captain America', 'Thanos']:
            names.append(name)
    return f'''Самый умный: {sorted(names, key=lambda x: x["powerstats"]["intelligence"], reverse=True)[0]['name']}'''

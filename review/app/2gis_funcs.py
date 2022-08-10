import json
import requests


YOUR_KEY = 'FFRERE4'
url = 'https://catalog.api.2gis.com/3.0/items'


def get_org_id(name):
    get_org_params = {
        'q': 'вкусно и точка', 'fields': 'items.org', 'key': YOUR_KEY
    }
    org_info = requests.get(url, params=get_org_params).content.decode()
    return json.loads(org_info)['id'].split('_')[0]


def get_city_id(name):
    get_city_params = {'q': 'Уфа', 'fields': 'items.org', 'key': YOUR_KEY}
    city_info = requests.get(url, params=get_city_params).content.decode()
    return json.loads(city_info)['id'].split('_')[0]


def get_org_places(city_name, org_name):
    city_id = get_city_id(city_name)
    org_id = get_org_id(org_name)
    params = {'city_id': city_id, 'org_id': org_id, 'key': YOUR_KEY}
    places_json = requests.get(url, params=params).content.decode()
    return json.loads(places_json)['result']['items']


places = get_org_places('Уфа', 'вкусно и точка')
for item in places:
    addr = item['address_name']
    name = item['reviews']

import requests
import os
import xml.etree.ElementTree as ET

baseUrl = os.environ['BG_API_URI']


def get_data(user_id):
    url = baseUrl + f'user?name={user_id}'
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f'Error: {resp.status_code}')
    return __parse_response(resp.text)


def __parse_response(response):
    root = ET.fromstring(response)
    parsed = {}
    for child in root:
        parsed[child.tag] = child.attrib['value']
    return parsed

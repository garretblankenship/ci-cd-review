import requests
import json

def get_joke():
    response = requests.get("https://sv443.net/jokeapi/v2/joke/Any")
    return (response.status_code, json.loads(response.text))
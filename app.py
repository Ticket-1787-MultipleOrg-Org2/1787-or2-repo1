
import requests
import flask
import django


resp = requests.get("https://ipinfo.io")
password = "test"

print(resp.json())

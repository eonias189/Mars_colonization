from pprint import pprint
import datetime as dt
import requests

url = 'http://127.0.0.1:5000/api/v2/users/6'
response = requests.delete(url)
print(response.json())

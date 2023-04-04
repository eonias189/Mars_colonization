from pprint import pprint
import datetime as dt
from tools import hash_password
import requests

js = {'id': 6, 'surname': 'surname', 'name': 'name_', 'age': 30,
      'position': 'position', 'speciality': 'speciality',
      'address': 'address', 'email': 'eonias',
      'hashed_password': hash_password('qwerty'),
      'modified_date': str(dt.datetime.now())}

url = 'http://127.0.0.1:5000/api/v2/users/6'
response = requests.put(url, json=js)
pprint(response.json())

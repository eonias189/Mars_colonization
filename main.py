from pprint import pprint
import datetime as dt
import requests

url = 'http://127.0.0.1:5000/edit_job/1'
response = requests.get(url)
print(response)

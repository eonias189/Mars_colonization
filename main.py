import requests
import datetime as dt
from pprint import pprint

url = 'http://127.0.0.1:5000/api/v2/jobs/5'
good_js = {'id': 4, 'team_leader': 5, 'job': 'good_job_', 'work_size': 11,
           'collaborators': '1', 'start_date': str(dt.datetime.now()),
           'end_date': '', 'is_finished': True}
response = requests.put(url, json=good_js).json()
print(response)

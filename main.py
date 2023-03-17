from pprint import pprint
import datetime as dt
import requests

response = requests.post('http://127.0.0.1:5000/api/jobs',
                         json={'id': 4, 'job': 'job_new', 'team_leader': 5,
                               'work_size': 15, 'collaborators': '1, 2, 3',
                               'start_date': dt.datetime.now().strftime(
                                   '%Y:%M:%D'), 'end_date': '2023/03/17',
                               'is_finished': True})
print(response.json())

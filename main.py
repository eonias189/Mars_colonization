from pprint import pprint
import datetime as dt
import requests

url = 'http://127.0.0.1:5000/api/jobs'
new_job = {'id': 8, 'team_leader': 3, 'job': 'job_edited', 'work_size': 15, 'start_date': str(dt.datetime.now()),
           'collaborators': '1, 2, 3', 'is_finished': False}
pprint(requests.get(url).json())  # все работы
pprint(requests.put(url + '/5', json=new_job).json())  # корректный запрос
pprint(requests.get(url).json())  # работа изменилась
pprint(requests.put(url + '/8', json={}).json())  # запрос без данных
new_job['id'] = 1
pprint(requests.put(url + '/8', json=new_job).json())  # id уже занято
new_job['id'] = 6
new_job['team_leader'] = 999
pprint(requests.put(url + '/8', json=new_job).json())  # team_leader id не существует

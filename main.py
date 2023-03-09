import datetime as dt
from data import db_session
from data.users import User
from data.jobs import Jobs

db_session.global_init("db/mars_explorer.db")
session = db_session.create_session()

job = Jobs()
job.team_leader = 1
job.job = 'deployment of residential modules 1 and 2'
job.work_size = '15'
job.collaborators = '2, 3'
job.start_date = dt.datetime.now()
job.is_finished = False
session.add(job)

session.commit()

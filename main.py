import datetime as dt
from data import db_session
from data.users import User
from data.jobs import Jobs

db_session.global_init("db/mars_explorer.db")
session = db_session.create_session()

# global_init(input())
# session = create_session()

jobs = session.query(Jobs).all()
team_leads = sorted([(len(job.collaborators.split(', ')), job.team_leader) for job in jobs], key=lambda x: x[0])[::-1]
n_max = team_leads[0][0]
users = [i[1] for i in team_leads if i[0] == n_max]
users = session.query(User).filter(User.id.in_(users))
for i in users:
    print(f'{i.name} {i.surname}')
session.commit()

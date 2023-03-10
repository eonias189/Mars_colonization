import datetime as dt
from data import db_session
from data.users import User
from data.jobs import Jobs

db_session.global_init("db/mars_explorer.db")
session = db_session.create_session()

# global_init(input())
# session = create_session()

jobs = session.query(Jobs).all()
users = session.query(User).filter(User.address == 'module_1', User.age < 21)
for user in users:
    user.address = 'module_3'
session.commit()

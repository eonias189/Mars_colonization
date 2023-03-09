from data import db_session
from data.users import User

db_session.global_init("db/mars_explorer.db")
session = db_session.create_session()

data = [('Scott', 'Ridley', 21, 'captain', 'research engineer', 'module_1',
         'scott_chief@mars.org')]
data += [(f'surmame_{i}', f'name_{i}', 20 + i, f'position_{i}',
          f'speciality_{i}', f'address_{i}', f'email{i}@mars.org') for i in
         range(2, 5)]
for user_data in data:
    user = User()
    user.surname, user.name, user.age, user.position, user.speciality, user.address, user.email = user_data
    session.add(user)

session.commit()

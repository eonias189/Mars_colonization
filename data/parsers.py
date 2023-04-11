from flask_restful import reqparse


class UserParser(reqparse.RequestParser):
    def __init__(self):
        super().__init__()
        self.add_argument('id', required=True, type=int)
        self.add_argument('surname', required=True)
        self.add_argument('name', required=True)
        self.add_argument('age', required=True, type=int)
        self.add_argument('position', required=True)
        self.add_argument('speciality', required=True)
        self.add_argument('address', required=True)
        self.add_argument('email', required=True)
        self.add_argument('hashed_password', required=True)
        self.add_argument('modified_date', required=True)


class JobParser(reqparse.RequestParser):
    def __init__(self):
        super().__init__()
        self.add_argument('id', required=True, type=int)
        self.add_argument('team_leader', required=True)
        self.add_argument('job', required=True)
        self.add_argument('work_size', required=True, type=int)
        self.add_argument('collaborators', required=True)
        self.add_argument('start_date', required=True)
        self.add_argument('end_date', required=True)
        self.add_argument('is_finished', required=True)


if __name__ == '__main__':
    parser = UserParser()

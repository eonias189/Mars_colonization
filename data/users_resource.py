import datetime as dt
from flask_restful import abort, Resource
from flask import jsonify
from . import db_session
from .users import User
from .parsers import UserParser


def abort_if_not_founded(user_id):
    db_sess = db_session.create_session()
    if not db_sess.query(User).get(user_id):
        return abort(404, message=f'User {user_id} not found')


USER_TO_DICT_ONLY = ('id', 'surname', 'name', 'age', 'position', 'speciality',
                     'address',
                     'email', 'modified_date')


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_not_founded(user_id)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        return jsonify({'user': user.to_dict(only=USER_TO_DICT_ONLY)})

    def put(self, user_id):
        abort_if_not_founded(user_id)
        db_sess = db_session.create_session()
        parser = UserParser()
        args = parser.parse_args()
        user = db_sess.query(User).get(user_id)
        id_was = db_sess.query(User).get(args['id'])
        if id_was and id_was.id != user_id:
            return jsonify({'error': 'Id is already taken'})
        user_was = db_sess.query(User).filter(
            User.email == args['email']).first()
        if user_was and user_was.email != user.email:
            return jsonify({'error': 'email is already taken'})
        user.id = args['id']
        user.surname = args['surname']
        user.name = args['name']
        user.age = args['age']
        user.position = args['position']
        user.speciality = args['speciality']
        user.address = args['address']
        user.email = args['email']
        user.modified_date = dt.datetime.strptime(args['modified_date'],
                                                  '%Y-%m-%d %H:%M:%S.%f')
        user.set_password(args['hashed_password'])
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def delete(self, user_id):
        abort_if_not_founded(user_id)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        db_sess.delete(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})


class UserListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        users = db_sess.query(User).all()
        return jsonify({'users': [
            [user.to_dict(only=USER_TO_DICT_ONLY) for user in users]]})

    def post(self):
        parser = UserParser()
        args = parser.parse_args()
        db_sess = db_session.create_session()
        if db_sess.query(User).get(args['id']):
            return jsonify({'error': 'Id is already taken'})
        if db_sess.query(User).filter(User.email == args['email']).first():
            return jsonify({'error': 'email is already taken'})
        user = User(id=args['id'], surname=args['surname'], name=args['name'],
                    age=args['age'], position=args['position'],
                    speciality=args['speciality'], address=args['address'],
                    email=args['email'],
                    modified_date=dt.datetime.strptime(args['modified_date'],
                                                       '%Y-%m-%d %H:%M:%S.%f'))
        user.set_password(args['hashed_password'])
        db_sess.add(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})

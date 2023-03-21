from flask_restful import reqparse, abort, Resource
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

from flask import jsonify
from flask_restful import abort, Resource
from . import db_session
from .parsers import JobParser
from .users import User
from .jobs import Jobs


def abort_if_not_founded(job_id):
    db_sess = db_session.create_session()
    if not db_sess.query(Jobs).get(job_id):
        return abort(404, message=f'Job {job_id} not found')


JOB_TO_DICT_ONLY = (
    'id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date',
    'end_date', 'is_finished')


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_not_founded(job_id)
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(job_id)
        return jsonify(job.to_dict(only=JOB_TO_DICT_ONLY))

    def put(self, job_id):
        abort_if_not_founded(job_id)
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(job_id)
        parser = JobParser()
        args = parser.parse_args()
        if args['id'] != job.id and db_sess.query(Jobs).get(args['id']):
            return jsonify({'error': 'Id already exists'})
        if not db_sess.query(User).get(args['team_leader']):
            return jsonify({'error': 'Team leader not found'})
        job.id, job.team_leader, job.job, job.work_size, \
        job.collaborators, job.start_date, job.end_date, job.is_finished = [
            args[i] for i in
            ['id', 'team_leader', 'job', 'work_size', 'collaborators',
             'start_date', 'end_date', 'is_finished']]
        job.is_finished = True if args[
                                      'is_finished'].lower() == 'true' else False
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def delete(self, job_id):
        abort_if_not_founded(job_id)
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(job_id)
        db_sess.delete(job)
        db_sess.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).all()
        return jsonify([i.to_dict(only=JOB_TO_DICT_ONLY) for i in jobs])

    def post(self):
        parser = JobParser()
        args = parser.parse_args()
        db_sess = db_session.create_session()
        if db_sess.query(Jobs).get(args['id']):
            return jsonify({'error': 'Id already exists'})
        user = db_sess.query(User).get(args['team_leader'])
        if not user:
            return jsonify({'error': 'Team leader not found'})
        job = Jobs(id=args['id'], team_leader=args['team_leader'],
                   job=args['job'], work_size=args['work_size'],
                   collaborators=args['collaborators'],
                   start_date=args['start_date'], end_date=args['end_date'],
                   is_finished=True if args[
                                           'is_finished'].lower() == 'true' else False)
        job.user = user
        db_sess.add(job)
        db_sess.commit()
        return jsonify({'success': 'OK'})

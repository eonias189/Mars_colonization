import flask

from flask import jsonify, request
from . import db_session
from .users import User
from .jobs import Jobs

blueprint = flask.Blueprint('server_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify({'jobs': [
        item.to_dict() for item in jobs]})


@blueprint.route('/api/jobs/<job_id>')
def get_job_id(job_id):
    if not job_id.isdigit():
        return jsonify({'error': 'Bad Request'})
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not Found'})
    return jsonify({'jobs': job.to_dict()})


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty Request'})
    if not all([key in request.json for key in
                ['id', 'team_leader', 'job', 'work_size', 'collaborators',
                 'start_date', 'is_finished']]):
        return jsonify({'error': 'Not all required keys are given'})
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(request.json['team_leader'])
    if not user:
        return jsonify({'error': 'Team leader not founded'})
    job = Jobs(id=request.json['id'], team_leader=request.json['team_leader'],
               job=request.json['job'], work_size=request.json['work_size'],
               collaborators=request.json['collaborators'],
               start_date=request.json['start_date'],
               end_date=request.json.get('end_date', None),
               is_finished=request.json['is_finished'])
    job.user = user
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})

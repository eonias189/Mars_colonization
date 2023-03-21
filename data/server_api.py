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
        return jsonify({'error': 'Team leader not found'})
    already_job = db_sess.query(Jobs).get(request.json['id'])
    if already_job:
        return jsonify({'error': 'Id already exists'})
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


@blueprint.route('/api/jobs', methods=['DELETE', 'PUT'])
def euuu():
    return jsonify({'Ошибка': 'Так нельзя!'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_point(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Job not found'})
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['PUT'])
def edit_job(job_id):
    if not request.json:
        return jsonify({'error': 'Empty Request'})
    if not all([key in request.json for key in
                ['id', 'team_leader', 'job', 'work_size', 'collaborators',
                 'start_date', 'is_finished']]):
        return jsonify({'error': 'Not all required keys are given'})
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Job not found'})
    job_already = db_sess.query(Jobs).get(request.json['id'])
    if job_already and job_already.id != job.id:
        return jsonify({'error': 'Id is already taken'})
    user = db_sess.query(User).get(request.json['team_leader'])
    if not user:
        return jsonify({'error': 'Team leader not found'})
    job.id, job.team_leader, job.job, job.work_size, job.collaborators, job.start_date, job.is_finished = [
        request.json[key] for key
        in ['id',
            'team_leader',
            'job',
            'work_size',
            'collaborators',
            'start_date',
            'is_finished']]
    if 'end_date' in request.json:
        job.end_date = request.json['end_date']
    job.user = user
    db_sess.commit()
    return jsonify({'success': 'OK'})

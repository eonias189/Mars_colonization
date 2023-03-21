import datetime as dt

import flask
from flask import Flask, url_for, request, render_template, redirect, \
    make_response, session
from flask_restful import reqparse, abort, Api, Resource
from flask_login import LoginManager, login_user, current_user, login_required, \
    logout_user

import data.users_resource
from data import db_session, server_api
from data.users import User
from data.jobs import Jobs
from tools import RegisterForm, hash_password, RegisterSuccess, LoginForm2, \
    AddJob, EditJob

db_session.global_init("db/mars_explorer.db")
session = db_session.create_session()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = dt.timedelta(days=365)
app.register_blueprint(server_api.blueprint)

api = Api(app)
api.add_resource(data.users_resource.UsersResource, '/api/v2/users/<int:user_id>')
api.add_resource(data.users_resource.UserListResource, '/api/v2/users')

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.errorhandler(404)
def not_found(error):
    return make_response(flask.jsonify({'error': 'Not found'}), 404)


@app.errorhandler(405)
def error_405(error):
    return make_response(flask.jsonify({'error': '405'}), 405)


@app.errorhandler(400)
def bad_request(_):
    return make_response(flask.jsonify({'error': 'Bad Request'}), 400)


@app.errorhandler(401)
def error_401(_):
    return render_template('access_denied.html', title='отказано в доступе')


@app.route('/')
def main():
    url_delete = url_for('static', filename='img/delete.png')
    url_style = url_for('static', filename='css/style_works_log.css')
    data = [[job.id, job.team_leader, job.job,
             f'{job.user.surname} {job.user.name}',
             f'{job.work_size} hours', job.collaborators,
             'Is finished' if job.is_finished else 'Is not finished'] for job in
            session.query(Jobs).all()]
    return render_template('works_log.html', url_style=url_style, data=data,
                           url_delete=url_delete,
                           title='Главная страница')


@app.route('/delete_job/<int:job_id>', methods=['GET'])
@login_required
def delete_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return make_response(flask.jsonify({'error': 'Job not founded'}))
    if current_user.id not in [1, job.team_leader]:
        return error_401(None)
    db_sess.delete(job)
    db_sess.commit()
    return redirect('/')


@app.route('/edit_job/<int:job_id>', methods=['POST', 'GET'])
@login_required
def edit_job(job_id):
    form = EditJob()
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return make_response('Ошибка: Работа не найдена')
    if current_user.id not in [1, job.team_leader]:
        return error_401(None)
    url_style = url_for('static', filename='css/style_form.css')
    form_data = job.to_dict()
    if form_data['end_date'] == None:
        form_data['end_date'] = '-'
    params = {'title': 'редактирование', 'url_style': url_style, 'form': form,
              'form_data': form_data}
    if form.validate_on_submit():
        user = db_sess.query(User).get(form.team_leader.data)
        if not user:
            return render_template('edit_job.html',
                                   message=f'Пользователь с id {form.team_leader.data} не найден',
                                   **params)
        job.team_leader = form.team_leader.data
        job.job = form.job.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.start_date = form.start_date.data
        job.end_date = form.end_date.data
        job.is_finished = form.is_finished.data
        job.user = user
        db_sess.commit()
        return redirect('/')
    return render_template('edit_job.html', **params)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm2()
    url_style = url_for('static', filename='css/style_form.css')
    params = {'title': 'авторизация', 'url_style': url_style, 'form': form,
              'user': current_user}
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if not user:
            return render_template('login_2.html', **params,
                                   message='Пользователь не найден')
        if not user.check_password(hash_password(form.password.data)):
            return render_template('login_2.html', **params,
                                   message='Неверный пароль')
        login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template('login_2.html', **params)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    url_style = url_for('static', filename='css/style_form.css')
    if form.validate_on_submit():
        if form.password.data != form.rep_password.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают",
                                   url_style=url_style)
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.log_em.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть",
                                   url_style=url_style)
        user = User(email=form.log_em.data, surname=form.surname.data,
                    name=form.name.data,
                    age=form.age.data, speciality=form.speciality.data,
                    address=form.address.data, position=form.position.data,
                    modified_date=dt.datetime.now())
        user.set_password(hash_password(form.password.data))
        db_sess.add(user)
        db_sess.commit()
        return redirect('/register/success')
    return render_template('register.html', title='Регистрация', form=form,
                           url_style=url_style)


@app.route('/register/success', methods=['GET', 'POST'])
def register_success():
    ans = RegisterSuccess()
    url_style = url_for('static', filename='css/style_form.css')
    if ans.validate_on_submit():
        return redirect('/')
    return render_template('register_success.html', form=ans,
                           title='регистрация успешна', url_style=url_style)


@app.route('/addjob', methods=['POST', 'GET'])
def add_job():
    url_style = url_for('static', filename='css/style_form.css')
    form = AddJob()
    params = {'title': 'Добавление работы', 'url_style': url_style,
              'form': form, 'current_user': current_user}
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs(job=form.job.data, team_leader=form.team_leader.data,
                   work_size=form.work_size.data,
                   collaborators=form.collaborators.data,
                   start_date=dt.datetime.now(),
                   is_finished=form.is_finished.data)
        user = db_sess.query(User).get(form.team_leader.data)
        if not user:
            return render_template('add_job.html', **params,
                                   message=f'пользователь с id {form.team_leader.data} не найден')
        job.user = user
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('add_job.html', **params)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')

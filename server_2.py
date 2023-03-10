import datetime as dt
from flask import Flask, url_for, request, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs
from tools import RegisterForm, hash_password

db_session.global_init("db/mars_explorer.db")
session = db_session.create_session()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def main():
    url_style = url_for('static', filename='css/style_works_log.css')
    data = [[job.job, f'{job.user.surname} {job.user.name}',
             f'{job.work_size} hours', job.collaborators,
             'Is finished' if job.is_finished else 'Is not finished'] for job in
            session.query(Jobs).all()]
    return render_template('works_log.html', url_style=url_style, data=data)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.rep_password.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.log_em.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(email=form.log_em, surname=form.surname, name=form.name,
                    age=form.age, speciality=form.speciality,
                    address=form.address, position=form.position,
                    modified_date=dt.datetime.now())
        user.set_password(hash_password(form.password))
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')

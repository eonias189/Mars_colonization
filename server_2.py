from flask import Flask, url_for, request, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs

db_session.global_init("db/mars_explorer.db")
session = db_session.create_session()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def main():
    url_style = url_for('static', filename='css/style_works_log.css')
    data = [[job.job, f'{job.user.surname} {job.user.name}', f'{job.work_size} hours', job.collaborators,
             'Is finished' if job.is_finished else 'Is not finished'] for job in
            session.query(Jobs).all()]
    return render_template('works_log.html', url_style=url_style, data=data)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')

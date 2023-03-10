from flask import Flask, url_for, request, render_template, redirect
from tools import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def main():
    return render_template('base.html')


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/promotion')
def promotion():
    data = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!']

    return f"""
    <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8">
                <title>о нас</title>
            </head>
            <body>
                <p>
                    {'</br>'.join(data)}"
                </p>
            </body>
        </html>
    """


@app.route('/promotion_image')
def promotion_image():
    data = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!']
    url_pic = url_for('static', filename='img/mars.jpg')
    url_style = url_for('static', filename='css/style.css')
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <div role="alert">
                        <img src="{}" alt="здесь должна была быть картинка, но не нашлась">
                    </div>
                    <div class="alert-dark" role="alert">
                      <br><h3>{}</h3>
                    </div>
                    <div class="alert-success" role="alert">
                      <br><h3>{}</h3>
                    </div>
                    <div class="alert-secondary" role="alert">
                      <br><h3>{}</h3>
                    </div>
                    <div class="alert-warning" role="alert">
                      <br><h3>{}</h3>
                    </div>
                    <div class="alert-danger" role="alert">
                      <br><h3>{}</h3>
                    </div>
                  </body>
                </html>""".format(url_style, url_pic, *data)


@app.route('/image_mars')
def image_mars():
    return f'''
    <!doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Привет, Марс!</title>
        </head>
        <body>
            <h1>Жди нас, Марс!</h1>
            <img src="{url_for('static', filename='img/mars.jpg')}" alt="здесь должна была быть картинка, но не нашлась">
            <p>
                Вот она какая, красная планета.
            </p>
        </body>
    </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    prof_list = [('инженер-исследователь', 'ing-issl'), ('пилот', 'pilot'),
                 ('строитель', 'stroitel'),
                 ('экзобиолог', 'ekzobiolog'), ('врач', 'doctor'),
                 ('инженер по терраформированию', 'ing_terraform'),
                 ('климатолог', 'klimatolog'),
                 ('специалист по радиационной защите', 'rad_zash'),
                 ('астрогеолог', 'asterolog'),
                 ('гляциолог', 'glaciolog'),
                 ('инженер жизнеобеспечения', 'ing-jizneob'),
                 ('метеоролог', 'meteorolog'),
                 ('оператор марсохода', 'operator_marsohoda'),
                 ('киберинженер', 'kyber-ing'),
                 ('штурман', 'shturman'), ('пилот дронов', 'pilot_dronov')]
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style_form.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <input type="surname" class="form-control" id="surname" aria-describedby="surnameHelp" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    {'</br>' * 1}
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адресс почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        </br>
                                        <select class="form-control" id="obrSelect" name="obr">
                                          <option>Начальное</option>
                                          <option>Среднее неполное</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Среднее полное</option>
                                          <option>Высшее</option>
                                          <option>-</option>
                                        </select>
                                    </div>
                                    </br>
                                    <div class="form-group">
                                        <label for="professii">Какие у Вас есть профессии?</label>
                                        {"".join([f"""<div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="professii" name="{prof[1]}">
                                            <label class="form-check-label" for="professii">{prof[0]}</label>
                                        </div>""" for prof in prof_list])}
                                    </div>
                                    </br>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="pol" id="male" value="male" checked>
                                          <label class="form-check-label" for="pol">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="pol" id="female" value="female">
                                          <label class="form-check-label" for="pol">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    </br>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="why" rows="3" name="why"></textarea>
                                    </div>
                                    </br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    </br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="ready_to_stay" name="ready">
                                        <label class="form-check-label" for="ready_to_stay">Готовы остаться на Марсе?</label>
                                    </div>
                                    </br>
                                    <button type="send" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        data = {'surname': request.form['surname'], 'name': request.form['name'], 'education': request.form['obr']}
        print('Почта:', request.form['email'])
        professii = []
        for prof in prof_list:
            proff = request.form.get(prof[1], False)
            if proff:
                professii += [prof[0]]
        data['profession'] = professii[0] if len(professii) > 0 else 'нет'
        data['sex'] = request.form['pol']
        data['motivation'] = request.form['why']
        f = request.files['file']
        ready = request.form.get('ready', False)
        ready = ready == 'on'
        data['ready'] = ready
        return answer(data=data)


@app.route('/choice/<planet_name>')
def choice(planet_name):
    data = ['Эта планета близка к Земле;', 'На ней много необходимых ресурсов;',
            'На ней есть вода и атмосфера;',
            'На ней есть небольшое магнитное поле;',
            'Наконец, она просто красива!']
    url_style = url_for('static', filename='css/style.css')
    return '''
<!doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{}"/>
            <title>Варианты выбора</title>
        </head>
        <body>
            <h2>Мое предложение: {}</h2>
            <h3>{}</h3>
            <div class="alert-success" role="alert">
                <br><h3>{}</h3>
            </div>
            <div class="alert-secondary" role="alert">
                <br><h3>{}</h3>
            </div>
            <div class="alert-warning" role="alert">
                <br><h3>{}</h3>
            </div>
            <div class="alert-danger" role="alert">
                <br><h3>{}</h3>
            </div>
        </body>
    </html>'''.format(url_style, planet_name, *data)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    url_style = url_for('static', filename='css/style.css')
    return f'''
<!doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_style}"/>
            <title>Результаты</title>
        </head>
        <body>
            <h2>Результаты отбора</h2>
            <h3>Претендента на участие в миссии {nickname}:</h3>
            <div class="alert-success" role="alert">
                <br><h3>Поздравляем! Ваш рейтинг после {level} этапа отбора</h3>
            </div>
            <h3>составляет {rating}!</h3>
            <div class="alert-warning" role="alert">
                <br><h3>Желаем удачи!</h3>
            </div>
        </body>
    </html>'''


@app.route('/training/<prof>')
def training(prof):
    params = {'prof': prof,
              'img_ing': url_for('static', filename='img/img_ing.png'),
              'img_sim': url_for('static', filename='img/img_sim.png')}
    return render_template('training.html', **params)


@app.route('/list_prof/<list>')
def list_prof(list):
    if list not in ['ol', 'ul']:
        return 'Неверный параметр'
    data = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
            'инженер по терраформированию', 'климатолог',
            'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
            'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода',
            'киберинженер', 'штурман', 'пилот дронов']
    return render_template('prof_list.html', list=list, data=data)


data_default = {'surname': 'Watny', 'name': 'Mark', 'education': 'выше среднего', 'profession': 'штурман марсохода',
                'sex': 'male', 'motivation': 'Всегда хотел застрять на Марсе!', 'ready': True}


@app.route('/answer')
def answer(data=data_default.copy()):
    if data == data_default:
        return auto_answer()
    field_names = ['Фамилия:', 'Имя:', 'Образование:', 'Профессия:', 'Пол:', 'Мотивация:', 'Готовы остаться на Марсе?']
    url_style = url_for('static', filename='css/style_ans.css')
    params = {'title': 'Анкета', 'data': data, 'field_names': field_names, 'url_style': url_style}
    return render_template('auto_answer.html', **params)


@app.route('/auto_answer')
def auto_answer():
    data = data_default.copy()
    field_names = ['Фамилия:', 'Имя:', 'Образование:', 'Профессия:', 'Пол:', 'Мотивация:', 'Готовы остаться на Марсе?']
    url_style = url_for('static', filename='css/style_ans.css')
    params = {'title': 'Анкета', 'data': data, 'field_names': field_names, 'url_style': url_style}
    return render_template('auto_answer.html', **params)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    url_emblem = url_for('static', filename='img/emblem.png')
    url_style_login = url_for('static', filename='css/style_login.css')
    params = {'title': 'Аварийный доступ', 'form': form, 'url_emblem': url_emblem, 'url_style': url_style_login}
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', **params)


@app.route('/distribution')
def distribution():
    url_style = url_for('static', filename='css/style_login.css')
    data = [f'человек_{i}' for i in range(1, 7)]
    params = {'data': data, 'url_style': url_style}
    return render_template('distribution.html', **params)


@app.route('/table/<pol>/<age>')
def table(pol, age):
    url_style = url_for('static', filename='css/style_table.css')
    age = 'young' if int(age) < 21 else 'old'
    emblem = f'img/{age}.png'
    pol = 'red' if pol == 'female' else 'blue'
    color = f'img/{pol}_{age}.png'
    url_color = url_for('static', filename=color)
    url_emblem = url_for('static', filename=emblem)
    params = {'url_style': url_style, 'url_emblem': url_emblem, 'url_color': url_color}
    return render_template('table.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

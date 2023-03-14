from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_astr = StringField('Id астронавта', validators=[DataRequired()])
    password_astr = PasswordField('Пароль астронавта',
                                  validators=[DataRequired()])
    id_kap = StringField('Id капитана', validators=[DataRequired()])
    password_kap = PasswordField('Пароль капитана', validators=[DataRequired()])
    ok = SubmitField('Доступ')


class RegisterForm(FlaskForm):
    log_em = StringField('Login / email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rep_password = PasswordField('Repeat password', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RegisterSuccess(FlaskForm):
    button = SubmitField('Вернуться на главную страницу')


class LoginForm2(FlaskForm):
    email = StringField('Почта/логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('войти')


def hash_password(password):
    hash_dict = {'q': 'ю', 'ю': 'q', 'w': 'б', 'б': 'w', 'e': 'ь', 'ь': 'e',
                 'r': 'т', 'т': 'r', 't': 'и', 'и': 't', 'y': 'м', 'м': 'y',
                 'u': 'с', 'с': 'u', 'i': 'ч', 'ч': 'i', 'o': 'я', 'я': 'o',
                 'p': 'э', 'э': 'p', '[': 'ж', 'ж': '[', ']': 'д', 'д': ']',
                 'a': 'л', 'л': 'a', 's': 'о', 'о': 's', 'd': 'р', 'р': 'd',
                 'f': 'п', 'п': 'f', 'g': 'а', 'а': 'g', 'h': 'в', 'в': 'h',
                 'j': 'ы', 'ы': 'j', 'k': 'ф', 'ф': 'k', 'l': 'ъ', 'ъ': 'l',
                 ';': 'х', 'х': ';', "'": 'з', 'з': "'", 'z': 'щ', 'щ': 'z',
                 'x': 'ш', 'ш': 'x', 'c': 'г', 'г': 'c', 'v': 'н', 'н': 'v',
                 'b': 'е', 'е': 'b', 'n': 'к', 'к': 'n', 'm': 'у', 'у': 'm',
                 ',': 'ц', 'ц': ',', '.': 'й', 'й': '.', 'ё': '`', '`': 'ё',
                 '1': '?', '?': '1', '2': ':', ':': '2', '3': '№', '№': '3',
                 '4': '"', '"': '4', '5': '+', '+': '5', '6': '_', '_': '6',
                 '7': ')', ')': '7', '8': '(', '(': '8', '9': '*', '*': '9',
                 '0': '&', '&': '0', '-': '^', '^': '-', '=': '%', '%': '=',
                 '!': '$', '$': '!', '@': '#', '#': '@'}
    return ''.join([hash_dict.get(i, i) for i in password])


if __name__ == '__main__':
    s1 = 'джфщзьфыьфщхёь0ш23-ш(_"*(7"*(_7№*"_эфюф фзв ф ъ     ъ ХЪХ{}{}[][][][]'
    s2 = "][kz'ekjekz;`e&x:№^x86498)4986)3946pkqk k'h k l     l ХЪХ{}{}жджджджд"
    print(hash_password(s2))

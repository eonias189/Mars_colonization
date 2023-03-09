from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_astr = StringField('Id астронавта', validators=[DataRequired()])
    password_astr = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_kap = StringField('Id капитана', validators=[DataRequired()])
    password_kap = PasswordField('Пароль капитана', validators=[DataRequired()])
    ok = SubmitField('Доступ')

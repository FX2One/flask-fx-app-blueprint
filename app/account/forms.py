from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, ValidationError
from wtforms.validators import Email, InputRequired, Length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Username',
                           validators=[InputRequired()])

    email_address = EmailField('Email', validators=[InputRequired(),
                                                Length(1, 64),
                                                Email()])

    password = PasswordField('Password', validators=[InputRequired(),
                                                 Length(min=6, max=254)])

    confirm = PasswordField('Repeat Password',
                        validators=[InputRequired(),
                                    EqualTo('password')])

    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[InputRequired()])

    password = PasswordField('Password',
                         validators=[InputRequired()])

    submit = SubmitField('Submit')

    
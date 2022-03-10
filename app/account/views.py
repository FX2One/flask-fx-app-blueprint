from flask import Blueprint, render_template
from app.account.forms import RegisterForm, LoginForm

account = Blueprint('account', __name__, template_folder='templates')

@account.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        create_user = User(username=form.username.data)
    return render_template('account/register.html', form=form)

@account.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    return render_template('account/login.html', form=form)
from flask import Blueprint, render_template

account = Blueprint('account', __name__, template_folder='templates')

@account.route('/register')
def register_page():
    return render_template('account/register.html')

@account.route('/login')
def login_page():
    return render_template('account/login.html')
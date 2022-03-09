from flask import Blueprint, render_template

account = Blueprint('account', __name__, template_folder='templates')

@account.route('/home')
def home():
    return render_template('account/home.html')


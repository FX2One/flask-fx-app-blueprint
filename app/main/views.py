from flask import Blueprint, render_template, url_for

main_home = Blueprint('main_home', __name__, template_folder='templates')

@main_home.route('/')
def home_page():
    return render_template('base/home.html')
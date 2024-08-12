from flask import render_template, Blueprint

core_ = Blueprint('core',__name__)

@core_.route('/')
def index():
    return render_template('index.html')


@core_.route('/about-us')
def about_us():
    return render_template('about_us.html')

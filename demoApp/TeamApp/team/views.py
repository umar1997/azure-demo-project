from flask import (
    Blueprint,
    render_template
)
from TeamApp import db
from TeamApp.models import User

team_ = Blueprint('team',__name__)

@team_.route('/team', methods=['POST', 'GET'])
def show_members():
    members = User.query.order_by(User.age.desc()).all()
    return render_template('team_members.html', members = members)
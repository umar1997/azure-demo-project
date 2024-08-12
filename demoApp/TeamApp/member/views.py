from flask import (
    url_for, 
    flash, 
    redirect, 
    Blueprint,
    render_template
)
from TeamApp import db
from TeamApp.models import User
from TeamApp.member.forms import AddMemberForm

member_ = Blueprint('member',__name__)

@member_.route('/member/add-member', methods=['POST', 'GET'])
def add_member():
    form = AddMemberForm()

    users = User.query.all()
    form.reports_to.choices = [(usr.email_id, usr.email_id) for usr in users]
    form.reports_to.choices += [("-", "-")]
    age = form.age.data if form.age.data is not None else None
    if form.validate_on_submit():
        user = User(
                name=form.name.data,
                email=form.email.data,
                gender=form.gender.data,
                age=age,
                position=form.position.data, 
                reports_to=form.reports_to.data
            )
        db.session.add(user)
        db.session.commit()
        flash(f'Team Member {user.name} added!', 'success')
        return redirect(url_for('member.member_profile', email_id=user.email_id))
    
    return render_template('member_add.html', form=form)


@member_.route("/member/<email_id>", methods=['GET'])
def member_profile(email_id):
    user = User.query.filter_by(email_id=email_id).first_or_404()
    return render_template('member_profile.html', member=user)


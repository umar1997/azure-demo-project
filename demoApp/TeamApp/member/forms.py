from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, RadioField, SelectField
from wtforms.validators import DataRequired, Email, ValidationError, Optional

from TeamApp.models import User


class AddMemberForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    name = StringField('Full Name', validators=[DataRequired()])
    gender = RadioField(
        'Gender',
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female')
        ],
        validators=[DataRequired()]
    )
    age = IntegerField('Age', validators=[Optional()])
    position = StringField('Position Title', validators=[DataRequired()])
    reports_to = SelectField('Reports To', choices=[], validators=[DataRequired()])
    submit = SubmitField('Add Member')

    def validate_email(self, field):
        if not field.data.endswith("@m42.ae"):
            flash(f'Only M42 emails are allowed to be added! {field.data} isn\'t a company email!', 'info')
            raise ValidationError('A team member with email ouside company is trying to be added!')
        elif User.query.filter_by(email=field.data).first():
            flash(f'Team Member with email id {field.data} already exists!', 'danger')
            raise ValidationError('A team member with this email has already been added!')


from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField
from wtforms.validators import Optional





class SettingDateForm(FlaskForm):
    next_meeting_date = DateField("Prochaine réunion",format="%d-%m-%Y", validators=[Optional()])  # permite que quede vacío)
    submit = SubmitField("Enregistrer")
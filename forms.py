from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField
from wtforms.validators import DataRequired, Length


class DonorForm(FlaskForm):
    donor = StringField(
        'Donor Name',
        validators=[DataRequired(),
                    Length(min=1)])
    amount = StringField('Donation', DataRequired())
    submit = SubmitField('Add Donation!')

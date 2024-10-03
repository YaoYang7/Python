from flask_wtf import FlaskForm 
from wtforms import SubmitField, StringField, IntegerField, RadioField, FloatField
from wtforms.validators import InputRequired, NumberRange

class GuessForm(FlaskForm):
    guess = IntegerField("Enter a number between 1 and 100, including 1 and 100:", 
                          validators=[InputRequired(), NumberRange(1, 100)])
    submit = SubmitField("Submit")
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired

class RPSForm(FlaskForm):
    rock = SubmitField(label='rock')
    paper = SubmitField(label='paper')
    scissor = SubmitField(label='scissor')
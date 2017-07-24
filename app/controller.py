from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class BucketListRegisterForm(FlaskForm):
    '''form for handling registration'''
    user-name = StringField ( 'username', validators = )
   
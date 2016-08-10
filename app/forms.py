import pytz
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, IntegerField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Required

class QueryForm(Form):
    name = StringField('name', validators=[DataRequired()])
    start = DateTimeField(
        'Start', format="%Y-%m-%dT%H:%M:%S",
        default=datetime.today
    )
    end = DateTimeField(
        'End', format="%Y-%m-%dT%H:%M:%S",
    )
    host = StringField('Host')
    net = StringField('Host')
    ipproto = IntegerField('Protocol')
    port = IntegerField('Port')

class Download(Form):
    submit = SubmitField('Download')

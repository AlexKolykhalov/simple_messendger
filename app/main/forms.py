from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, TextField, HiddenField, FileField
from wtforms.validators import DataRequired, Email


class DisqusForm(FlaskForm):
    message    = TextAreaField('Your message', id='message_data', validators=[DataRequired()])
    submit     = SubmitField('Send')

class EditForm(FlaskForm):
    username    = StringField('Username', validators=[DataRequired()])
    email       = StringField('Email', validators=[DataRequired(), Email()])
    url_avatar  = ('Url avatar')  
    submit      = SubmitField('Submit')

class UploadForm(FlaskForm):    
    photo    = FileField('Choose your new photo', validators=[DataRequired()])
    submit   = SubmitField('Submit')

# class TestSocketIO_Emit(FlaskForm):    
#     message         = TextField('', id='emit_data', render_kw={'placeholder': 'Message'})
#     message_button  = SubmitField('Echo')

# class TestSocketIO_BroadCast(FlaskForm):
#     message_broadcast   = TextField('', id='broadcast_data', render_kw={'placeholder': 'Message'})
#     broadcast_button    = SubmitField('Broadcast')


    # roomname_join   = TextField('', render_kw={"placeholder": "Room name"})
    # join_button     = SubmitField('Join Room')
 
    # roomname_leave  = TextField('', render_kw={"placeholder": "Room name"})
    # leave_button    = SubmitField('Leave Room')
 
    # roomname_send = TextField('', render_kw={"placeholder": "Room name"})
    # message_send =  TextField('', render_kw={"placeholder": "Message"}) 
    # send_to_room = SubmitField('Send to Room')

    # roomname_close = TextField('', render_kw={"placeholder": "Room name"})
    # close_room = SubmitField('Close Room')

    # disconnect = SubmitField('Disconnect')
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, TextField, FormField
from wtforms.validators import DataRequired


class DisqusForm(FlaskForm):
    message    = TextAreaField('Your message', id='message_data', validators=[DataRequired()])
    submit     = SubmitField('Send')

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
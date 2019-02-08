from app import db
from app.models import User, Message
from app.main import bp
from app.main.forms import DisqusForm
from flask import render_template, redirect, url_for, flash, session, request
from flask_login import current_user, fresh_login_required

# from messenger import socketio
# from flask_socketio import emit, join_room, leave_room, close_room, rooms, disconnect
# from threading import Lock

# thread_lock = Lock()
# thread = None

@bp.route('/')
@bp.route('/index')
@fresh_login_required
def index():        
    all_users = User.query.all()
    return render_template('index.html', users=all_users)
    # form = TestSocketIO_Emit()
    # form1 = TestSocketIO_BroadCast()
    # return render_template('index.html', form=form, form1=form1)
    # return render_template('index1.html')

@bp.route('/talk/<int:id>', methods=['get', 'post'])
@fresh_login_required
def talk(id):
    form = DisqusForm()
    if form.validate_on_submit():        
        message = Message()
        message.body = form.message.data
        message.sender_id = current_user.id
        message.recipient_id = id
        db.session.add(message)
        db.session.commit()        
        return redirect(url_for('main.talk', id=id))        
    messages = current_user.messeges_send
    return render_template('talking_room.html', form=form, messages=messages)
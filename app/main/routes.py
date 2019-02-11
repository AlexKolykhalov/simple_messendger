from app import db, images
from app.models import User, Message
from app.main import bp
from app.main.forms import DisqusForm, EditForm, UploadForm
from flask import render_template, redirect, url_for, flash, session, request
from flask_login import current_user, fresh_login_required


@bp.route('/')
@bp.route('/index')
@fresh_login_required
def index():        
    all_users = User.query.all()
    return render_template('index.html', user=current_user, users=all_users)    
    # return render_template('index1.html')

@bp.route('/profile', methods=['get', 'post'])
@fresh_login_required
def profile():
    form = EditForm()    
    if form.validate_on_submit():
        count_of_same_data = User.query.filter((User.username==form.username.data) & (User.email==form.email.data)).count()
        if count_of_same_data == 1:        
            flash('Your profile has been edited', 'alert-success')            
        else:
            user            = User.query.get(current_user.id)
            user.username   = form.username.data
            user.email      = form.email.data
            try:
                db.session.commit()
                flash('Your profile has been edited', 'alert-success')
            except:
                flash('Another user has same username or email', 'alert-danger')            
        return redirect(url_for('main.profile'))
    if request.method == 'GET':
        form.username.data   = current_user.username
        form.email.data      = current_user.email
        if current_user.url_photo == None:
            url_photo = current_user.avatar(128)
        else:
            url_photo = current_user.url_photo
        form.url_avatar      = url_photo
    return render_template('main/profile.html', form=form)

@bp.route('/upload', methods=['get', 'post'])
@fresh_login_required
def upload():
    if request.method == 'POST':
        filename    = images.save(request.files['photo'])
        url_photo   = images.url(filename)
        user = User.query.get(current_user.id)
        user.url_photo = url_photo
        try:
            db.session.commit()
            flash('Photo uploaded', 'alert-success')
        except:
            flash('Photo did not load', 'alert-danger')        
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form = UploadForm()
        return render_template('main/upload.html', form=form)

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
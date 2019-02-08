from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user
from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm
from app.models import User
from werkzeug.urls import url_parse


@bp.route('/login', methods=['get', 'post'])
def login():    
    if current_user.is_authenticated:        
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():        
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password!', 'alert-danger')
            return redirect(url_for('auth.login'))
        login_user(user, remember=True)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('auth/login.html', form=form)

@bp.route('/refresh')
def refresh():    
    logout_user()
    return redirect(url_for('auth.login'))

@bp.route('/register', methods=['get', 'post'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))        
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        user.username       = form.username.data
        user.email          = form.email.data
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you’re registered!", 'alert-success')
        redirect(url_for('auth.login'))
    return render_template('auth/registration.html', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
from datetime import datetime
from flask_login import UserMixin
from app import login_manager, db
from werkzeug.security import check_password_hash, generate_password_hash
from hashlib import md5


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id                      = db.Column(db.Integer, primary_key=True) 
    username                = db.Column(db.String(60), index=True, unique=True)
    email                   = db.Column(db.String(60), index=True, unique=True)
    password_hash           = db.Column(db.String(128))
    url_photo               = db.Column(db.String, default=None, nullable=True)
    last_message_read_time  = db.Column(db.DateTime)    

    #relationships
    messeges_send       = db.relationship('Message', foreign_keys='Message.sender_id', backref='author', lazy='dynamic')
    messages_received   = db.relationship('Message', foreign_keys='Message.recipient_id', backref='recipient', lazy='dynamic')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def count_unreaded_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        return Message.query.filter_by(recipient=self).filter(Message.timestamp > last_read_time).count()

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)    

class Message(db.Model):
    __tablename__ = 'message'
    
    id            = db.Column(db.Integer, primary_key=True) 
    body          = db.Column(db.String(300))
    sender_id     = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id  = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp     = db.Column(db.DateTime, index=True, default=datetime.utcnow)

# initialize 
@login_manager.user_loader
def load_user(id):    
    return User.query.get(int(id))
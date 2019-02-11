import os


class Config(object):   
    SECRET_KEY                      = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI         = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS  = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    UPLOADS_DEFAULT_DEST            = os.environ.get('UPLOADS_DEFAULT_DEST')
    UPLOADED_IMAGES_DEST            = os.environ.get('UPLOADED_IMAGES_DEST')
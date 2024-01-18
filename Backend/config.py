import os
basedir = os.path.abspath(os.path.dirname(__file__))
postgrespass = os.environ.get('postgresepass')
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql+psycopg2://apoebqvc:'+postgrespass+'@hansken.db.elephantsql.com/apoebqvc'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
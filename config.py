import os 

class Config(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    TESTING = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True

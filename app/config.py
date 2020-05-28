import os
import urllib
basedir=os.path.abspath(os.path.dirname(__file__))

class Config():

    #bcrypt settings
    SECRET_KEY=b'f0f05d31b4d0bfaf649ce4bbcfa72af85bcc7ab18aaab183'
    #for production use environment variable
    #os.environ.get('APP_SECRET')
    SQLALCHEMY_TRACKMODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='sqlite:////Users ' 
import os
class Config:

   UPLOADED_PHOTOS_DEST ='app/static/photos' 
   SECRET_KEY = os.environ.get('SECRET_KEY')
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fahadbasi:333@localhost/pitch' 
   DEBUG = True

#    email configurations
   MAIL_SERVER = 'smtp.googlemail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
   MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") 


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://etujabyelnapni:b9c669f5b422bd5ecaf5c5d1b2525a6c4486aca6104c1b3ebe824f3f69b0f223@ec2-54-80-123-146.compute-1.amazonaws.com:5432/ddvmm40s6dnpbr' 
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    

    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fahadbasi:333@localhost/pitch'
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fahadbasi:333@localhost/pitch_test'
        


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}  
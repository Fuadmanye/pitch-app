import os
class Config:

   UPLOADED_PHOTOS_DEST ='app/static/photos' 
   SECRET_KEY = os.environ.get('SECRET_KEY')
#    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fahadbasi:333@localhost/pitch' 
  

#    email configurations
   MAIL_SERVER = 'smtp.googlemail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
   MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") 


class ProdConfig(Config):
      
      SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("://", "ql://", 1)  
   
    
    

    
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
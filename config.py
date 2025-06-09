

class Config: 
  DEBUG = False

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root123456@localhost/flask-template'

  SQLALCHEMY_TRACK_MODIFICATIONS = False

  JWT_SECRET_KEY = 'your key'

class DevelopmentConfig(Config):
  DEBUG = True


class ProductionConfig(Config):
  DEBUG = False
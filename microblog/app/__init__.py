#  just an init file

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask("app")
# app.config.from_object('config')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)

# from app import views, models

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists

import os

load_dotenv()
APP_SECRET_KEY = os.getenv('APP_SECRET_KEY') 
DB_NAME = os.getenv('DB_NAME') 
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_URI = f'mysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_NAME}'

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = APP_SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    db.init_app(app)
    
    from .HTTPEndpoints.auth import auth
    
    
    app.register_blueprint(auth, url_prefix='/')
    
    create_database(app)
    
    return app

def create_database(app):
    if not database_exists(DB_URI):
        db.create_all(app=app)
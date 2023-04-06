from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
APP_SECRET_KEY = os.getenv('APP_SECRET_KEY') 

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = APP_SECRET_KEY
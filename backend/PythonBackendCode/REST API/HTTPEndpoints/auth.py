from flask import Blueprint, jsonify, request, Response, abort
from ..Schemas.User_model import User, db

auth = Blueprint('auth', __name__)

@auth.route('/login',endpoint='login', methods=["POST"])
def login():
    data = request.form
    return jsonify({"test":"login"})

@auth.route('/logout',endpoint='logout')
def logout():
    return jsonify({"test":"logout"})

@auth.route('/signup',endpoint='signup')
def signup():
    try:
        if request.method == 'POST':
            email = request.form.get('email')
            name = request.form.get('name')
            password = request.form.get('password')
            new_user = User(email=email, name=name, password=password)
            db.session.add(new_user)
            db.session.commit()
            session_token = None
            refresh_token = None
            return jsonify({"session_token": session_token, "refreshToken" : refresh_token}), 201 
    except:
        return abort(500)
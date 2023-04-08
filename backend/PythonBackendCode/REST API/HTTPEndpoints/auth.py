from flask import Blueprint, jsonify

auth = Blueprint('auth', __name__)

@auth.route('/login',endpoint='login', methods=["POST"])
def login():
    return jsonify({"test":"login"})

@auth.route('/logout',endpoint='logout')
def logout():
    return jsonify({"test":"logout"})

@auth.route('/signup',endpoint='signup')
def signup():
    return jsonify({"test":"signup"})
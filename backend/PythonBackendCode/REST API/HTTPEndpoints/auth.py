from flask import Blueprint, jsonify, request

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
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
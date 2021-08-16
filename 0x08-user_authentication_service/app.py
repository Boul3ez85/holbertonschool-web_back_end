#!/usr/bin/env python3
"""route module for API"""

from auth import Auth
from flask import Flask, jsonify, request


app = Flask(__name__)

AUTH = Auth()


@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """implements the POST /users route."""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        check_user = AUTH.register_user(email, password)
        if check_user:
            return jsonify({"email": email, "message": "user created"})

    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
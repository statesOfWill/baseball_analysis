import os

import flask
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, worldy world!"

app.run(host='0.0.0.0', port=8080)
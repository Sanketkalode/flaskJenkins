from flask import Flask, jsonify
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app = Flask(__name__)

app.config['SECRET_KEY'] = 'test'
xray_recorder.configure(service='My application')
XRayMiddleware(app, xray_recorder)


@app.route('/')
def home():
    return jsonify(message='Welcome to flask app')


@app.route('/<string>')
def reverse_string(string):
    data = string[::-1]
    return jsonify(reverse_string=data)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')

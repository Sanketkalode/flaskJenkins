from flask import Flask, jsonify

app = Flask(__name__)

app.config['SECRET_KEY'] = 'test'


@app.route('/')
def home():
    return jsonify(message='Welcome to flask app')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')

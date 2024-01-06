from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.before_request
def check_get():
    if request.method != 'GET':
        return 'This API only supports GET requests'


@app.route('/', methods=['GET'])
def index():
    r = requests.get('https://official-joke-api.appspot.com/random_joke')
    if r.status_code == 200:
        joke = r.json()
        return jsonify({'punchline_id': joke['id'], 'punchline': joke['punchline']})
    else:
        return 'Request failed, error code', r.status_code


if __name__ == '__main__':
    app.run()

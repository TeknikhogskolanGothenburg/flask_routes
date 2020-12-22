from view import app
from flask import request
import json

@app.route('/', methods=['POST'])
def index_post():
    data = request.data
    python_data = json.loads(data)
    out_data = {
        'result': 'this was fun',
        'the things i got was': python_data['things']
    }

    response = app.response_class(
        response=json.dumps(out_data),
        status=299,
        mimetype='application/json'
    )
    return response


@app.route('/json')
def index_json():
    out_data = {
        "hello": "hepp",
        "value": 45
    }
    response = app.response_class(
        response=json.dumps(out_data),
        status=200,
        mimetype='application/json'
    )
    return response

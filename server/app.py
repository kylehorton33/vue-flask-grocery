import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS


ITEMS = [
    {
        'id': uuid.uuid4().hex,
        'name': 'apple',
        'category': 'produce',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'milk',
        'category': 'dairy',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'flour',
        'category': 'baking',
        'read': True
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_item(item_id):
    for item in ITEMS:
        if item['id'] == item_id:
            ITEMS.remove(item)
            return True
    return False


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/items', methods=['GET', 'POST'])
def all_items():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        ITEMS.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'category': post_data.get('category'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Item added!'
    else:
        response_object['items'] = ITEMS
    return jsonify(response_object)


@app.route('/items/<item_id>', methods=['PUT', 'DELETE'])
def single_item(item_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_item(item_id)
        ITEMS.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'category': post_data.get('category'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Item updated!'
    if request.method == 'DELETE':
        remove_item(item_id)
        response_object['message'] = 'Item removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
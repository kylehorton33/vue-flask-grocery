import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grocery_list.db'
db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)

class Item(db.Model):
    __tablename__ = 'grocery_list'
    __table_args__ = { 'extend_existing': True }
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, primary_key=False)
    category = db.Column(db.Text, primary_key=False)

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
        item = Item(
            name = post_data.get('name'),
            category = post_data.get('category'),
        )
        db.session.add(item)
        db.session.commit()

        response_object['message'] = 'Item added!'
    else:
        ITEMS = []
        for item in Item.query.all():
            ITEMS.append(
                {
                    "id": item.id,
                    "name": item.name,
                    "category": item.category,
                    "read": True,
                }
            )
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
    app.run(host='0.0.0.0', port=5000)
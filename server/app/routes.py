from app import app, db
from flask import jsonify, request
from app.models import Item, Category
from flask_cors import CORS

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

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
        )
        db.session.add(item)
        db.session.commit()

        response_object['message'] = 'Item added!'
    else:
        ITEMS = []
        for i, category in enumerate(Category.query.all()):
            ITEMS.append({
                "category":category.name,
                "items": [],
            })
            for item in category.items:
                ITEMS[i]["items"].append({
                    "id": item.id,
                    "name": item.name,
                    "category": item.category.name,
                })
        response_object['items'] = ITEMS
    return jsonify(response_object)


@app.route('/items/<item_id>', methods=['PUT', 'DELETE'])
def single_item(item_id):
    response_object = {'status': 'success'}
    item = Item.query.filter_by(id=int(item_id)).first()

    if request.method == 'PUT':
        post_data = request.get_json()        
        item.name = post_data.get('name')
        item.category = post_data.get('category')
        db.session.commit()
        response_object['message'] = 'Item updated!'
    if request.method == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        response_object['message'] = 'Item removed!'
    return jsonify(response_object)
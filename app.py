from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize the app, database, and marshmallow
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Item model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))

    def __init__(self, name, description):
        self.name = name
        self.description = description

# Define the Item schema
class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Home route
@app.route('/')
def home():
    return "Welcome to the Item Management API!"

# Implement CRUD operations
@app.route('/item', methods=['POST'])
def add_item():
    name = request.json['name']
    description = request.json['description']
    new_item = Item(name, description)
    db.session.add(new_item)
    db.session.commit()
    return item_schema.jsonify(new_item)

@app.route('/item', methods=['GET'])
def get_items():
    all_items = Item.query.all()
    result = items_schema.dump(all_items)
    return jsonify(result)

@app.route('/item/<id>', methods=['GET'])
def get_item(id):
    item = Item.query.get(id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    return item_schema.jsonify(item)

@app.route('/item/<id>', methods=['PUT'])
def update_item(id):
    item = Item.query.get(id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    item.name = request.json['name']
    item.description = request.json['description']
    db.session.commit()
    return item_schema.jsonify(item)

@app.route('/item/<id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get(id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    db.session.delete(item)
    db.session.commit()
    return item_schema.jsonify(item)

if __name__ == '__main__':
    app.run(debug=True)

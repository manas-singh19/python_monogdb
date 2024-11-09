from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import importlib
import os

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/your_database"
mongo = PyMongo(app)

# Directory for schema files
SCHEMA_DIR = "schemas"

# Helper function to load schema
def load_schema(schema_name):
    schema_path = os.path.join(SCHEMA_DIR, f"{schema_name}_schema")
    try:
        schema_module = importlib.import_module(f"{SCHEMA_DIR}.{schema_name}_schema")
        return getattr(schema_module, f"{schema_name}_schema")
    except (ImportError, AttributeError) as e:
        print(f"Error loading schema: {e}")
        return None

# Example route for adding a user
@app.route('/add_user', methods=['POST'])
def add_user():
    schema = load_schema("user")
    if not schema:
        return jsonify({"error": "Schema not found"}), 400

    data = request.json
    # Here you can add validation logic based on schema
    
    result = mongo.db.users.insert_one(data)
    return jsonify({"message": "User added", "id": str(result.inserted_id)})

# Example route for adding a product
@app.route('/add_product', methods=['POST'])
def add_product():
    schema = load_schema("product")
    if not schema:
        return jsonify({"error": "Schema not found"}), 400

    data = request.json
    # Add validation logic if necessary based on schema
    
    result = mongo.db.products.insert_one(data)
    return jsonify({"message": "Product added", "id": str(result.inserted_id)})

if __name__ == '__main__':
    app.run(debug=True)
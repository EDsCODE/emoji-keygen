from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from src.emoji_encoder import encode, decode
from src.crypto import generate_new_address, encrypt
from src.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from src.models import db, PrivateKey
from src.repo import get_all, add_instance, get


def create():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    CORS(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


app = create()


# Description: Test endpoint to view all database data and see how information is stored
@app.route('/all')
def hello():
    keys = get_all(PrivateKey)
    all_keys = []
    for key in keys:
        new_key = {
            "hash_key": key.hash_key,
            "name": key.name,
        }

        all_keys.append(new_key)
    return json.dumps(all_keys), 200

# Description: Accepts a name and generates a new address that's encoded in emojis
# Params: name (String)
# Return: emoji string (String)
@app.route('/new', methods=["POST"])
def generate_address():
    data = request.json
    name = data["name"]

    # generate an address and incode
    new_address = generate_new_address()
    encoded_address = encode(new_address)

    # encrypt and save into database with name
    encrypted_address = encrypt(new_address)
    add_instance(PrivateKey, hash_key=encrypted_address, name=name)

    return jsonify(original_address=new_address, encoded=encoded_address), 200

# Description: Accepts an emoji string and returns name associated with encoded address
# Params: emoji String (String)
# Return: name (String)
@app.route('/decode', methods=["GET"])
def decode_address():
    encoded_sequence = request.args.get('key')

    # decode emoji encoding and use query using hash
    decoded_sequence = decode(encoded_sequence)
    encrypted_address = encrypt(decoded_sequence)
    result = get(PrivateKey, encrypted_address)

    # return associated name if match exists otherwise return error
    if result is None:
        return jsonify({'error': 'No Associated Key'}), 404
    return jsonify(decoded_address=result.name), 200


if __name__ == '__main__':
    app.run()

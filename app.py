from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#Hack-1
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'payload': 'success'})


#Hack-2
@app.route('/user', methods=['POST'])
def post_user():
    return jsonify({'payload': 'success'})


#Hack-3
@app.route('/user', methods=['DELETE'])
def delete_user():
    return jsonify({'payload': 'success'})


#Hack-4
@app.route('/user', methods=['PUT'])
def put_user():
    return jsonify({'payload': 'success', 'error': False})


#Hack-5
@app.route('/api/v1/users', methods=['GET'])
def get_users_v1():
    return jsonify({'payload': []})


#Hack-6
@app.route('/api/v1/user', methods=['POST'])
def post_user_v1():
    email = request.args.get('email')
    name = request.args.get('name')
    return jsonify({'payload': {'email': email, 'name': name}})


#Hack-7
@app.route('/api/v1/user/add', methods=['POST'])
def add_user():
    email = request.form.get('email')
    name = request.form.get('name')
    user_id = request.form.get('id')
    return jsonify({'payload': {'email': email, 'name': name, 'id': user_id}})



#Hack-8
@app.route('/api/v1/user/create', methods=['POST'])
def create_user():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    user_id = data.get('id')
    return jsonify({'payload': {'email': email, 'name': name, 'id': user_id}})

if __name__ == "__main__":
    app.run(debug=True)
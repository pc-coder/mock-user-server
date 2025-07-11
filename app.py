from flask import Flask, jsonify, request, abort

app = Flask(__name__)

users = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid input"}), 400
    user_id = max(users.keys()) + 1
    user = {"id": user_id, "name": data['name'], "email": data['email']}
    users[user_id] = user
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    user = users[user_id]
    user.update({k: v for k, v in data.items() if k in ['name', 'email']})
    return jsonify(user), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

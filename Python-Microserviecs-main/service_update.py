from flask import Flask, request, jsonify
import data_user as us

app = Flask(__name__)

# Find and update data in json
def _update_user(user, new_user, username):
    for x in username:
        if x["user"] == user:
            x["user"] = new_user
            return True
    return False

@app.route('/update', methods=['POST'])
def update():
    # Get the user's login information from the request
    username = request.form.get('username')
    password = request.form.get('password')
    new_username = request.form.get('new_username')

    _user = us.find_username(username)
    data = [x for x in _user if x["user"]==username and x["password"]==password]
    if data:
        us.update_user(username,password,new_username)
        return jsonify({'message': 'Update successfully.'}), 200
    else:
        return jsonify({'message': 'Fail to update'}), 401

    # if data:
    #     updated = _update_user(username, new_username, _user)
    #     if updated:
    #         return jsonify({'message': 'Update successfully.'}), 200
    #     else:
    #         return jsonify({'message': 'User not found.'}), 404
    # else:
    #     return jsonify({'message': 'Invalid username or password.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
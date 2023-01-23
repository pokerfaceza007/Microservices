from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
#import jwt
import data_user as us

app = Flask(__name__)

# username = us.user_name()

# Find data in json
# # def _find_user(user, username):
#     data = [x for x in username if x["user"]==user]
#     return data

@app.route('/username', methods=['GET'])
def user():
    _user = us.user_name()
    return jsonify(_user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True) #127.0.0.1
from flask import  Flask, request, jsonify
from flask_cors import CORS


app= Flask(__name__)
cors = CORS(app, origins='*')

@app.route('/', methods=['GET'])
def hello():
    return 'Welcome to EarlyBird server!'

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({'users': [{"name":'jack', "id": 1}, {"name":'john', "id": 2}, {"name":'doe', "id": 3}]})

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8080)

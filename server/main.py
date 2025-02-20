from flask import  Flask, request, jsonify
from flask_cors import CORS
from spotify import get_token, get_artists

from db import Artist, Session

token = get_token()
artist_info =get_artists(token, 'BTS')
# print("artist_info", artist_info)


# parse artist_info and insert to the Artist db
session = Session()

for artist in artist_info:
    artist = Artist(
        id=artist['id'],
        name=artist['name'],
        genre=artist['genres'][0],
        image_url=artist['images'][0]['url']
    )
    session.add(artist)

session.commit()
session.close()


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


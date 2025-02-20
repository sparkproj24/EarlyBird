from dotenv import load_dotenv
import os
import base64
import requests

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


# documentation reference: https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_byte = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_byte), "utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
    }
    data = {
        "grant_type": "client_credentials",
    }
    response = requests.post(url, headers=headers, data=data)
    json = response.json()
    access_token = json["access_token"]
    return access_token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def get_artists(token, artist_name):
    base_url = "https://api.spotify.com/v1/search?"
    query = f"q={artist_name}&type=artist&limit=1"
    url = base_url + query

    headers = get_auth_header(token)
    response = requests.get(url, headers=headers)
    json = response.json()
    artist_info = json["artists"]["items"]
    return artist_info

# sample response from get_artists
# res = [
#     {
#         "external_urls": {
#             "spotify": "https://open.spotify.com/artist/3Nrfpe0tUJi4K4DXYWgMUX"
#         },
#         "followers": {"href": None, "total": 77931560},
#         "genres": ["k-pop"],
#         "href": "https://api.spotify.com/v1/artists/3Nrfpe0tUJi4K4DXYWgMUX",
#         "id": "3Nrfpe0tUJi4K4DXYWgMUX",
#         "images": [
#             {
#                 "url": "https://i.scdn.co/image/ab6761610000e5ebd642648235ebf3460d2d1f6a",
#                 "height": 640,
#                 "width": 640,
#             },
#             {
#                 "url": "https://i.scdn.co/image/ab67616100005174d642648235ebf3460d2d1f6a",
#                 "height": 320,
#                 "width": 320,
#             },
#             {
#                 "url": "https://i.scdn.co/image/ab6761610000f178d642648235ebf3460d2d1f6a",
#                 "height": 160,
#                 "width": 160,
#             },
#         ],
#         "name": "BTS",
#         "popularity": 86,
#         "type": "artist",
#         "uri": "spotify:artist:3Nrfpe0tUJi4K4DXYWgMUX",
#     }
# ]

import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from urllib.parse import urlencode
import base64
import webbrowser 
import json
import pandas as pd
import csv

CLIENT_ID = "ca7fbe12e14546cb94ec1ec90c536bce"
CLIENT_SECRET = "2a21c07b2a1d4acea157cb60de098142"


new_list = []
grant_type = 'client_credentials'
body_params = {'grant_type' : grant_type}
csvheaders = ["Song Name", "Artists", "Genre"]

url='https://accounts.spotify.com/api/token'
response = requests.post(url, data=body_params, auth = (CLIENT_ID, CLIENT_SECRET)) 

access_token = response.json().get('access_token')

base_url = 'https://api.spotify.com/v1/users/x5raulz6ufun7mia2v0s6oqeq/playlists/4X8mtKyMYDYdvm2R0RfQvc/' 

headers = {
    'Authorization': 'Bearer {}'.format(access_token)
    
}

response = requests.get(base_url,headers=headers).json()
play = response['tracks']['items']   #['track']-->['album']-->['artists']-->['name']








#Songs
for j in play:
    print(j['track']['name'])

#Artists
for j in play:
    listings = [j['track']['album']['artists']]
    for s in listings:
        artists = [s[0]['name']]
        new_list.add(artists)


#Genres
for j in play:
    artist = [j['track']['album']['artists']]
    for g in artist:
        genre = g[0]['href']
        response2 = requests.get(genre,headers=headers).json()
        genre_1 = response2['genres']
        new_list.append(genre_1)        
        genre_list = ','.join(str(v) for v in new_list)  


'''

#Popularity
for j in play:
    artist = [j['track']['album']['artists']]
    for g in artist:
        genre = g[0]['href']
        response2 = requests.get(genre,headers=headers).json()
        genre_1 = response2['popularity']
        new_list.append(genre_1)        
        genre_list = ','.join(str(v) for v in new_list)  




response2 = requests.get(genre,headers=headers).json()

genre_1 = response2['genres']
        
print(type(genre_1))



for gx in genre_1:
    print(gx)


    artist_name = j["track"]["artists"][0]["name"]
    artist_pop = j["popularity"]
    artist_genres = j["genres"]


print(artist_genres)


create a pretty table object
tableobj = []
csvheaders = ["currency_name","currency_symbol", "price", "percent_change_24h", "percent_change_7d", "percent_change_30d"]


client_id = "ca7fbe12e14546cb94ec1ec90c536bce"
client_secret = "2a21c07b2a1d4acea157cb60de098142"
code = "AQDLT6t6T4U-iyBn_jTsjZ5POsz3ivxhujXRQsB8weVeobUuhoN6myAJ2xYFWqhPSaIyZgzlP5dMsxOxyalcy5SqQWgETsi5jZ1beBXv0Ie9knOIZ-3M52xRtN8otQ9Jinvwk-CpZOXh963QXg65CQC8Ncx-bF8dCGnMP-ns-JvS5m-bnxWSy1J0aNQgnuLpXH1xoV0"

auth_headers = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": "http://localhost:7777/callback",
    "scope": "user-library-read"
}

#webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded"
}


token_data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": "http://localhost:7777/callback"
}

r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers).json()



token = r.json()["access_token"]

user_headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json"
}

user_params = {
    "limit": 50
}

user_tracks_response = requests.get("https://api.spotify.com/v1/me/tracks", params=user_params, headers=user_headers)

print(user_tracks_response.json())




'''
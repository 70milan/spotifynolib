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
csvheaders = ["Artists"]

url='https://accounts.spotify.com/api/token'
response = requests.post(url, data=body_params, auth = (CLIENT_ID, CLIENT_SECRET)) 

access_token = response.json().get('access_token')

base_url = 'https://api.spotify.com/v1/users/x5raulz6ufun7mia2v0s6oqeq/playlists/4CPdJAFwZhgik31FK76Pow/' 

headers = {
    'Authorization': 'Bearer {}'.format(access_token)
    
}

response = requests.get(base_url,headers=headers).json()

play = response['tracks']['items']   #['track']-->['album']-->['artists']-->['name']



#to get the artists

for j in play:
    listings = [j['track']['album']['artists']]
    for s in listings:
        artists = [s[0]['name']]
        new_list.append(artists)



with open('C:/projects/Data Engineering/py/apicalls/spotify/my_artists.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csvheaders)
    writer.writerows(new_list)






'''create a pretty table object
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
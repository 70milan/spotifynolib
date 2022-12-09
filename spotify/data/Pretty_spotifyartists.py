import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from prettytable import PrettyTable


CLIENT_ID = "ca7fbe12e14546cb94ec1ec90c536bce"
CLIENT_SECRET = "2a21c07b2a1d4acea157cb60de098142"


new_list = []
tableObj = PrettyTable()

grant_type = 'client_credentials'
body_params = {'grant_type' : grant_type}

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
        tableObj.add_row([artists])


tableObj.field_names = ["artist"]









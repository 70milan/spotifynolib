import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from urllib.parse import urlencode
import base64
import webbrowser 
import json
import pandas as pd
import csv

CLIENT_ID = "ca7fbe12e14546cb94ec1ec90c536bce"
CLIENT_SECRET = "f660057e1ba2440dae9b3dbe4a9d67aa"




#

song_list =[]
artist_list = []
genre_list = []
grant_type = 'client_credentials'
body_params = {'grant_type' : grant_type}

url='https://accounts.spotify.com/api/token'
response = requests.post(url, data=body_params, auth = (CLIENT_ID, CLIENT_SECRET)) 

access_token = response.json().get('access_token')

base_url = 'https://api.spotify.com/v1/users/x5raulz6ufun7mia2v0s6oqeq/playlists/4CPdJAFwZhgik31FK76Pow'

csvheaders = ['song_name','artist_name','Genre']
#4CPdJAFwZhgik31FK76Pow/' 

headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

response = requests.get(base_url,headers=headers).json()


play1 = response['tracks']['items'] 


play1 = response['items']   #['track']-->['album']-->['artists']-->['name']
#genre
for j in play1:
    s_n = [j['track']['name']]
    song_name = ', '.join(str(v) for v in s_n) 
    song_list.append(song_name)
    artist = [j['track']['album']['artists']]
    for g in artist:
        artist_name = g[0]['name']
        artist_list.append(artist_name)
        href = g[0]['href']
        response2 = requests.get(href,headers=headers).json()
        g_n = response2['genres']
        genress = ', '.join(str(v) for v in g_n) 
        genre_list.append(genress) 
   




df = pd.DataFrame({
    "name" : song_list,
        
        "artists" : artist_list,


        "genre" : genre_list
        
})


play = response['tracks']['next']


df1 = df.to_csv('C:/projects/Data Engineering/py/apicalls/spotify/data/final_songs.csv', encoding='utf-8')

url2 = "https://api.spotify.com/v1/playlists/4CPdJAFwZhgik31FK76Pow/tracks?offset=100&limit=100"
response = requests.get(url2,headers=headers).json()

url3= "https://api.spotify.com/v1/playlists/4CPdJAFwZhgik31FK76Pow/tracks?offset=200&limit=100"

url4 = "https://api.spotify.com/v1/playlists/4CPdJAFwZhgik31FK76Pow/tracks?offset=300&limit=100"
    
url5 = "https://api.spotify.com/v1/playlists/4CPdJAFwZhgik31FK76Pow/tracks?offset=400&limit=100"

url6 = "https://api.spotify.com/v1/playlists/4CPdJAFwZhgik31FK76Pow/tracks?offset=500&limit=100"


track_url = "https://api.spotify.com/v1/tracks/3hkBwj7l9JPQajF6RsKzGW"

https://api.spotify.com/v1/tracks/3hkBwj7l9JPQajF6RsKzGW

response = requests.get(track_url,headers=headers).json()


response = requests.get(url6,headers=headers).json()
response = requests.get(url5,headers=headers).json()
response = requests.get(url4,headers=headers).json()
response = requests.get(url3,headers=headers).json()





client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)




track_uri = "spotify:track:3hkBwj7l9JPQajF6RsKzGW"




sp.audio_features(track_uri)[0]



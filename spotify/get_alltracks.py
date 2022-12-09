



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


song_list =[]
artist_list = []
genre_list = []
grant_type = 'client_credentials'
body_params = {'grant_type' : grant_type}

url='https://accounts.spotify.com/api/token'
response = requests.post(url, data=body_params, auth = (CLIENT_ID, CLIENT_SECRET)) 

access_token = response.json().get('access_token')

base_url = 'https://api.spotify.com/v1/users/x5raulz6ufun7mia2v0s6oqeq/playlists/4CPdJAFwZhgik31FK76Pow/'

csvheaders = ['song_name','artist_name','Genre']

#4X8mtKyMYDYdvm2R0RfQvc 
#4CPdJAFwZhgik31FK76Pow
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

response = requests.get(base_url,headers=headers).json()
play = response['tracks']['items']   #['track']-->['album']-->['artists']-->['name']

#genre
for j in play:
    s_n = [j['track']['name']]
    song_name = ','.join(str(v) for v in s_n) 
    song_list.append(song_name)
    artist = [j['track']['album']['artists']]
    for g in artist:
        artist_name = g[0]['name']
        artist_list.append(artist_name)
        href = g[0]['href']
        response2 = requests.get(href,headers=headers).json()
        g_n = response2['genres']
        genress = ','.join(str(v) for v in g_n) 
        genre_list.append(genress) 
   

df = pd.DataFrame({
    "name" : song_list,
        
        "artists" : artist_list,


        "genre" : genre_list
        
})


df1 = df.to_csv('C:/projects/Data Engineering/py/apicalls/spotify/data/first100.csv', encoding='utf-8')






   
   










'''
#genre
for j in play:
    artist = [j['track']['album']['artists']]
    for g in artist:
        href = g[0]['href']
        response2 = requests.get(href,headers=headers).json()
        genre_1 = response2['genres']
        genre_list.append(genre_1) 
            
'''  







'''
            continue  
        continue



            genre_1 = response2['genres']
            genre_list = ','.join(str(v) for v in genre_1)  
            new_list.append(genre_list)
    
    
    
    
    
    new_list.append(genre)



for i in new_list:




        response2 = requests.get(genre,headers=headers).json()
        genre_1 = response2['genres']
        






df = pd.DataFrame({

            'artist' : artist_list
})




df

pd.set_option('display.max_rows', None)


df.set_option('display.max_rows', None)




pandas.set_option('display.max_rows', None)




each artisthave uniques url

fetch artist url and from there fetch genre list, one per each row


'''
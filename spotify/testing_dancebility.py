import requests
import json
import pandas as pd
import csv
import tekore as tk


client_id = "ca7fbe12e14546cb94ec1ec90c536bce"
client_secret = "f660057e1ba2440dae9b3dbe4a9d67aa"
redirect_uri = "http://localhost:7777/callback"
playlist_id = "4CPdJAFwZhgik31FK76Pow"

conf = (client_id, client_secret, redirect_uri)
token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)

spotify = tk.Spotify(token)

first_items = spotify.playlist_items(playlist_id)




for item in spotify.all_items(first_items):
    print(item('tracks'))


    for i2 in item:
        print(i2['tracks'])



tracks1 = spotify.playlist(playlist_id, fields=None, market=None, as_tracks=True)

new_l = []

play = tracks1['tracks']['items']

#genre
for j in play:
    s_n = [j['track']['name']]
    new_l.append(s_n)

first_items = spotify.playlist_items(playlist_id)
for item in spotify.all_items(first_items):













spotify.playback_start_tracks([t.id for t in tracks.items])

spotify = tk.Spotify(token)
tracks = spotify.current_user_top_tracks(limit=10)
spotify.playback_start_tracks([t.id for t in tracks.items])



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
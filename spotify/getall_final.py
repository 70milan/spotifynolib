import requests
import pandas as pd
import matplotlib.pyplot as plt 
from pandasql import sqldf
from urllib.parse import urlencode
#import json
import webbrowser
import base64

client_id = "ca7fbe12e14546cb94ec1ec90c536bce"
client_secret = "764ad9c13b9a475288eb7f5f394a2ed8"

limit = 20
offset = 0

all_items = []
add = []
hrefs=[]
song_list =[]
artist_list = []
genre_list = []
ids = []
diff_scores = []
album_list=[]
#access_token = "BQDeV0IiPAN2p1fAmnin7Exdq5JOCrcvEZkdZe_xAfgcrw0v5EQMmTjdb8UsGCuijVboj4uLd24d82FN1fDVPd3rCCSHBVuxS4nHs3AEIurb2F67SRw"




auth_headers = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": "http://localhost:7777/callback",
    "scope": "user-library-read"
}



webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

code = str(input("enter your code here: "))

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

r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

access_token = r.json()["access_token"]

headers = {
'Authorization': 'Bearer {}'.format(access_token)
}

response = requests.get('https://api.spotify.com/v1/me/tracks', headers=headers).json()

total = response['total']  

print("Total 'liked songs' found: ", total)
##$ to save the json object ##

'''
jsonString = json.dumps(all_items)
jsonFile = open("testdata.json", "w")
jsonFile.write(jsonString)
jsonFile.close()
'''

for offset in range(0, total, 20):
        url = "https://api.spotify.com/v1/me/tracks?offset="+str(offset) + "&limit=20" 
        response1 = requests.get(url, headers=headers).json()
        getter = response1['items']
        all_items.extend(getter)          

for j in all_items:
    dateAddd = j['added_at'] 
    dateAdd = dateAddd[0:10]#added date
    add.append(dateAdd)
    s_n = [j['track']['name']]
    Id = [j['track']['id']] #id
    identif = ' '.join(str(v) for v in Id) 
    ids.append(identif) 
    song_name = ','.join(str(v) for v in s_n) 
    song_list.append(song_name) #tracks
    album = [j['track']['album']['name']]
    album1 = ' '.join(str(v) for v in album) 
    album_list.append(album1) #albums
    artist = [j['track']['album']['artists']]
    for g in artist:
        if len(g) > 1:
            art = g[0]['name'], g[1]['name']
            artist_name = ', '.join(str(v) for v in art) 
        else:
            artist_name = g[0]['name']
        artist_list.append(artist_name) #artist name
        href = g[0]['href']
        response2 = requests.get(href,headers=headers).json()
        g_n = response2['genres']
        genress = ', '.join(str(v) for v in g_n) 
        genre_list.append(genress) 

#########Get Audio features###########

url = "https://api.spotify.com/v1/audio-features/"

for i in ids:
    urls = url + i
    res = requests.get(urls, i, headers=headers).json()
    dance_score = [res['id'],res['danceability'], res['energy'],res['key']
    ,res['loudness'],res['mode'],res['speechiness'],res['acousticness']
    ,res['instrumentalness'],res['liveness'],res['valence'], res['tempo']]
    diff_scores.append(dance_score)



df = pd.DataFrame({"id": ids, "date_added":add,"track_list": song_list,"album_name" : album_list, "artists_list": artist_list, "genre_list": genre_list})
df2 = pd.DataFrame(diff_scores)
df2.columns=['id','danceability','energy','key','loudness','mode','speechiness','acousticness', 'instrumentalness','liveness','valence', 'tempo']
df_merged = df.merge(df2)



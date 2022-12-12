import requests
import pandas as pd
#import json



CLIENT_ID = "ca7fbe12e14546cb94ec1ec90c536bce"
CLIENT_SECRET = "2a21c07b2a1d4acea157cb60de098142"

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

response = requests.get('https://api.spotify.com/v1/me/tracks/?access_token=BQAK53qidG3z_6K2HjmsHevezDeTZze_swCXn6i_v1z_BP4tY17sQkRC3aAXJLG48J9PdOLqfpW_126KHaCcmCNAx6IjHN-KsDCUA7XRQ_E4S-rmwxM8YJgi6MzDrYAkAf1bHb_Yioh3JuzXVK-agxqaloRHJEZ1ZQDwYKuvuTOZ9GM08dzRm6RTotND8lHhK8wF5d-wDS8p').json()

access_token = "BQAK53qidG3z_6K2HjmsHevezDeTZze_swCXn6i_v1z_BP4tY17sQkRC3aAXJLG48J9PdOLqfpW_126KHaCcmCNAx6IjHN-KsDCUA7XRQ_E4S-rmwxM8YJgi6MzDrYAkAf1bHb_Yioh3JuzXVK-agxqaloRHJEZ1ZQDwYKuvuTOZ9GM08dzRm6RTotND8lHhK8wF5d-wDS8p"

headers = {
'Authorization': 'Bearer {}'.format(access_token)
}

total = response['total']  #['track']-->['album']-->['artists']-->['name']

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
    dateAdd = j['added_at'] #added date
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





df = pd.DataFrame({"id": ids, "date_added":add,"track_list": song_list,"album_name" : album_list, "artists_list": artist_list, "genre_list": genre_list})

#########Get Audio features###########

url = "https://api.spotify.com/v1/audio-features/"

for i in ids:
    urls = url + i
    res = requests.get(urls, i, headers=headers).json()
    dance_score = [res['id'],res['danceability'], res['energy'],res['key']
    ,res['loudness'],res['mode'],res['speechiness'],res['acousticness']
    ,res['instrumentalness'],res['liveness'],res['valence'], res['tempo']]
    diff_scores.append(dance_score)

df2 = pd.DataFrame(diff_scores)
df2.columns=['id','danceability','energy','key','loudness','mode','speechiness','acousticness', 'instrumentalness','liveness','valence', 'tempo']
df_merged = df.merge(df2)
df_merged.to_csv('C:/projects/Data Engineering/py/apicalls/spotify/data/song_details.csv', encoding='utf-8')

#################################################

#################################################

#################################################

#################################################
'''
for a in all_items:
    items = a['added_at'] #added date
    add.append(items)
    trak = a['track']['name']
    #trak_name = ', '.join(str(v) for v in trak) 
    song_list.append(trak) #Songs 
    for artists in a['track']['album']['artists'][0]["name"]
    artist_list.append(artists) #artists 


for g in a['track']['album']['artists'][0]['href']:
    print(genres)



    response2 = requests.get(genres,headers=headers).json()
    g_n = response2['genres']
    genre_list.append(g_n) 
        




        href = genres['href']
        hrefs.append(href)
        for refs in hrefs:
            response2 = requests.get(refs,headers=headers).json()
            g_n = response2['genres']
            genre_list.append(g_n) 
 

df = pd.DataFrame({"date_added":add,"track_list": song_list,"artists_list": artist_list, "genre_list": genre_list})







            
            
         
                artist = [items[0]['track']['album']['artists']]
                for g in artist:
                    artist_name = g[0]['name']
                    artist_list.append(artist_name)
                    href = g[0]['href']
                    response2 = requests.get(href,headers=headers).json()
                    g_n = response2['genres']
                    genress = ', '.join(str(v) for v in g_n) 
                    genre_list.append(genress) 


          
url = "https://api.spotify.com/v1/audio-features/"

for i in ids:
    urls = url + i
    res = requests.get(urls, i, headers=headers).json()
    dance_score = [res['id'],res['danceability'], res['energy'],res['key']
    ,res['loudness'],res['mode'],res['speechiness'],res['acousticness']
    ,res['instrumentalness'],res['liveness'],res['valence'], res['tempo']]
    diff_scores.append(dance_score)




df = pd.DataFrame({"id": ids, "name" : song_list, "Date_added": date_add ,"artists" : artist_list,"genre" : genre_list})
df2 = pd.DataFrame(diff_scores)
df2.columns=['id','danceability','energy','key','loudness','mode','speechiness','acousticness', 'instrumentalness','liveness','valence', 'tempo']
df_merged = df.merge(df2)
df.to_csv('C:/projects/Data Engineering/py/apicalls/spotify/data/song_details.csv', encoding='utf-8')

df2.to_csv('C:/projects/Data Engineering/py/apicalls/spotify/data/dance_song_details.csv', encoding='utf-8')


   












df = pd.DataFrame({"song": song_list})'''
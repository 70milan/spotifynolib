from __future__ import print_function
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util


client_id = "ca7fbe12e14546cb94ec1ec90c536bce"
client_secret = "764ad9c13b9a475288eb7f5f394a2ed8"

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

auth_headers = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": "http://localhost:7777/callback",
    "scope": "user-library-read"
}



username="x5raulz6ufun7mia2v0s6oqeq"
scope = "user-library-read"
token = util.prompt_for_user_token(username, scope)

util.prompt_for_user_token(username,scope,client_id='your-spotify-client-id',client_secret='your-spotify-client-secret',redirect_uri='your-app-redirect-url')



client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)




'''
set SPOTIPY_CLIENT_ID="ca7fbe12e14546cb94ec1ec90c536bce"
set SPOTIPY_CLIENT_SECRET="764ad9c13b9a475288eb7f5f394a2ed8"
set SPOTIPY_REDIRECT_URI="http://localhost:7777/callback"
'''

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)




'''
#SETTING UP CONNECTION
pgconn = psycopg2.connect (
host='localhost',
database='postgres',
user='postgres',
password='3231'
)

# BYPASSING TRANSACTION ERRORS WHILE USING PSYCOPG2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
pgconn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

#CREATE A CURSOR
pgcursor = pgconn.cursor()

#EXECUTE SQL

pgcursor.execute('select current_database()')

#to get result fetchall or fetchone
pgcursor.fetchall()

#to execute, COMMIT


#CLOSE CONNECTION

'''


from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:3231@localhost:5432/postgres')



df_merge_2.to_sql('song_all_details_1', engine, schema = 'dataeng', if_exists='replace', index=False)
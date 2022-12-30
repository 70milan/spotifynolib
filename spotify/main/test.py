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

import requests
import json

uri_redirect = 'http://localhost:7777/callback'
authorize_endpoint = 'https://accounts.spotify.com/authorize'
request_authorization_parameters = {'client_id': "ca7fbe12e14546cb94ec1ec90c536bce",
                                    'response_type': 'code',
                                    'redirect_uri': uri_redirect,
                                    'scope': 'user-library-read playlist-read-private'}
r_auth = requests.get(authorize_endpoint,
                      params=request_authorization_parameters)



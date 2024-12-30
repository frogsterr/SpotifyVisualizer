import dotenv
import os
import json


dotenv.load_dotenv()
client_id = os.environ.get("CLIENTID")
client_secret = os.environ.get("CLIENTSECRET")
redirect_uri = 'https://www.testworks.com/'
'''
# OAuth endpoints given in the Spotify API documentation
# https://developer.spotify.com/documentation/general/guides/authorization/code-flow/
authorization_base_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"
# https://developer.spotify.com/documentation/general/guides/authorization/scopes/
scope = [
    "user-read-email",
    "playlist-read-collaborative",
    "playlist-read-private"
]

from requests_oauthlib import OAuth2Session
spotify = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

# Redirect user to Spotify for authorization
authorization_url, state = spotify.authorization_url(authorization_base_url)
print('Please go here and authorize: ', authorization_url)

# Get the authorization verifier code from the callback url
redirect_response = input('\n\nPaste the full redirect URL here: ')

from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth(client_id, client_secret)

# Fetch the access token
token = spotify.fetch_token(token_url, auth=auth,
        authorization_response=redirect_response)

print(token)

# Fetch a protected resource, i.e. user profile
r = spotify.get('https://api.spotify.com/v1/me/playlists')
json = json.loads(r.content)
print(json)
'''

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="user-library-read playlist-read-private user-top-read",  # Multiple scopes

))

results = sp.current_user_saved_tracks()
print(results)

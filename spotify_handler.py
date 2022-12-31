from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from config_handler import config
from config_handler import changeValue
from os import system

spotify_config = config["SPOTIFY"]

if spotify_config['spotify_username'] == '':
  system('clear')
  print("Head to the spotify web app and click on your profile. Your spotify username should be a string of numbers\n")
  username = input("spotify username :")
  changeValue('SPOTIFY','spotify_username',username)

if spotify_config['SPOTIPY_CLIENT_ID'] == '' and spotify_config["SPOTIPY_CLIENT_SECRET"] == '':
  system('clear')
  print('THIS IS REQUIRED TO RUN THE REST OF THE PROGRAM\n1.) Go to https://developer.spotify.com/ and sign in\n2.) Go to dashboard and create a new app\n3.) Get the client Id and client secret from the application you just created\n')
  client_id = input("client id :")
  client_secret = input("client secret :")
  changeValue('SPOTIFY','SPOTIPY_CLIENT_ID',client_id)
  changeValue('SPOTIFY','SPOTIPY_CLIENT_SECRET',client_secret)

if __name__ == "__main__":
  auth_manager = SpotifyClientCredentials(client_id = spotify_config['SPOTIPY_CLIENT_ID'],client_secret = spotify_config["SPOTIPY_CLIENT_SECRET"])
  sp = Spotify(client_credentials_manager=auth_manager)
  print("Connected to spotify, hi ")
import discogs_client
from config_handler import config
from config_handler import changeValue
from os import system

discog_config = config["DISCOGS"]

if discog_config['user_token'] == '':
  system("clear")
  userToken = input("Please input user token\n“Click user avatar on top right of screen” - “Settings” - “Developers” - “Generate new token “\nuser token :")
  changeValue("DISCOGS",'user_token',userToken)

if discog_config['consumer_key'] == '' and discog_config['consumer_secret'] == '' :
  system("clear")
  print("Please input consumer key and secret \n “Click user avatar on top right of screen” - “Settings” - “Developers” - “Create an appplication”. Fill out the form, copy consumer key and secret")
  consumerKey = input("consumer key : ")
  consumerSecret = input("consumer secret : ")
  changeValue("DISCOGS",'consumer_key',consumerKey)
  changeValue("DISCOGS",'consumer_secret',consumerSecret)
  
d = discogs_client.Client(
  'discog2playlist/0.1', 
  user_token = discog_config["user_token"],
  consumer_key = discog_config["consumer_key"],
  consumer_secret = discog_config["consumer_secret"],
  token=u'my_token',
  secret=u'my_token_secret'  
)

if discog_config['access_token'] == '' and discog_config['access_token_secret'] == '' :
  print(f"Please click this link and type the code here\n {d.get_authorize_url()[-1]}")
  token = input(">> ")
  tokens = d.get_access_token(token)
  changeValue("DISCOGS",'access_token',tokens[0])
  changeValue("DISCOGS",'access_token_secret',tokens[1])

d.set_token(discog_config['access_token'],discog_config['access_token_secret'])

me = d.identity()
counter= 0
for item in me.collection_folders[0].releases:
  title = item.release.title
  artists =  list(map(lambda x: x.name,item.release.artists))
  print(f"{counter}: {title} | {artists[0]}")
  counter += 1

  

"""

result = d.search("Creep")
print(result.page(1))

"""


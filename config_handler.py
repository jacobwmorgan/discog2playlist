from configparser import ConfigParser
import os.path

dir_path =  os.path.dirname(os.path.realpath(__file__))
config_location = dir_path+"/config.ini"

if os.path.exists(config_location):
  print("--------config.ini file found at ", config_location)
  config = ConfigParser()
  config.read(config_location)


else:
    print("---------config.ini file not found at ", config_location)


def changeValue(section,value,new):
  config.set(section,value,new)
  with open(config_location,'w') as configfile:
    config.write(configfile)

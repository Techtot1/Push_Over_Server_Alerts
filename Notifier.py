
import os
import json
import datetime
import requests

SendTime = datetime.datetime.now()

with open(os.getcwd()+"/Config.json","r") as ConfigFile:
    Config = json.load(ConfigFile)

Config["message"] ="",
Config["title"] = ""

with open(os.getcwd()+"/Config.json","w") as ConfigFile:   
    json.dump(Config,ConfigFile)
    ConfigFile.close()



with open(os.getcwd()+"/Config.json","r") as File_Upload:
    File = json.load(File_Upload)
    send = requests.post("https://api.pushover.net/1/messages.json",File)
    print(send.text)
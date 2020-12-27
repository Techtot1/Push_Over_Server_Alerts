
import os
import json
import datetime
import requests

SendTime = datetime.datetime.now()

with open(os.getcwd()+"/Config.json","r") as ConfigFile:
    Config = json.load(ConfigFile)

Config["message"] =("The MCMA and/or Eternalcraft minecraft server has stopped at: {}".format(SendTime.strftime("%Y-%m-%d  %H:%M:%S"))),
Config["title"] = "MCMA/Eternalcraft CRASH/ERROR!"

with open(os.getcwd()+"/Config.json","w") as ConfigFile:   
    json.dump(Config,ConfigFile)
    ConfigFile.close()



with open(os.getcwd()+"/Config.json","r") as File_Upload:
    File = json.load(File_Upload)
    send = requests.post("https://api.pushover.net/1/messages.json",File)
    print(send.text)
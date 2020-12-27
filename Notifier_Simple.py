
import os
import json
import datetime
import requests

with open(os.getcwd()+"/Config.json","r") as File_Upload:
    File = json.load(File_Upload)
    send = requests.post("https://api.pushover.net/1/messages.json",File)
    print(send.text)
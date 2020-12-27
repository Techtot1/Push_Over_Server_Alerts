import json
import os



with open(os.getcwd()+"/reset.json","r") as ResetFile:
    reset = json.load(ResetFile)


for i in reset:
    with open(os.getcwd()+"/"+reset[str(i)],"r") as ConfigFile:
        Config = json.load(ConfigFile)
    Config["sent"] ="False"
    with open(os.getcwd()+"/"+reset[str(i)],"w") as ConfigFile:   
                json.dump(Config,ConfigFile)
                ConfigFile.close()
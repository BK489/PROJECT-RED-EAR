#functions for config stuff

import os 

def config_exists(inputpath):
    querypath = os.path.join(inputpath, "RED-EAR-Config.json")
    if os.path.isfile(querypath):
        return True
    else:
        return False

def load_config():
    #will load json file into software, should be efficient so can be called 
    pass
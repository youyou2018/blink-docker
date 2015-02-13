#!/usr/bin/python3
# -*-coding:utf-8 -*

import time
import subprocess
from browser import Browser,utils

class Firefox(Browser):        
    
    def __init__(self):
        super().__init__()
        
    def importData(self):
        pass
            
    def exportData(self):
        jsonExportData = utils.readJSONDataFile(self.dataPath)
        return jsonExportData["passwordEncryption"]
            
    def runBrowser(self):
        return subprocess.Popen("LD_PRELOAD=/home/blink/ldpreload/modUname.so ./browsers/firefox/firefox -no-remote  -profile /home/blink/.mozilla/firefox/blink.default", shell=True)
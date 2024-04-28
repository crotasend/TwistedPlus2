from sys import version
import settingsmanager
import configparser
from configparser import ConfigParser
import os
import webbrowser
import time
import psutil
import subprocess
import macro


def CheckRoblox():
    for proc in psutil.process_iter():
        if proc.name() == "RobloxPlayerBeta.exe":
            return True
    return False

def RunRoblox():
    subprocess.run(["taskkill", "/im", "RobloxPlayerBeta.exe", "/f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["taskkill", "/im", "actions.ahk", "/f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2.5)
    config = configparser.ConfigParser()
    config.read('config.ini')
    link = config.get('Settings', 'serverLink')
    
    webbrowser.open(link, new=0, autoraise=False)
                    
    while not CheckRoblox():
        time.sleep(1) 
        
    subprocess.run(["taskkill", "/im", "firefox.exe", "/f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["taskkill", "/im", "chrome.exe", "/f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    time.sleep(3)
    macro.StartServer()
    return

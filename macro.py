from re import I
import gui
import settingsmanager
import configparser
import pyautogui, sys
from PIL import ImageGrab
import time
import subprocess
import psutil
import threading
import os
import recog

lock = threading.Lock()
    



def StartServer():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    actions_script = os.path.join(script_dir, "actions.ahk")
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    resolution = config.get('Settings', 'resolution')

    litemode = config.get('Settings', 'litemode')
        
    global cr, cg # announce globals
    cr = (255, 85, 127)
    cg = (170, 255, 127)

    if resolution:
        process = subprocess.Popen(["AutoHotkeyU64.exe", actions_script, resolution, litemode])
    else:
        return
    
    process.wait()
    
    recog.getThermos()
import re
import pytesseract
from PIL import ImageGrab, ImageOps
import configparser
import time
import roblox
import tkinter as tk
import gui
from tkinter import messagebox
import webhooks


def getThermos():
    time.sleep(1)
    config = configparser.ConfigParser()
    config.read('config.ini')
    sw = config.get('Settings', 'resolution')
    
    # Set the coordinates of the region to capture (left, top, right, bottom)
    if sw == "1440p": 
        region = (720, 105, 1820, 745)  # Example coordinates
    elif sw == "1080p":
        region = (550, 105, 1365, 660)
    else:

        exit()

    # Grab a screenshot of the specified region
    screenshot = ImageGrab.grab(bbox=region)

    # Use Tesseract OCR to extract text
    time.sleep(1)
    text = pytesseract.image_to_string(screenshot, config='--psm 11', lang='eng')
   
    variables = [
    ("DAY1", r"DAY 1 (\w+)"),
    ("DAY2", r"DAY 2 (\w+)"),
    ("DAY3", r"DAY 3 (\w+)"),
    ("TEMPERATURE", r"TEMPERATURE: (\d+)F"),
    ("SRH", r"SRH: (\d+)"),
    ("DEWPOINT", r"DEWPOINT: (\d+)F"),
    ("CAPE", r"CAPE: (\d+) J/kg"),
    ("THREECAPE", r"3CAPE: (\d+) J/kg"),
    ("LLAPSE", r"0-3KM LAPSE RATES: (\d+(?:\.\d+)?) C/km"),
    ("HLAPSE", r"3-6KM LAPSE RATES: (\d+(?:\.\d+)?) C/km"),
    ("STP", r"S(?:T)?P:\s?(\d+)"),
    ("VTP", r"V(?:T)?P:\s?(\d+)"),
    ("PWAT", r"PWAT: (\d+\.\d+) in."),
    ("MBRH", r"700-500mb RH: (\d+)%"),
    ("SURFACERH", r"SURFACE RH: (\d+)")
    ]
    
    thermos = {}
    for var_name, pattern in variables:
        match = re.search(pattern, text)
        thermos[var_name] = match.group(1) if match else None
   

    def compareThermos():
        config = configparser.ConfigParser()
        config.read('config.ini')
        min_srh = int(config.get('Settings', 'min_srh'))
        min_stp = int(config.get('Settings', 'min_stp'))
        min_vtp = int(config.get('Settings', 'min_vtp'))
        min_cape = int(config.get('Settings', 'min_cape'))
        min_3cape = int(config.get('Settings', 'min_3cape'))
        min_03km_lapse = float(config.get('Settings', 'min_03km_lapse'))
        min_36km_lapse = float(config.get('Settings', 'min_36km_lapse'))
        min_mbrh = int(config.get('Settings', 'min_mbrh'))
        min_surface_rh = int(config.get('Settings', 'min_surface_rh'))

        # Initialize a flag to track if all conditions are met
        all_conditions_met = True

        # Check each condition
        conditions = {
            'SRH': int(thermos.get('SRH', '9999')) >= min_srh,
            'STP': int(thermos.get('STP', '9999')) >= min_stp,
            'VTP': int(thermos.get('VTP', '9999')) >= min_vtp,
            'CAPE': int(thermos.get('CAPE', '9999')) >= min_cape,
            'THREECAPE': int(thermos.get('THREECAPE', '9999')) >= min_3cape,
            'LLAPSE': float(thermos.get('LLAPSE', '9999')) >= min_03km_lapse,
            'HLAPSE': float(thermos.get('HLAPSE', '9999')) >= min_36km_lapse,
            'MBRH': int(thermos.get('MBRH', '9999')) >= min_mbrh,
            'SURFACERH': int(thermos.get('SURFACERH', '9999')) >= min_surface_rh
        }

        # Print if any condition is not met and set all_conditions_met flag
        for key, value in conditions.items():
            if not value:
                all_conditions_met = False

        # Print the overall result
        if all_conditions_met:
            root = tk.Tk()
            root.withdraw()
    
            webhooks.send_thermos_discord(thermos)
            messagebox.showinfo("All Conditions Met", "All conditions are met.")
    
            root.destroy()  # Close the tkinter window and stop the mainloop
            
        else:
            autoroll = config.get('Settings', 'autoroll')
            if autoroll == "False":
                root = tk.Tk()
                root.withdraw()  # Hide the main window

                # Show a message box with options
                choice = messagebox.askquestion("Twisted+",
                                                "Requirements are not met. Do you want to reroll?",
                                                icon='warning')

                if choice == 'yes':
                    roblox.RunRoblox()
                else:
                    return

                root.destroy()  # Start the tkinter event loop
            else:
                roblox.RunRoblox()

            
    compareThermos()
def getCode():
    time.sleep(1)
    config = configparser.ConfigParser()
    config.read('config.ini')
    sw = config.get('Settings', 'resolution')
    
    if sw == "1440p": 
        region = (138, 0, 240, 57)  # Example coordinates
    elif sw == "1080p":
        region = (120, 0, 212, 31)
    else:
        exit()

    # Grab a screenshot of the specified region
    screenshot = ImageGrab.grab(bbox=region)

    # preprocess the image
    screenshot = ImageOps.invert(screenshot)
    screenshot = ImageOps.autocontrast(screenshot)

    # Use Tesseract OCR to extract text
    time.sleep(1)
    code = pytesseract.image_to_string(screenshot, config='--psm 7', lang='eng')
    return code

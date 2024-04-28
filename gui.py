import traceback
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import settingsmanager
import roblox
import threading

class GUI:
    
    def __init__(self):
        self.root = tk.Tk() # Create the main window
        
        self.ico = Image.open('icon.jpg') # CHANGE ICON
        self.photo = ImageTk.PhotoImage(self.ico) 
        self.root.wm_iconphoto(False, self.photo) 
        
        
        self.root.title("TwistedPlus2.0") # ----------- INIT
        self.root.geometry("900x500")
        
        self.root.tk.call('source', 'theme/azure.tcl')
        self.root.tk.call('set_theme', 'dark')

        def rerollMessage():
            messagebox.showinfo("Twisted+", "Server does not meet requirements.")
        
        def createSettingsWindow():
            

            global settings
            settings = {}
            
            global window_2
            
            window_2 = tk.Toplevel() # --- Initializes window
            window_2.title('Settings')
            window_2.geometry("650x500") 
            
            notebook = ttk.Notebook(window_2) # --- Initializes tabs
            notebook.pack(fill='both', expand=True)
            
            
            # General intialization
            general_tab = ttk.Frame(notebook)
            notebook.add(general_tab, text='General')
           
            # Preferences initialization
            preferences_tab = ttk.Frame(notebook)
            notebook.add(preferences_tab, text='Preferences')
            

            
            # Preferences contents

            def generatePrefs():
                
                def applyPrefs():
                    if LiteMode:
                        settings['liteMode'] = LiteMode.get()
                    if min_srh: 
                        settings['min_srh'] = min_srh.get()
                    if min_stp:   
                        settings['min_stp'] = min_stp.get()
                    if min_vtp:   
                        settings['min_vtp'] = min_vtp.get()
                    if min_cape:    
                        settings['min_cape'] = min_cape.get()
                    if min_3cape:    
                        settings['min_3cape'] = min_3cape.get()
                    if min_03km_lapse:    
                        settings['min_03km_lapse'] = min_03km_lapse.get()
                    if min_36km_lapse:    
                        settings['min_36km_lapse'] = min_36km_lapse.get()
                    if min_mbrh:    
                        settings['min_mbrh'] = min_mbrh.get()
                    if min_surface_rh:    
                        settings['min_surface_rh'] = min_surface_rh.get()
         
                    if any([LiteMode, min_srh, min_stp, min_vtp, min_cape, min_3cape, min_03km_lapse, min_36km_lapse, min_mbrh, min_surface_rh]):
                        settingsmanager.save_settings(settings)

                
                LiteMode = tk.BooleanVar()
                min_srh = tk.StringVar()
                min_stp = tk.StringVar()
                min_vtp = tk.StringVar()
                min_cape = tk.StringVar()
                min_3cape = tk.StringVar()
                min_03km_lapse = tk.StringVar()
                min_36km_lapse = tk.StringVar()
                min_mbrh = tk.StringVar()
                min_surface_rh = tk.StringVar()  


                LiteCheck = ttk.Checkbutton(preferences_tab, text="Lite Mode", variable = LiteMode)
                LiteCheck.place(relx = 0.5, rely = (1/12), anchor = "center")
            
                min_srh_label = ttk.Label(preferences_tab, text="Minimum SRH")
                min_srh_label.place(relx=0.2, rely=(2/12), anchor="center")
                min_srh_entry = ttk.Entry(preferences_tab, textvariable = min_srh)
                min_srh_entry.place(relx=0.5, rely=(2/12), anchor="center")
            
                min_stp_label = ttk.Label(preferences_tab, text="Minimum STP")
                min_stp_label.place(relx=0.2, rely=(3/12), anchor="center")
                min_stp_entry = ttk.Entry(preferences_tab, textvariable = min_stp)
                min_stp_entry.place(relx=0.5, rely=(3/12), anchor="center")
            
                min_vtp_label = ttk.Label(preferences_tab, text="Minimum VTP")
                min_vtp_label.place(relx=0.2, rely=(4/12), anchor="center")
                min_vtp_entry = ttk.Entry(preferences_tab, textvariable = min_vtp)
                min_vtp_entry.place(relx=0.5, rely=(4/12), anchor="center")
            
                min_cape_label = ttk.Label(preferences_tab, text="Minimum CAPE")
                min_cape_label.place(relx=0.2, rely=(5/12), anchor="center")
                min_cape_entry = ttk.Entry(preferences_tab, textvariable = min_cape)
                min_cape_entry.place(relx=0.5, rely=(5/12), anchor="center")
            
                min_3cape_label = ttk.Label(preferences_tab, text="Minimum 3CAPE")
                min_3cape_label.place(relx=0.2, rely=(6/12), anchor="center")
                min_3cape_entry = ttk.Entry(preferences_tab, textvariable = min_3cape)
                min_3cape_entry.place(relx=0.5, rely=(6/12), anchor="center")
            
                min_03km_lapse_label = ttk.Label(preferences_tab, text="Minimum 0-3KM LAPSE RATES")
                min_03km_lapse_label.place(relx=0.2, rely=(7/12), anchor="center")
                min_03km_lapse_entry = ttk.Entry(preferences_tab, textvariable = min_03km_lapse)
                min_03km_lapse_entry.place(relx=0.5, rely=(7/12), anchor="center")
            
                min_36km_lapse_label = ttk.Label(preferences_tab, text="Minimum 3-6KM LAPSE RATES")
                min_36km_lapse_label.place(relx=0.2, rely=(8/12), anchor="center")
                min_36km_lapse_entry = ttk.Entry(preferences_tab, textvariable = min_36km_lapse)
                min_36km_lapse_entry.place(relx=0.5, rely=(8/12), anchor="center")
            
                min_mbrh_label = ttk.Label(preferences_tab, text="Minimum mbRH")
                min_mbrh_label.place(relx=0.2, rely=(9/12), anchor="center")
                min_mbrh_entry = ttk.Entry(preferences_tab, textvariable = min_mbrh)
                min_mbrh_entry.place(relx=0.5, rely=(9/12), anchor="center")
            
                min_surface_rh_label = ttk.Label(preferences_tab, text="Minimum Surface RH")
                min_surface_rh_label.place(relx=0.2, rely=(10/12), anchor="center")
                min_surface_rh_entry = ttk.Entry(preferences_tab, textvariable = min_surface_rh)
                min_surface_rh_entry.place(relx=0.5, rely=(10/12), anchor="center")

               
               
                applyButton = ttk.Button(preferences_tab, text="Apply", command = applyPrefs)
                
                applyButton.place(relx = 0.9, rely = 0.9, anchor = "center")


            # General contents
            
            def generateGeneral():
                            
                # General contents
                def applyGeneral():
                    server_link = privServerLink.get()
                    webhook_link = dscrdLink.get()
                    res = resolution.get()

                    # Update settings only if the input is not empty
                    if server_link:
                        settings["serverLink"] = server_link
                    if webhook_link:
                        settings["webhookLink"] = webhook_link
                    if res:
                        settings["resolution"] = res
                        
                    settings["autoroll"] = autoroll.get()

                    if server_link or webhook_link or res or autoroll:
                        # Save settings and print a message
                        settingsmanager.save_settings(settings)
                
                privServerLink = tk.StringVar()
                dscrdLink = tk.StringVar()
                resolution = tk.StringVar()

                serverLinkLabel = ttk.Label(general_tab, text="Server Link")
                serverLinkLabel.place(relx = 0.5, rely = (1/12), anchor = "center")
                serverLink = ttk.Entry(general_tab, textvariable = privServerLink)
                serverLink.place(relx = 0.5, rely = (2/12), anchor = "center")
                
                webhookLinkLabel = ttk.Label(general_tab, text="Discord Webhook Link")
                webhookLinkLabel.place(relx = 0.5, rely = (3/12), anchor = "center")
                webhookLink = ttk.Entry(general_tab, textvariable = dscrdLink)
                webhookLink.place(relx = 0.5, rely = (4/12), anchor = "center")
                
                Reso = ttk.Label(general_tab, text="Resolution (ex; 1080p)")
                Reso.place(relx = 0.5, rely = (5/12), anchor = "center")
                Reso = ttk.Entry(general_tab, textvariable = resolution)
                Reso.place(relx = 0.5, rely = (6/12), anchor = "center")
                
                autoroll = tk.BooleanVar()
                
                autorollcheck = ttk.Checkbutton(general_tab, text="Auto-Roll", variable = autoroll)
                autorollcheck.place(relx = 0.5, rely = (7/12), anchor = "center")
                
                applyButton = ttk.Button(general_tab, text="Apply", command=applyGeneral)
                applyButton.place(relx = 0.9, rely = 0.9, anchor = "center")


            generatePrefs()
            generateGeneral()
        
            
        name_label = ttk.Label(self.root, text="Twisted+ (2.0)", font=('Arial', 20))
        name_label.place(relx=0.5, rely=0.1, anchor="center")
        
        
        settingsbutton = ttk.Button(text = "Settings", command=createSettingsWindow)
        settingsbutton.place(relx = 0.5, rely = 0.4, anchor = "center")
        
        def run_roblox():
            threading.Thread(target=roblox.RunRoblox).start()
        
        rollbutton = ttk.Button(text="Roll", command=run_roblox)
        rollbutton.place(relx=0.5, rely=0.5, anchor="center")


        self.root.mainloop()

        
GUI()
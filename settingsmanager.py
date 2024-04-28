import configparser
import os
import gui

if not os.path.exists('config.ini'):
    # Create a new settings.ini file with default settings
    config = configparser.ConfigParser()
    config['Settings'] = {
        'liteMode': '',
        'min_srh': '',
        'min_stp': '',
        'min_vtp': '',
        'min_cape': '',
        'min_3cape': '',
        'min_03km_lapse': '',
        'min_36km_lapse': '',
        'max_pwat': '',
        'min_mbrh': '',
        'min_surface_rh': '',
        'serverLink': '',
        'webhookLink': ''
    }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

config = configparser.ConfigParser()
config.read('config.ini')



def save_settings(settings):
    config = configparser.ConfigParser()
    config.read('config.ini')

    for key, value in settings.items():
        config.set('Settings', key, str(value))

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
        

def load_settings():
    settings = {
    'liteMode': '',
    'min_srh': '',
    'min_stp': '',
    'min_vtp': '',
    'min_cape': '',
    'min_3cape': '',
    'min_03km_lapse': '',
    'min_36km_lapse': '',
    'min_mbrh': '',
    'min_surface_rh': '',   
    'serverLink': '',
    'webhookLink': '',
    'resolution': '',
    'autoroll': ''
    }
    
    settings['liteMode'] = config['Settings']['liteMode']
    settings['min_srh'] = config['Settings']['min_srh']
    settings['min_stp'] = config['Settings']['min_stp']
    settings['min_vtp'] = config['Settings']['min_vtp']
    settings['min_cape'] = config['Settings']['min_cape']
    settings['min_3cape'] = config['Settings']['min_3cape']
    settings['min_03km_lapse'] = config['Settings']['min_03km_lapse']
    settings['min_36km_lapse'] = config['Settings']['min_36km_lapse']
    settings['min_mbrh'] = config['Settings']['min_mbrh']
    settings['min_surface_rh'] = config['Settings']['min_surface_rh']
    settings['serverLink'] = config['Settings']['serverLink']
    settings['webhookLink'] = config['Settings']['webhookLink']
    settings['resolution'] = config['Settings']['resolution']
    return settings
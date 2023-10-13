import os
import configparser

def read_config(section, key):
    # Define the path to the config.ini file
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(current_dir, '../..'))
    config_file_path = os.path.join(parent_dir, 'config', 'config.ini')
    
    # Initialize the ConfigParser
    config = configparser.ConfigParser()

    # Read the config.ini file
    config.read(config_file_path)

    # Access and return the value from the config file
    return config.get(section, key)
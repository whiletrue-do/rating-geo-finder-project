import os
from dotenv import load_dotenv

load_dotenv()

""" _INFO_
The load_dotenv() will need to be moved to the 'main' entry point to kick off the program

It is held here for the sake of development
"""

GOOGLE_MAPS_API_KEY = os.getenv('google_maps_api_key')
NEW_PLACES_API_BASE_URL = os.getenv('places_text_new_search')
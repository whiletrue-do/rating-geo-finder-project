from src.utils.env_config import GOOGLE_MAPS_API_KEY, NEW_PLACES_API_BASE_URL
import requests

# The following function utilises the following service
# https://developers.google.com/maps/documentation/places/web-service/text-search#text-search-examples

def search_for_places(search_text: str):
    
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": GOOGLE_MAPS_API_KEY,
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.id,places.types"
    }
    
    json = {
        "textQuery": search_text,
        "minRating": "4.5"
        }
    
    response = requests.post(NEW_PLACES_API_BASE_URL, json=json, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response}"





print(search_for_places("chinese restaurant in shoreditch, london"))
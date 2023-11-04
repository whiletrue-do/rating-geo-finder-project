import logging
import logging.config
import requests
from src.utils.env_config import GOOGLE_MAPS_API_KEY, NEW_PLACES_API_BASE_URL

logging.config.fileConfig('logging/google_places_api/google_places_logging.ini', disable_existing_loggers=True)
logger = logging.getLogger('googlePlacesApi')

# The following function utilises the following service
# https://developers.google.com/maps/documentation/places/web-service/text-search#text-search-examples


def search_for_places(search_text: str):
    
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": GOOGLE_MAPS_API_KEY,
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.types,places.rating,places.regularOpeningHours,places.googleMapsUri"
    }
    
    json = {
        "textQuery": search_text,
        "minRating": "4.5"
        }
    
    response = requests.post(NEW_PLACES_API_BASE_URL, json=json, headers=headers)
    
    try:
        logger.info(f"Request received a {response.status_code} and the first 10 characters of the body {response.text[:10]}")
        return response.json()
    except requests.exceptions.HTTPError as error:
        logger.error(f"a HTTP error occurred {error}")
    except requests.exceptions.ConnectionError as error:
        logger.error(f"a connection error has occurred {error}")
        logger.info(f"Connection error response {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as error:
        logger.error(f"unknown caught error please read -> {error}")
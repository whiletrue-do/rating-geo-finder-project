import logging
import logging.config
from src.utils.env_config import GOOGLE_PLACES_OPTIONAL_PARAMS_LIST


def google_places_parameter_validation(places_parameters: dict):
    
    for key in places_parameters.keys():
        if key not in GOOGLE_PLACES_OPTIONAL_PARAMS_LIST:
            return False
    
    return True
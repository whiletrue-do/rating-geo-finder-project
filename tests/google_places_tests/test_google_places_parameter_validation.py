import pytest
from src.google_maps_api.optional_parameter_validation import google_places_parameter_validation


def test_with_valid_parameters():
    valid_parameters = {
        "maxResultCount": 5,
        "minRating": 3.5
    }
    assert google_places_parameter_validation(valid_parameters) is True
    

def test_with_valid_parameters():
    valid_parameters = {
        "testpytest": 5,
        "minRating": 3.5
    }
    assert google_places_parameter_validation(valid_parameters) is False
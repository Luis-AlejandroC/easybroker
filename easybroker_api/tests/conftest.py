import pytest

@pytest.fixture
def user_data():
    return{ 'user_name': 'name', 'user_phone': 'phone', 'user_property_id': 'property_id', 
        'user_public_url': 'public_url'}
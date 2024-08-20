#Watthana Siamliem 653380280-0

from requests.models import Response

def get_mock_currency_api_response():
    """
    Method to create a sample response from the currency API (e.g. example-currency.com/rate)
    """
    mock_api_response = Response()
    mock_api_response.status_code = 200
    # Mocking a JSON response for currency exchange
    mock_api_response._content = b'{"base": "THB", "result": {"USD": 0.029}}'

    return mock_api_response

# Example usage:
response = get_mock_currency_api_response()
print(response.json())  # Output: {'base': 'THB', 'result': {'USD': 0.029}}

#Watthana Siamliem 653380280-0

import os
import sys
import unittest
from unittest.mock import patch

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from assignment.source.currency_exchanger import CurrencyExchanger
from assignment.test.utils import get_mock_currency_api_response

class TestCurrencyExchanger(unittest.TestCase):

    def setUp(self):
        self.currency_exchanger = CurrencyExchanger()
        self.mock_currency_api_response = get_mock_currency_api_response()

    @patch('assignment.source.currency_exchanger.requests.get')
    def test_get_currency_rate(self, mock_get):
        # Arrange
        mock_get.return_value = self.mock_currency_api_response

        # Act
        self.currency_exchanger.get_currency_rate()

        # Assert
        mock_get.assert_called_once_with(
            self.currency_exchanger.currency_api,
            params={'from': 'THB', 'to': 'USD'}
        )
        self.assertIsNotNone(self.currency_exchanger.api_response)
        self.assertEqual(self.currency_exchanger.api_response, self.mock_currency_api_response.json())

    @patch('assignment.source.currency_exchanger.requests.get')
    def test_currency_exchange(self, mock_get):
        # Arrange
        mock_get.return_value = self.mock_currency_api_response
        amount_in_thb = 500

        # Act
        converted_amount = self.currency_exchanger.currency_exchange(amount_in_thb)

        # Assert
        mock_get.assert_called_once_with(
            self.currency_exchanger.currency_api,
            params={'from': 'THB', 'to': 'USD'}
        )
        self.assertEqual(converted_amount, 14.50)  # 500 * 0.029 = 14.5

if __name__ == '__main__':
    unittest.main()

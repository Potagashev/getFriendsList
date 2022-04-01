from unittest import TestCase

from utils import format_date_to_iso, format_data


class DataFormattingTestCase(TestCase):
    def test_format_date_to_iso(self):
        real = format_date_to_iso('01.04.2022')
        expected = '2022-04-01'
        self.assertEqual(expected, real)

    def test_format_data(self):
        _list = [
            {
                'id': 111111111,
                'first_name': 'Иван',
                'last_name': 'Иванов',
                'can_access_closed': True,
                'is_closed': False,
                'sex': 2,
                'track_code': "f824oegcx-c-h5lz5i8mXUkYC-SMK3rJTa1vD_g"
            }
        ]
        expected = [
            {
                'first_name': 'Иван',
                'last_name': 'Иванов',
                'country': None,
                'city': None,
                'bdate': None,
                'sex': "Мужчина"
            }
        ]
        real = format_data(_list)
        self.assertEqual(expected, real)
import json
from unittest import TestCase

import report_maker


class SerializingTestCase(TestCase):
    """Ожидаемый результат создается вручную заранее"""
    def test_list_to_json(self):
        with open('test_reports/expected.json', encoding='utf-8') as json_file:
            expected = json.load(json_file)
            json_file.close()

        _dict = [
            {
                'first_name': 'Иван',
                'last_name': 'Иванов',
                'country': None,
                'city': None,
                'bdate': None,
                'sex': 'Мужчина'
            }
        ]
        report_maker.dict_to_json(data=_dict, output_path='test_reports/real.json')

        with open('test_reports/real.json', encoding='utf-8') as json_file:
            real = json.load(json_file)
            json_file.close()

        self.assertEqual(expected, real)

    def test_list_to_csv(self):
        with open('test_reports/expected.csv', encoding='utf-8') as csv_file:
            expected = csv_file.readlines()
            csv_file.close()

        _dict = [
            {
                'first_name': 'Иван',
                'last_name': 'Иванов',
                'country': None,
                'city': None,
                'bdate': None,
                'sex': 'Мужчина'
            }
        ]
        report_maker.dict_to_csv(data=_dict, output_path='test_reports/real.csv')

        with open('test_reports/real.csv', encoding='utf-8') as csv_file:
            real = csv_file.readlines()
            csv_file.close()

        self.assertEqual(expected, real)

    def test_list_to_tsv(self):
        with open('test_reports/expected.tsv', encoding='utf-8') as csv_file:
            expected = csv_file.readlines()
            csv_file.close()

        _dict = [
            {
                'first_name': 'Иван',
                'last_name': 'Иванов',
                'country': None,
                'city': None,
                'bdate': None,
                'sex': 'Мужчина'
            }
        ]
        report_maker.dict_to_tsv(data=_dict, output_path='test_reports/real.tsv')

        with open('test_reports/real.tsv', encoding='utf-8') as csv_file:
            real = csv_file.readlines()
            csv_file.close()

        self.assertEqual(expected, real)

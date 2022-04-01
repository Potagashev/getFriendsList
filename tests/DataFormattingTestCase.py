from unittest import TestCase

from utils import format_date_to_iso


class DataFormattingTestCase(TestCase):
    def test_format_date_to_iso(self):
        real = format_date_to_iso('01.04.2022')
        expected = '2022-04-01'
        self.assertEqual(expected, real)

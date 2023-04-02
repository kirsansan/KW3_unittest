import os.path

from jsondata.utils import *
from unittest import TestCase


class TestUtils(TestCase):
    def test_load_from_json_file(self):
        file4test = "tests/json_for_test.json"
        dict4test = [{'date': '2019-08-16T04:23:41.621065',
                      'description': 'Перевод с карты на счет',
                      'from': 'MasterCard 8826230888662405',
                      'id': 86608620,
                      'operationAmount': {'amount': '6004.00',
                                          'currency': {'code': 'RUB', 'name': 'руб.'}},
                      'state': 'EXECUTED',
                      'to': 'Счет 96119739109420349721'}]
        self.assertEqual(load_from_json_file(file4test), dict4test)

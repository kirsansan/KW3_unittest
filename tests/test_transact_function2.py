# import unittest
from unittest import TestCase, main

import transaction.functions
from transaction.functions import mask_number_of_card, account_number_hide, convert_string_to_date


class Test_CardNumber(TestCase):
    def test_card_num(self):
        self.assertEqual(transaction.functions.card_number_chop_and_hide("abcd"), "abcd")
        self.assertEqual(transaction.functions.card_number_chop_and_hide("1"), "1")

    def test_card_number16(self):
        self.assertEqual(mask_number_of_card("1234567890123456"), "1234 56** **** 3456")

    # def test_TestFunc(self):
    #     self.assertEqual(transaction.functions.selftest(), None)

    def test_account_hide(self):
        self.assertEqual(account_number_hide("12345678901234567890"), "**7890")


class Test_ConvertStringToDate(TestCase):
    def test_convert_string_to_date(self):
        self.assertEqual(str(convert_string_to_date("2018-08-17T03:57:28.607101")), "2018-08-17 03:57:28.607101")
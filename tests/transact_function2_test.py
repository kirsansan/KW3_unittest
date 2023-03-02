#import unittest
from unittest import TestCase, main

import transaction.functions
from transaction.functions import card_number_chop_and_hide, mask_number_of_card, account_number_hide


class CardNumberTest(TestCase):
    def test_card_num(self):
        self.assertEqual(transaction.functions.card_number_chop_and_hide("abcd"), "abcd")
        # self.assertTrue("1", "1")

    def test_card_number16(self):
        self.assertEqual(mask_number_of_card("1234567890123456"), "1234 56** **** 3456")

    def testTestFunc(self):
        self.assertEqual(transaction.functions.test(), None)

    def test_account_hide(self):
        self.assertEqual(account_number_hide("12345678901234567890"), "**7890")

if __name__ == '__main__':
    main()

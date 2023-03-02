from unittest import TestCase, main
from transaction.functions import mask_number_of_card


class Mask_number_of_card_test(TestCase):
    def test_card_number18(self):
        self.assertEqual(mask_number_of_card("123456789012345678"), "1234 56** **** 345678")

    def test_card_number16(self):
        self.assertEqual(mask_number_of_card("1234567890123456"), "1234 56** **** 3456")

    def test_card_number6(self):
        self.assertEqual(mask_number_of_card("111100002222333"),
                         "111100002222333")  # because too small number (15 digits)

    def test_account_number(self):
        self.assertEqual(mask_number_of_card("Счет 11110000222233334444"), 'Счет **4444')

    def test_card_number_with_words(self):
        self.assertEqual(mask_number_of_card("Master card 1111000022223333"), 'Master card 1111 00** **** 3333')

    def test_card_number_with_big_digit(self):
        self.assertEqual(mask_number_of_card("Master card 111100002222333344445555"),
                         'Master card 1111 00** **** 333344445555')


if __name__ == '__main__':
    main()

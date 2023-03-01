from unittest import TestCase, main
from transaction.functions import mask_number_of_card

class Mask_number_of_card_test(TestCase):
    def test_card_number18(self):
        self.assertEqual(mask_number_of_card("123456789012345678"),   "1234 56** **** 345678")

    def test_card_number16(self):
        self.assertEqual(mask_number_of_card("1234567890123456"), "1234 56** **** 3456")

     # def test_card_number6(self):
     #    self.assertEqual(mask_number_of_card("1111000022223333"), "1234 56** **** 3456")


if __name__ == '__main__':
    main()
from unittest import TestCase, main
from transaction.functions import mask_number_of_card, create_list_of_transactions_from_long_data
from transaction.transaction import Transaction


class MaskNumberOfCardTest(TestCase):
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


class CreateListTransaction(TestCase):
    def test_create_list_transaction(self):
        test_data = [{
            "id": 111,
            "state": "EXECUTED",
            "date": "2019-08-16T04:23:41.621065",
            "operationAmount": {
                "amount": "111.00",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "qwer",
            "from": "Muwer",
            "to": "Счет 96119739109420349721"
        }]
        # answ = create_list_of_transactions_from_long_data(test_data)
        tr = Transaction("2019-08-16T04:23:41.621065",
                     "qwer", "Muwer",
                     "Счет 96119739109420349721", "EXECUTED",
                     {"amount": "111.00", "currency": {"name": "руб.", "code": "RUB"}}, id=111)
        self.assertEqual(create_list_of_transactions_from_long_data(test_data)[0].__repr__(), tr.__repr__())


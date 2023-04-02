from transaction.transaction import Transaction
from unittest import TestCase

class Test_TransactionClass(TestCase):

    def test_get_date_and_amount(self):
        tr = Transaction("2019-08-16T04:23:41.621065",
                         "qwer", "Muwer",
                         "Счет 96119739109420349721", "EXECUTED",
                         {"amount": "111.00", "currency": {"name": "руб.", "code": "RUB"}}, id=111)
        self.assertEqual(tr.get_date_human_mode(), '16.08.2019')
        self.assertEqual(tr.get_amount_human_mode(), "111.00")


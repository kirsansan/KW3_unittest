# This is a simple Python script for learning work with pytest and unittest.
# Written by Kirill.S (pyton 20.0)

from jsondata.utils import load_from_json_file
from transaction.transaction import Transaction
from transaction.functions import create_list_of_transactions_from_long_data, convert_string_to_date, mask_number_of_card
from config.config import FILE_FOR_TRANSACTIONS
from pprint import pprint




def main():
    print(f'Hi, gays!')  # Press Ctrl+F8 to toggle the breakpoint.

    non_seek_data = load_from_json_file(FILE_FOR_TRANSACTIONS)
    pprint(non_seek_data)
    transactions_list = create_list_of_transactions_from_long_data(non_seek_data)
    pprint(transactions_list)

    one_transaction: Transaction = transactions_list[1]
    print(one_transaction)

    convert_string_to_date(one_transaction.date)
    print(one_transaction.from_)
    print(mask_number_of_card(one_transaction.from_))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

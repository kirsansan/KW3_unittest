# This is a simple Python script for learning work with pytest and unittest.
# Written by Kirill.S (pyton 20.0)

from jsondata.utils import load_from_json_file
from transaction.transaction import Transaction
from transaction.functions import create_list_of_transactions_from_long_data, convert_string_to_date, mask_number_of_card
from config.config import FILE_FOR_TRANSACTIONS, NUMBER_OF_TRANSACTIONS_FOR_PRINT
from pprint import pprint

#from transaction.transaction import Transaction

def prepare_to_print(transaction):
    """
    Пример вывода для одной операции:
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб.
    :param transaction:
    :return: f-string representation of transaction
    """
    return f"""{transaction.get_date_human_mode()}  {transaction.description} 
    {mask_number_of_card(transaction.from_)} -> {mask_number_of_card(transaction.to_)}  
    {transaction.get_amount_human_mode()} {transaction.operation_amount['currency']['name']} """

def main():
    print(f'Hi, gays! Do you want to see five last executed transactions?')

    # read the transactions from the file
    non_seek_data = load_from_json_file(FILE_FOR_TRANSACTIONS)

    # create a list of transactions
    transactions_list = create_list_of_transactions_from_long_data(non_seek_data)

    # sort the list
    transactions_list.sort(key=lambda x: convert_string_to_date(x.date),reverse=True)

    # debug the transactions
    # pprint(transactions_list[:6])

    counter_while = NUMBER_OF_TRANSACTIONS_FOR_PRINT
    for transaction in transactions_list:
        if counter_while == 0:
            break
        if transaction.state == 'EXECUTED': # only executed will be printed
            counter_while -= 1
            print(prepare_to_print(transaction))


if __name__ == '__main__':
    main()

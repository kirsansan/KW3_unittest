from transaction.transaction import Transaction
from datetime import datetime


def create_list_of_transactions_from_long_data(some_data_from_json) -> list[Transaction:]:
    """read from_long_data and fill objects like class QTransaction then append it to the list
    this list will be returned
    Format data like this example:
    'date': '2019-07-13T18:51:29.313309',
    'description': 'Перевод с карты на счет',
    'from': 'Maestro 1308795367077170',
    'id': 667307132,
    'operationAmount': {'amount': '97853.86',
                        'currency': {'code': 'RUB', 'name': 'руб.'}},
    'state': 'EXECUTED',
    'to': 'Счет 96527012349577388612'
    :param some_data_from_json: some data which load from json format
    :return: list of Transaction
    """
    trans_list = []
    for tmp_data in some_data_from_json:
        if 'from' in tmp_data.keys():  # because don't exist this fill in CREATE ACCOUNT operations
            tmp_from_ = tmp_data['from']
        else:
            tmp_from_ = ""
        if tmp_data == {}:
            continue
        one_transaction: Transaction = Transaction(id=tmp_data['id'],
                                                   date=str(tmp_data['date']),
                                                   description=tmp_data['description'],
                                                   from_=tmp_from_,
                                                   to_=tmp_data['to'],
                                                   state=tmp_data['state'],
                                                   operation_amount=tmp_data['operationAmount'])
        trans_list.append(one_transaction)
    return trans_list


def convert_string_to_date(date_in_str_format: str):
    """
    convert string to date
    :param date_in_str_format:
    :return: date
    """
    return datetime.strptime(date_in_str_format, "%Y-%m-%dT%H:%M:%S.%f")


def mask_number_of_card(card_info_in_string_format: str) -> str:
    """
    hide part of card or part of account number
    :param card_info_in_string_format:
    :return: string with hide part of number
    """
    temp_string_for_return = card_info_in_string_format
    is_account = False

    for word in card_info_in_string_format.split():
        if word.lower() in ["счет", "счёт"]:  # different hide procedure for account and card number
            is_account = True
        if word.isdigit() and len(word) >= 16:  # only for long digits
            if is_account:
                temp_string_for_return = card_info_in_string_format.replace(word, account_number_hide(word))
            else:
                temp_string_for_return = card_info_in_string_format.replace(word, card_number_chop_and_hide(word))
        else:
            # temp_string_for_return += word
            # temp_string_for_return = " ".join([temp_string_for_return, word])
            pass
    return temp_string_for_return


def account_number_hide(number_as_string: str) -> str:
    """
    hide head of number, only 4 tail
    :param number_as_string:
    :return: hided number
    """
    return "**" + number_as_string[-4:]


def card_number_chop_and_hide(number_as_string: str) -> str:
    """
    hide body of number with separate on 4-digits blocks
    :param number_as_string:
    :return: hided number (number will be chop and part of number will be hide)
    """
    if not number_as_string.isdigit():
        return number_as_string
    if len(number_as_string) == 16:
        return number_as_string[:4] + " " + number_as_string[4:6] + "** **** " + number_as_string[-4:]
    if len(number_as_string) >= 17:
        return number_as_string[:4] + " " + number_as_string[4:6] \
            + "** **** " + number_as_string[12:len(number_as_string)]
    else:   # len < 16
        return number_as_string

#
# def selftest():
#     print(account_number_hide("497854789788970"))
#     print(card_number_chop_and_hide("1234567812345678"))
#     print(card_number_chop_and_hide("123456781234567800"))
#     print(mask_number_of_card("Maestro 1234567812345678"))
#     print(mask_number_of_card("Master card 1234567812345678"))
#     print(mask_number_of_card("Счет 5897568975678965798657986897"))
#
#
# if __name__ == '__main__':
#     selftest()

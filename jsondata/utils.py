""" utils for working with json-format file"""

import json
import os
from pprint import pprint


def print_where_we_going_from(tell_me_about_you):
    """
    decorator with parameter
    :param tell_me_about_you: I guess to see where are we going from (main or module)
    :return: link to real_decorator func
    """

    def real_decorator(function):
        """
        I am real decorator, but I can use parameter from above decorator
        :param function: our function which we need to decorate
        :return: link to wrapper
        """
        def wrapper(*args):
            """ I  only decorator inside other decorator. I going to wrap your function"""
            print("я вижу что ты пришел из", tell_me_about_you)
            print("будем читать файл", *args)
            res = function(*args)  # it's our function with they arguments, and it must be returned
            print("прочитано")
            return res

        return wrapper

    return real_decorator


@print_where_we_going_from(__name__)
def load_from_json_file(filename: str = './transactions.json') -> dict:
    """ load any information from json-format file and return it"""
    if not os.path.exists(filename):
        return {}  # we did not find file and need to return nothing
        # seriously we need to create exception
    with open(filename, 'r', encoding='utf-8') as fh:  # open file
        data = json.load(fh)  # load data
    return data


# test function
def selftest():
    tr_data = load_from_json_file('./transactions.json')
    if len(tr_data) != 0:
        print("file with transactions was opened and data were loaded")
        pprint(tr_data)
    else:
        print("we have some troubles with opening file 'transactions'")


# this block for a self-test
if __name__ == '__main__':
    selftest()

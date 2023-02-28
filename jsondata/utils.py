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

        # print("я вижу что ты пришел из", tell_me_about_you)
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

    # load from file
    if not os.path.exists(filename):
        return {}  # we did not find file and need to return nothing
        # seriously we need to create exception
    with open(filename, 'r', encoding='utf-8') as fh:  # open file
        data = json.load(fh)  # load data

    fh.close()  # I know that "with" has already close file. It is a control bullet only =)
    # at this point we can decipher data and put to my structure
    # but in first version we will return all data 'as is'
    return data


# def get_student_by_pk(pk: int, data: dict = {}) -> dict:
#     """ return dict by the number of record
#         return include fields:
#         'pk' - str;
#         'full_name' - str;
#         'skills' - list of str.
#     """
#     for challanger in data:
#         if challanger['pk'] == pk:
#             return challanger
#     return None  # we can't find anything


# def get_profession_by_title(title: str, data: dict = {}) -> list:
#     """ return list of skills-strings  by the string of title"""
#     for challanger in data:
#         if challanger['title'] == title:
#             return challanger['skills']
#     print("kak ya suda popal?")  # this string will print instead exeption
#     return None
#
#
# def check_fitness(student: dict, profession: list) -> dict:
#     """ compare student by professions
#         and calculate percents of skill which have this student in list of profession
#         for instance
#         "has": ["Python", "Linux"],
#         "lacks": ["Docker, SQL"],
#         "fit_percent": 50
#     """
#     has: list[str:] = []
#     lacks: list[str:] = []
#
#     # print("вот скилы нашего студента: ", student['skills'])
#     # print("вот скилы которые хотим найти: ", profession)
#     has = list(set(student['skills']) & set(profession))
#     lacks = list(set(profession) - set(student['skills']))
#     fit_percent: int = round(100 * len(has) / len(profession), 0)
#     # [has.append(search_prof) for search_prof in profession if student['skills'] in profession['skills'] ]
#     return {'has': has, 'lacks': lacks, "fit_percent": int(fit_percent)}


# test function
def test():
    tr_data = load_from_json_file('./transactions.json')
    if len(tr_data) != 0:
        print("file with transactions was opened and data were loaded")
        pprint(tr_data)
    else:
        print("we have some troubles with opening file 'transactions'")



# this block for a self-test
if __name__ == '__main__':
    test()

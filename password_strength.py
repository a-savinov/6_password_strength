import re
import sys


def load_data(filepath):
    with open(filepath, "r", encoding='utf-8') as input_file:
        raw_text = input_file.read()
    return raw_text


def check_password_not_in_file(user_password, password_string):
    if password_string.find(user_password) == -1:
        password_check = True
    else:
        password_check = False
    return password_check


def check_password_length(user_password, min_length, max_length):
    if len(user_password) in range(min_length, max_length):
        password_check = True
    else:
        password_check = False
    return password_check


def check_password_has_digit(user_password):
    return re.search(r'[0-9]', user_password)


def check_password_has_upper(user_password):
    return re.search(r'[A-Z]', user_password)


def check_password_has_lower(user_password):
    return re.search(r'[a-z]', user_password)


def check_password_has_symbol(user_password):
    return re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', user_password)


def get_password_strength_score(user_password, min_length, max_length, raw_data):
    score = 1
    check_list = [check_password_not_in_file(user_password, raw_data),
                  check_password_length(user_password, min_length, max_length),
                  check_password_has_digit(user_password),
                  check_password_has_upper(user_password),
                  check_password_has_lower(user_password),
                  check_password_has_symbol(user_password)]
    for check in check_list:
        if check:
            score = score + 1.5
    return score


if __name__ == '__main__':
    if len(sys.argv) > 2:
        user_password = sys.argv[1]
        filename = sys.argv[2]
        min_length = 6
        max_length = 12
        raw_data = load_data(filename)
        print('You password strength score : ' + str(
            get_password_strength_score(user_password, min_length, max_length, raw_data)))
    else:
        print(
            'Not all necessary data provided \n'
            'Example: python password_strength.py <user_password> <weak_passwords_file.txt>')

import re
import sys

WEIGHT_OF_ONE_CHECK = 1.5
MIN_SCORE = 1


def load_data(filepath):
    with open(filepath, "r", encoding='utf-8') as input_file:
        raw_text = input_file.read()
    return raw_text


def check_password_not_in_file(user_password, password_string):
    return bool(password_string.find(user_password) == -1)


def check_password_length(user_password, min_length, max_length):
    return bool(min_length <= len(user_password) <= max_length)


def check_password_has_digit(user_password):
    return bool(re.search(r'[0-9]', user_password))


def check_password_has_upper(user_password):
    return bool(re.search(r'[A-Z]', user_password))


def check_password_has_lower(user_password):
    return bool(re.search(r'[a-z]', user_password))


def check_password_has_symbol(user_password):
    return bool(re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', user_password))


def get_password_strength_score(user_password, min_length, max_length, raw_data):
    check_list = [check_password_not_in_file(user_password, raw_data),
                  check_password_length(user_password, min_length, max_length),
                  check_password_has_digit(user_password),
                  check_password_has_upper(user_password),
                  check_password_has_lower(user_password),
                  check_password_has_symbol(user_password)]
    score = MIN_SCORE + sum(check_list) * WEIGHT_OF_ONE_CHECK
    return score


if __name__ == '__main__':
    if len(sys.argv) == 3:
        user_password = sys.argv[1]
        filename = sys.argv[2]
        min_length = 6
        max_length = 12
        raw_data = load_data(filename)
        print('Your password strength score : %s' % get_password_strength_score(user_password,
                                                                                min_length,
                                                                                max_length,
                                                                                raw_data))
    else:
        print(
            'Not all necessary data provided \n'
            'Example: python password_strength.py <user_password> <weak_passwords_file.txt>')

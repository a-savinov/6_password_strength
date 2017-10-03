import argparse
import re

WEIGHT_OF_ONE_CHECK = 1.5
MIN_SCORE = 1


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as input_file:
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
    return bool(
        re.search(r'[!$%^&*()_+|~\-=`{}[\]:";\'<>?,./]', user_password))


def get_password_strength_score(user_password,
                                min_length,
                                max_length,
                                raw_data):
    check_list = [check_password_not_in_file(user_password, raw_data),
                  check_password_length(user_password, min_length, max_length),
                  check_password_has_digit(user_password),
                  check_password_has_upper(user_password),
                  check_password_has_lower(user_password),
                  check_password_has_symbol(user_password)]
    score = MIN_SCORE + sum(check_list) * WEIGHT_OF_ONE_CHECK
    return score


def input_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--password', required=True,
                        help='User password for analyse')
    parser.add_argument('-f', '--file', required=True,
                        help='File with worst passwords')
    return parser


if __name__ == '__main__':
    parser = input_argument_parser()
    namespace = parser.parse_args()
    user_password = namespace.password
    filename = namespace.file
    min_length = 6
    max_length = 12
    raw_data = load_data(filename)
    print('Your password strength score : {}'.format(
        get_password_strength_score(user_password, min_length, max_length,
                                    raw_data)))

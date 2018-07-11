"""
Stephan and Sophia forget about security and use simple passwords for everything. Help Nikola develop a password security check module. The password will be considered strong enough if its length is greater than or equal to 10 symbols, it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. The password contains only ASCII latin letters or digits.

Input: A password as a string.

Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean. In the results you will see the converted results.
"""

import re


def checkio(data: str) -> bool:

    print("[a-z]: %s" % (re.compile('[a-z]+').findall(data)))
    print("[A-Z]: %s" % (re.compile('[A-Z]+').findall(data)))
    print("[0-9]: %s" % (re.compile('[0-9]+').findall(data)))
    # replace this for solution
    # return bool(len(data) > 9 and re.compile('[a-z]+').findall(data) and re.compile('[A-Z]+').findall(data) and re.compile('[0-9]+').findall(data))
    d = data
    return len(d) > 9 and d.isalnum() and not (d.islower() or d.isupper() or d.isdigit() or d.isalpha())


if __name__ == '__main__':
    print(checkio('bAse730onE4'))

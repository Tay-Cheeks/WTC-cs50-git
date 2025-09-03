"""
    IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.
    Bool: True / False
    leading zeros = invalid
    re import for working with the regEx input
    sys import for sys.exit and handling error
    match.group() : to capture and access match objects
"""

import re
import sys #for command_line input

def main():

    #call our modular function:
    print(validate(input("IPv4 Address: ")))

#function to validate/invalidate IPv4 input
def validate(ip):

    """
    An IPv4 address must have exactly 4 numbers (octets), separated by dots.
    Each number must be between 0 and 255, without leading zeros (unless it's just '0')
    """

#RegEx breakdown:
    # ^: start of string
    # (25[0-5]: matches 250 - 255
    # |2[0-4][0-9]: matches 200 - 249
    # |1[0-9][0-9] / |1[0-9]{2}: matches 100 - 199
    # |[1-9]?[0-9]): matches 0-99 but no leading zeros are allowed except a single 0. "?" makes 1-9 optional
    # (\. ...){3}: after the first octet, expect a dot + valid octet three more times.
    # (\.): expect a literal . between octets.
    # $: end of string
    # pattern = r"(...)(\. ...)x3
    pattern = r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"

    # return True if pattern matches, otherwise False
    # re.fullmatch() requires the entire input string to conform to the specified regular expression=> IPv4.
    match = re.fullmatch(pattern, ip)
    return bool(match) #True/False
    """ Other Options of return:
        1. return re.fullmatch(pattern, ip) is not None #in the RegEx of the string at hand
        2. if statement:
            if re.fullmatch(pattern, ip):
                return True
            else:
                return False
    """

if __name__ == "__main__":
    main()



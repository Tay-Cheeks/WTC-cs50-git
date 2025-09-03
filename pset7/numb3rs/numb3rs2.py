"""
Validate an IPv4 address provided via command line or input.

- IPv4 must have 4 octets, separated by dots.
- Each octet must be 0–255.
- No leading zeros allowed (except the single '0').
"""

import re
import sys  # for command-line input


def main():
    if len(sys.argv) > 2:
        print("Usage: python numb3rs.py [IPv4_ADDRESS]")
        sys.exit(1)  # exit code 1 indicates error

    # If an argument is passed, use it; else ask for input
    if len(sys.argv) == 2:
        ip = sys.argv[1]
    else:
        ip = input("IPv4 Address: ")

    if validate(ip):
        print("True")
        sys.exit(0)  # success exit
    else:
        print("False")
        sys.exit(1)  # failure exit


def validate(ip):
    """
    Validates an IPv4 address using regex.
    """

    # Regex pattern explanation:
    # ^                     → Start of string
    # (25[0-5]              → 250–255
    # |2[0-4][0-9]          → 200–249
    # |1[0-9]{2}            → 100–199
    # |[1-9]?[0-9])         → 0–99 (no leading zero unless single '0')
    # (\.(...)){3}          → repeat 3 more octets separated by dots
    # $                     → End of string
    pattern = (
        r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"
        r"(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"
    )

    return re.fullmatch(pattern, ip) is not None


if __name__ == "__main__":
    main()

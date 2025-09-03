# a function called count that expects a line of text as input as a str and returns, as an int
#he number of times that “um” appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word.
    #For instance, given text like hello, um, world, the function should return 1. Given text like yummy, though, the function should return 0

# RegEx to search in the input string for um
# doesnt have to be fromm start to end of string, we just want um
# .+ for 1 or more chars to the left

import re
import sys


def main():

    print(count(input("Input: ")))

#function to find the count of "ums"
def count(s: str) -> int: #input s as a str and output an int
    #RegEx:
        #len for count of um in input
        #re.findall: The function scans the string from left to right, and matches are returned in the order they are found, including any empty matches.
            #as a list of strings or tuples. => turn its length to the count
        #\b: to more cursor to the left from space to space around "um"
        #re.IGNORECASE: case sensitive to upper()/lower().

    pattern = len(re.findall(r'\bum\b', s, re.IGNORECASE)) #isolates the regex for 'um'
    return pattern

if __name__ == "__main__":
    main()



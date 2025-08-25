
"""Command-line arguments:
    exactly 1 argument is passed (the filename).
    If not, exit with sys.exit("Too few...") or sys.exit("Too many...").

Validate file:
    Must end with .py.
    Must exist (catch FileNotFoundError).

Read file n count LOC:
    Ignore lines that are:
        Blank (line.strip() == "")
        Comments (line.lstrip().startswith("#"))

Count everything else (including docstrings)
"""

import sys #for life command line arguments and sys.exit
import os #for checking file existance

def count_LOC(filename):
    #Counts the LOC(lines of code) in a given file, excl. blank lines and #comments
    #args: filname(str) - fame of file to be read
    #returns: an integer - num of lines of code in that file
    #raises: FileNotFoundError

    count = 0 #initialize empty counter to build on

    #open file in read mode
    with open(filename, "r") as file:
        for line in file:
            #strip whitespaces from both ends of line
            stripped = line.strip()

            #two if statements as they are independent conditions

            #skip blank lines:
            if stripped == "":
                continue

            #skip comments:
            if stripped.startswith("#"):
                continue

            #if line is valid, increment counter
            count += 1

        return count

def main():
    #handles commnad line agrs and file validation
    #call count_LOC and print result returned

    #check command line agrs
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments") #no file added
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments") #more than one file added

    #Validate File: endswith .py and exists
    filename = sys.argv[1] #get filename from command line args

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    #Count LOC
    try:
        loc = count_LOC(filename) #call reusable function above
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(loc) #print result

if __name__ == "__main__":
    main()

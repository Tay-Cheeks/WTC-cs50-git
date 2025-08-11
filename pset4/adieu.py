#prompt user for atleast 1 name
#control/cmd D once done
#Assume that the user will input at least one name.Error if no input sys.exit(1)
# bid adieu to those names, separating two names with one and, three names with two commas and one and, and
# names with commas and one and.
#new empty list to store the name input strings

#define reusable function to get names for farewell
#takes in the new list of inputted names and formats them into the farewell string

import sys
import inflect

"""The methods of the class 'engine' in module inflect.py provide plural inflections,
 singular noun inflections, “a”/”an” selection for English words, and manipulation of numbers as words."""

#create a variable to collect the plural inflections
p = inflect.engine()

#reusable function that takes in names(empty list built up by inputs)
def format_farewell(names):
    #no need for manual string operations, therefore just return what we want which is to just join the list
    #using inflect to handle the name joining
    return f"Adieu, adieu, to {p.join(names)}"

def main():
    names = []

    #While its true that theres a new list to build
    while True:
        try:
            #prompt user for input of name(s)
            name = input(" ")
            if name.strip():#if name is enter and stripped of whitespaces
                names.append(name.strip()) #append it to the new list of strings
            else: #print this if theres no entry of name(s) and user just presses enter
                print("Pleas enter valid inputs")
                #no break/sys.exit so we can loop thru again to prompt user
        except EOFError:
            break #end input on Ctrl-D/Z

    if not names: #after input ends, check if we have any names, if not print msg and exit
        print("No valid name(s) entered.")
        #stop input collection
        sys.exit(1) #break would only stop the current loop. and not the whole program with a failure msg

    farewell_msg = format_farewell(names)
    print(farewell_msg)

if __name__ == "__main__":
    main()


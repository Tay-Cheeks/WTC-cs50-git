def main():
    dollars = dollars_to_float(input("How much is the meal?"))
    percent = percent_to_float(input("What percentage would you like to tip?"))
    tip = dollars*percent
    #print the tip amount rounded to 2 decimal places
    print(f"Leave R{tip:.2f}")

#def a function to convert dollar amount in string format to float
#and remove the dollar sign
def dollars_to_float(d):
    #Convert a dollar amount arg in string format to a float.
    return float(d.replace("R", ""))

def percent_to_float(p):
    #Convert a percentage in string format to a float.
    return float(p.strip('%')) / 100

main()

"""
To add a function that'll split the bill according to each persons order in the bill total
    Define a function called split_bill:
    Prompt user for total number of people
    Create an empty dictionary to store each person's name and their order total

    For each person:
        Ask for their name
        Ask for the total amount they ordered
        Convert amount to float
        Save this info in the dictionary

    Prompt for the tip percentage
    Convert tip percentage to float

    For each person in the dictionary:
        Calculate their tip: amount * tip_percent
        Calculate their total: amount + tip
        Print their name and total amount owed (with tip)

Call split_bill
"""
def main():
    dollars = dollars_to_float(input("How much is the meal?"))
    percent = percent_to_float(input("What percentage would you like to tip?"))
    tip = dollars*percent
    #print the tip amount rounded to 2 decimal places
    print(f"Leave ${tip:.2f}")

#def a function to convert dollar amount in string format to float
#and remove the dollar sign
def dollars_to_float(d):
    #Convert a dollar amount arg in string format to a float.
    return float(d.replace("$", ""))

def percent_to_float(p):
    #Convert a percentage in string format to a float.
    return float(p.strip('%')) / 100

main()


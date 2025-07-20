""" a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting,
and treat the user’s greeting case-insensitively."""

#A function with parameter greeting that returns the amount of money based on the greeting
#if statement to check if the greeting starts with "hello"

#reusable function to determine the amount based on the greeting
def bank(greeting):
    greeting = greeting.strip().lower() #remove whitespace and convert to lowercase

    #if statements to check the greeting
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

#main function to test the bank function
def main():
    greeting = input("Greeting: ")
    amount = bank(greeting) #a variable to store the amount returned by the bank function
    print(f"${amount}") #print the amount with a dollar sign

main()

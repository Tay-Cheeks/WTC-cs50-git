"""
    prompts the user for an email address via input and then prints Valid or Invalid
"""
#import
from validator_collection import validators, errors

def main():
    user_input = input("What's your email address? ")

    #try and except to handle errors
    try:
        #validate email syntax
        if validators.email(user_input):
            print("Valid")
    except errors.InvalidEmailError:
        print("Invalid")

if __name__ == "__main__":
    main()

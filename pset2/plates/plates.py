#prompt user for vanity plate input
#valid input if it starts with 2 letters and ends with a number(s): return True, otherwise return False
#min of 3 char and max of 6 char
#no punctuation or special characters allowed
#while input is invalid, prompt user for input again
#make it uppercase
#The first number used cannot be a ‘0’.”

def validate_plate(vanity_input): #function to validate the vanity plate input
    #check if len is between 3 and 6 characters
    #we will use 'not' so we dont loop in too many times
    if not (3 <= len(vanity_input) <= 6):
        return False
    #if it starts with 2 letters
    if not (vanity_input[0].isalpha() and vanity_input[1].isalpha()): #index 0 and 1 must be letters
        return False
    #check if all chars are alphanumeric(also rules out punctuation and special characters)
    if not vanity_input.isalnum():
        return False

   #find the 1st digit in the string
    first_digit_index = None #no digit is found for now, so we set it to none
    for i, char in enumerate(vanity_input):
        if char.isdigit():
            first_digit_index = i #if the char is a digit, we store the index of the digit where it is found in the string HERE(in the variablee)
            break #stop looping once we found 1st digit and its index

    if first_digit_index is not None: #if we found a 1st digit
            #check if that first digit is '0' in the input
        if vanity_input[first_digit_index] == "0": # if the first digit is 0
            return False
        #if it has to end with a number then whatever char that comes after the first digit must also be a digit
        if not vanity_input[first_digit_index: ].isdigit(): #if next char after the first digit is not a digit
            return False

    return True #otherwise return True if all conditions are met

def main():

    vanity_input = input("Enter your vanity plate: ").strip().upper() #user input tht is stripped of leading/trailing spaces and converted to uppercase
    is_valid = validate_plate(vanity_input) #call our reusable function and pass the input in it

    if is_valid:
        print("Valid")
        #if the input is valid, we print valid and break out of the loop
    else:
        print("Invalid")

    #if the input is invalid, we print invalid and loop again to ask for input

if __name__ == "__main__":
    main() #call the main function to run the program

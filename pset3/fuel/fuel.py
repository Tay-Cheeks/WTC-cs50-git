#prompt user for a fraction formatted as x/y.
#output a percentage, rounded to the nearest whole number.
#if the percentage is 99% or greater, output "F".
#IF THE PERCENTAGE IS 1% OR LESS, OUTPUT "E".
#otherwise, output the percentage followed by "%".
#Exception handling for invalid inputs:
#ZeroDivisionError for division by zero.
#ValueError for invalid input format
#While loop to keep prompting user until a valid input is received.

def get_fuel(): #no parameters needed
    #while the loop continues, promt user for input until valid input is received
    while True:
        try:
            #prompt the user for fraction input
            #converting the input str into an int now would round it off too soon before the calculation
            #so convert later after splitting the str input
            user_input = input("input fraction: ")

            #split the input into numerator(x) and denominator(y)
            x, y = user_input.split("/") # x and y are strings split by "/"
            x = int(x) #convert the string x into integer
            y = int(y) #convert the string y into integer

            #now we are working with integers
            #if y(denominator) is zero or less than, give a ZeroDivisionError
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError #numerator cannot be greater than denominator
            if x < 0 or y < 0:
                raise ValueError #numerator and denominator cannot be negative

        #except if we do raise the errors, catch them here and prompt again(loop back)
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please try again.")
            continue #re-loop to reprompt for valid input

        #if the input is valid, calculate percentage and account for different cases
        else:
            percentage = round((x / y) * 100)


            if percentage <= 1: #if 1% or less, output "E"
                return "E"
            elif percentage >= 99: #if 99% or greater, output "F"
                return "F"
            else: #return everything else in between as a percentage
                return f"{percentage}%"
            break
        #if percent is 99% or greater, output "F"


print(get_fuel()) #I dont just wnt to call the function to run the program but print it too,hence call in print()

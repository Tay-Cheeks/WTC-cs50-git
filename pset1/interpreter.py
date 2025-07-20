""" a program that prompts the user for an arithmetic expression and then calculates
and outputs the result as a floating-point value formatted to one decimal place.
Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z"""

#reusable function called calculation with 3cparameter
def calculation(x, y, z):

    #convert x and y into int
    x = int(x)
    z = int(z)

    #y is the operator, so we check its value and perform the corresponding operation
    if y == "+":
        return float(x) + float(z)
    elif y == "-":
        return float(x) - float(z)
    elif y == "*":
        return float(x) * float(z)
    elif y == "/":
        # Check for division by zero inside this if statement first so we can handle it,otherwise it will return first the result of the division
        if float(z) == 0:
            return "Error: Division by zero"
        return float(x) / float(z)
    else:
        return "Error: Invalid operator"

def main():
    #prompt user for input and then strip it of whitespace and split it into parts
    expression = input("Enter an arithmetic expression (x y z): ").strip().split()

    #after splitting, length should be 3, therefore if not, print error message
    #and return from the function
    if len(expression) != 3:
        print("Error: Please enter exactly three parts in the format x y z.")
        return

    #unpack the parts of the expression into x, operator, and y
    x, y, z = expression

    result = calculation(x, y, z)

    # Check if the result is a string indicating an error
    if result == "Error: Division by zero":
        #if its an error message, just print it
        print(result)
    elif result == "Error: Invalid operator":
        print(result)
    else:
        print(f"The result is: {result: .1f}") #print the result formatted to one decimal place

main()  # Call the main function to execute the program






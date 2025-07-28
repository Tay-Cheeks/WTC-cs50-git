# prompt user for a string and then output a string that has stripped all the vowels from it.

#def a function that'll take the user input and strip all the vowels from it
def main():
    #prompt user for a string
    input_string = input("please enter a string: ")
    #call the strip_vowels function and pass the input_string to it
    stripped_string = strip_vowels(input_string)
    print(stripped_string)


#def a function that'll take the users input and strip all the vowels from it
def strip_vowels(input_string):
    vowels = "aeiouAEIOU"
    strng = "" #empty string to hold the result and build it up


    for char in input_string:
        if char not in vowels:#if char is not in the vowels string
            strng += char #just add the char to the new string
    return strng #return the string with the vowels stripped after loop is done


if __name__ == "__main__":
    main() #call the main function to run the program



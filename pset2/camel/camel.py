#for loop to iterate through a
# prompt user for a variable in camelCase and convert it to snake_case
#string input to convert to lower case and put an underscore before each capital letter

#reusable function to convert camelCase to snake_case
def camel_to_snake(camel_str):
    snake_str = [] #placeholder for the snake_case string to build up as we loop through the camelCase string

    for i in range(len(camel_str)): #for the range of the length of the camelCase string, so we can index it
        char = camel_str[i] #character being the index of the string items
        if char.isupper() and i != 0: #if the character is upper case and not the first character(index 0)
            # add a _ before the upper case letter
            #Each time you append(), you add one character (or more) as a string to the list of characters.
            snake_str.append("_") #append an underscore to the snake_case string
            #and then after appending, add a lower case version of the character into the new string.
            snake_str.append(char.lower())
        else: #if the character is not upper case or is the first character, just add it as is to the string
            snake_str.append(char.lower())


            #converts the list of strings into one single string by concatenating all elements with '' (empty string) as the separator.
            #join the list of characters into a single string
    return "".join(snake_str)

camel_str = input("Enter a camelCase string: ") #prompt user for a camelCase string input
#call the function to convert the camelCase string input to snake_case
snake_str = camel_to_snake(camel_str)
#print the converted snake_case string
print(camel_to_snake(camel_str)) #print the converted snake_case string



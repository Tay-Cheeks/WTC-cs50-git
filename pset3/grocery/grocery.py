#prompt user for grocry item(looping thru to get more items)
#EOFError
#output: list in uppercase, sorted alphabetically, prefix each item with number that item
#newline add: to output 1 per line
#Keyerror with .get

#reusable funcion to use in another function, no need for parameters
def get_item():
    grocery_list = {} #empty dictionary to store new list added by input to print 1(key) orange(value)

    while True: #while we still prompt for input
        try:
            item = input("").strip().upper() #get input, strip whitespace, convert to uppercase

            if item == "": #if input is empty, keep prompting
                continue
        except EOFError: #detect ctl+z/d, break the loop
            break

        #increment count of items using .get method to account for KeyError
        #if item is not in grocery_list, it will return 0, then we add 1 to it
        #assign items as keys in the dict and assign it a count as a value
        #indexing the dictionary with the item as key
        #get item from new dict list, if not in list set to 0 and then add 1 to it if in list
        grocery_list[item] = grocery_list.get(item, 0) + 1 #start indexing from 0(not there) and add 1 to it

    return grocery_list #return the grocery_list dictionary with items and their counts

def print_list(grocery_list): #function to print the grocery list
    for item in sorted(grocery_list): #for the items in grocery_list, sorted alphabetically
        #print then items count and the item name
        print(f"{grocery_list[item]} {item}")

def main():
    grocery_list = get_item() #assign the returned grocery_list to the variable grocery_list
    print_list(grocery_list) #call the print_list function to print the grocery list

if __name__ == "__main__": #if this file is run directly, not imported
    main()


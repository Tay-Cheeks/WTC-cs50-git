#prompt user for food items
#reprompted to add itemsuntil they end the order with control-d:EOFError
#add newline for next prompt
#keyerror
#display the iteem: food item and
#at the end the total cost of the order. total: $.. 2 decimal places
#input is case insensitive
#ignore input that isnt in the menu and reprompt(loop)

def get_menu():
    #return a dict of food items and their prices so we cn use it in another function
    return {
        "Baja Taco" : 4.25,
        "Burrito" : 7.50,
        "Bowl" : 8.50,
        "Nachos" : 11.00,
        "Quesadilla" : 8.50,
        "Super Burrito" : 8.50,
        "Super Quesadilla" : 9.50,
        "Taco" : 3.00,
        "Tortilla Salad" : 8.00
    }

#function to take order from the user and deliver relevant output
#parameter: menu
def take_order(menu):
    #prompt user for food and display running total
    total = 0.0 #intialize the total to add to as we go

    while True:
        try:
            item = input("Item: ").title().strip() #get input and title case it and strip whitespaces
            if item == "": #if input is empty, continue iteration
                continue
        except EOFError: #if user ends input with Ctrl+D to break the loop
            print() #print newline
            break


        #Use .get() to acess the values in the dict to  avoid KeyError if item isnt in the menu.
        # we are getting the price(value of the key) in relation to the item input
        price = menu.get(item)
        if price is not None: #if price of an item is in the menu
            total += price #add the price to the initialized total
            print(f"Total: ${total:.2f}") #display the total formatted to 2 decimal places
        else: #if item is not in the menu
            continue

def main():
    #to not reuse the get_menu function which will create a dict everytime we call it, we store it in a variable
    #so we can use it in the take_order function
    menu = get_menu()
    take_order(menu) #call the function to take order with the menu

if __name__ == "__main__":
    main() #call the main function to run the program


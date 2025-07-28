#for loop
# variable to prompt user for coin input
#amount due = amount due - inserted coins
# variable to store the total amount of money
#while loop executed until user put in 50cents
#mention what the user owes/is owed
#coins: 5, 10, 25 cents

def main():
    #max amount due for a coke, while loop will run until this amount is reached
    amount_due = 50

    #while the user owes money, keep prompting for coin input
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        #prompt user for coin input
        insert_coin = int(input())
        #check if the inserted coin is valid from our list of coins
        #if valid, subtract the coin value from the amount due
        if insert_coin in [5, 10, 25]:
            amount_due -= insert_coin #minuses the value of the coin from the amount due
        else:
            #if invalid, prompt user to insert a valid coin
            continue

    #otherwise, once the user has inserted enough coins, print the change owed
    print(f"Change Owed: {abs(amount_due)}")

    """We could explicitly do a loop for when the machine owes the user money: amount_due<0
       if amount_due < 0:
           print(f"Change owed: {abs(amount_due)} cents")
       else:
           print("No change owed.")
       But since we already have the absolute value of amount_due, we can just print it directly
       as change owed."""

if __name__ == "__main__":
    main()


from jar import Jar

#demo showing how the Jar class works
def main():
    #Get jar capacity from user
    #We use while True to create an infinite loop, which keeps running until we explicitly break out of it
    while True:
        try:
            capacity = int(input("Enter jar capacity: "))
            if capacity < 0:
                print("Capacity cannot be negative!")
                continue
            jar = Jar(capacity) #call Jar class capacity
            break #breaks this loop and we move onto the next
        except ValueError:
            print("Please enter a valid positive integer")

    #interactive loop
    while True:
        print(f"\nCurrent jar: {jar}")
        action = input("Do you want to deposit or withdraw cookies?(d/w/quit): ").strip().lower()

        if action == "quit":
            print("goodbye")
            break

        elif action in ("d", "deposit"):
            try:
                n = int(input("How many cookies to deposit? "))
                jar.deposit(n)
            except ValueError as e:
                print(f"Error: {e}") #e contains details about what went wrong

        elif action in ("w", "withdraw"):
            try:
                n = int(input("How many cookies to withdraw? "))
                jar.withdraw(n)
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid input. Type d/w/quit")

if __name__ == "__main__":
    main()

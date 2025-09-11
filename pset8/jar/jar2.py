from jar import Jar

def main():
    # Get jar capacity from user
    while True:
        try:
            capacity = int(input("Enter jar capacity: "))
            if capacity < 0:
                print("Capacity cannot be negative!")
                continue
            jar = Jar(capacity)
            break
        except ValueError:
            print("Please enter a valid positive integer")

    action = ""
    while action != "quit":
        print(f"\nCurrent jar: {jar} ({jar.size}/{jar.capacity} cookies)")
        action = input("Do you want to deposit or withdraw cookies? (d/w/quit): ").strip().lower()

        if action in ("d", "deposit"):
            try:
                n = int(input("How many cookies to deposit? "))
                jar.deposit(n)
            except ValueError as e:
                print(f"Error: {e}")

        elif action in ("w", "withdraw"):
            try:
                n = int(input("How many cookies to withdraw? "))
                jar.withdraw(n)
            except ValueError as e:
                print(f"Error: {e}")

        elif action == "quit":
            print("Goodbye!")

        else:
            print("Invalid input. Type d/w/quit")

if __name__ == "__main__":
    main()

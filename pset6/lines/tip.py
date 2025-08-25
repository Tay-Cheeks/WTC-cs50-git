def dollars_to_float(d):
    """Remove $ sign and convert string to float."""
    return float(d.replace("$", "").strip())

def percent_to_float(p):
    """Remove % sign and convert string to float as decimal."""
    return float(p.replace("%", "").strip()) / 100

def main():
    num_people = int(input("How many people are splitting the bill? "))
    if num_people <= 0:
        print("❌ Number of people must be at least 1.")
        return

    # Get the tip percentage
    tip_input = input("What percentage would you like to tip (e.g. 15%)? ")
    tip_percent = percent_to_float(tip_input)

    # Collect each person's bill subtotal
    subtotals = []
    for i in range(1, num_people + 1):
        bill_input = input(f"How much did person {i} spend (e.g. $25.00)? ")
        amount = dollars_to_float(bill_input)
        subtotals.append(amount)

    total_meal = sum(subtotals)
    total_tip = total_meal * tip_percent
    total_with_tip = total_meal + total_tip

    print(f"\nTotal meal cost: ${total_meal:.2f}")
    print(f"Total tip: ${total_tip:.2f}")
    print(f"Total bill (meal + tip): ${total_with_tip:.2f}\n")

    # Calculate and print each person's contribution
    for i, subtotal in enumerate(subtotals, 1):
        # Each person's share of the tip proportional to their order
        tip_share = (subtotal / total_meal) * total_tip if total_meal != 0 else 0
        total_due = subtotal + tip_share
        print(f"Person {i} pays: Meal = ${subtotal:.2f} + Tip = ${tip_share:.2f} -> Total = ${total_due:.2f}")

if __name__ == "__main__":
    main()

def main():
    fraction = input("Fraction: ")

    try:
        percentage = convert(fraction) #we get percentage when we use convert function
        print(gauge(percentage)) #print output
    except ValueError:
        print("Error")


def convert(fraction):
    try:
        x, y = fraction.split("/") #fraction has 2 parts x and y split by /
        x = int(x)
        y = int(y)

    except(ValueError, AttributeError):
        raise ValueError("x and y nust be integers in the format x/y")

    if y == 0:
        raise ZeroDivisionError("y cannot be zero")
    elif x > y:
        raise ValueError("x cannot be greater than y")

    return round((x/y)*100) #return the %


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()

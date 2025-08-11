import random

def main():
    level = get_level()
    score = 0

    # Generate and ask 10 problems
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        # Allow up to 3 tries for each problem
        for _ in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                continue  # invalid input, try again

            if answer == x + y:
                score += 1
                break  # correct, go to next problem
            else:
                print("EEE")  # incorrect answer, try again
        else:
            # Executed if loop is not broken, i.e. 3 failed attempts
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass  # ignore and prompt again

def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Level must be 1, 2, or 3")

    min_val = 10 ** (level - 1) if level > 1 else 0
    max_val = (10 ** level) - 1
    return random.randint(min_val, max_val)

if __name__ == "__main__":
    main()

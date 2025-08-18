def main():
    s = input("Enter your vanity plate: ").strip().upper()
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #rule 1-3
    if not (3 <= len(s) <= 6):
        return False
    if not s[:2].isalpha(): #from index 0 to end at 2(excl. 2)
        return False
    if not s.isalnum():
        return False

    #rule 4:fist 1st digit in str
    for i, char in enumerate(s): #for index, characters in the input must be counted
        if char .isdigit():
            if char == "0" and i == 2: #if first no. is 0(index 2)
                return False
            #of we find a num, everything else mst be a digit
            #if the substring starting at the first number contains any non-digit characters, return False
            if not s[i:].isdigit(): #This is a slice of the string s starting from index i to the end is a digit
                return False
            break #break the loop after and move on

    #otherwise return true
    return True

if __name__ == "__main__":
    main()

# prompt user for a string and then output a string that has stripped all the vowels from it.
def main():
    word = input("Enter a string: ")
    print(shorten(word))


def shorten(word):
    vowels = "aeiouAEIOU"
    return "".join(ch for ch in word if ch not in vowels) #join the v characters with ""


if __name__ == "__main__":
    main()


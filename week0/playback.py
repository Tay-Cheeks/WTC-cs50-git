def main():
    #prompt the user for input
    text = input("What's your input?")
    #variable converted takes the text variable and replaces all spaces with "..."
    converted = text.replace(" ", "...")
    #print the converted text
    print(converted)
main()

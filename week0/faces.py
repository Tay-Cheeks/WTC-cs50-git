#define a function called convert that takes a string arguement(text)
def convert(text):
    #replace :) with 🙂 and :( with ☹️ in an updated string
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "☹️")
    #returns the updated string to wherever convert() was called
    return text

def main():
    #call the convert function with user input
    user_input = input(" Say Something with an emoticon:")
    #print the result of the convert function from the users input
    print(convert(user_input))
main()

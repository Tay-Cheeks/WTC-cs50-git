#import emoji modles
import emoji

def main():
    #user input prompt
    str_input = input("Input: ")

    #convert input to emoji
    str_input = emoji.emojize(str_input, language="alias")

    #print converted string
    print(str_input)

if __name__ == "__main__":
    main()



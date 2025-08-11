#import sys, random
import sys
import random #to choose a font from the list of fonts in the module when no font is specified in the command line
import pyfiglet #to use the pyfiglet module to generate ASCII art text

#reusable function to choose font from command line args
#takes command line arguments and list of fonts to return a font name to use or print an error message
def choose_font(fonts, args):

    #if no font is psecified(arg is 0) choose a random font from the list of fonts
    if len(args) == 0:
        return random.choice(fonts)

    #if thers 2 args(index 1 and 2 => 2 elements)
    #i.e. args == ['-f', 'slant']
    elif len(args) == 2:
        #assign element 1(index 1) to flag and 2 to font name
        flag, font = args #unpack arg into 2 separate variables

        # if flag is not in the list and isnt either item or if font is not in fonts
        if flag not in ["-f" , "--font"] or font not in fonts:
            print("Invalid usage")
            sys.exit(1) #exit program with an error

        #otherwise if both args elements are present, return font
        #so we call it in main() and use it to print our output
        return font

    else:
        #if number of args is not 0 or 2, print an error message and exit
        print("Invalid usage")
        sys.exit(1)


def main():
    #from pyfiglet, we create a Figlet object to create the font art
    figlet = pyfiglet.Figlet()

    #get list of available fonts by calling fonts parameter and store in here
    fonts = figlet.getFonts()

    #extract command_line args(exluding index 0 : the name of the file)
    args = sys.argv[1:] #start nidexing from 1 to the end of the arg

    #call choose_font function to get the font in question
    font_choice = choose_font(fonts, args)

    #tell pyfiglet to use/set the chosen font
    figlet.setFont(font = font_choice)

    #prompt user for args
    user_input = input("Input: ")

    result = figlet.renderText(user_input)

    print(result)

if __name__ == "__main__":
    main()

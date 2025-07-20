"""implement a program that prompts the user for the answer
to the Great Question of Life, the Universe and Everything and output Yes if the input(answer is 42 or
(case-insensitively) forty-two or forty two) or No otherwise"""

#def a boolean function that returns True if the input is 42 or forty-two or forty two
def is_great_answer(answer):
    # type: str -> bool
    answer = answer.strip().lower() # I want the parameter to be stripped of white spaces and lowercased
    return answer == "42" or answer == "forty-two" or answer == "forty two" # return True if the answer is 42 or forty-two or forty two

def main(): #this function will deliver my prev. reusable function above
    # define a variable answer and assign it the input from the user
    answer = input("What is the answer to the Great Question of like, the unniverse and everything?")
    #if the answer is great, print Yes, otherwise print No

    #output if statement
    if is_great_answer(answer):
        print("Yes")
    else:
        print("No")

    #call the main function to run the programme
main()


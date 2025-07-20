"""a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time,
or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s
input will be formatted in 24-hour time as #:## or ##:##.
And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00,
or anytime in between, it’s time for breakfast"""

def main():
    #variable called time_str that will hold the user input
    time_str = input("What time is it? (24 hr format)").strip()

    #need to convert the time_str into a float before we can compare it to the meal times
    time = convert(time_str)

    #if time is greater than or equal to 7 and less than and equal to 8
    if 7 <= time <= 8:
        print("breakfast time")
    #if time is greater than or equal to 12 and less than and equal to 13
    elif 12 <= time <= 13:
        print("lunch time")
    #if time is greater than or equal to 17 and less than and equal to 19
    elif 18 <= time <= 19:
        print("dinner time")


#function to convert time into mins
def convert(time_str):
    #2 varibales to hold hours and minutes, split by :
    hours, minutes = time_str.split(":")
    #return hours and minutes as a fraction of hours
    return int(hours) + int(minutes)/60

#Only run the code below if this file is being run directly (not imported as a module)
if __name__ == "__main__":
    main()



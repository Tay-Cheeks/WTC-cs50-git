"""
- prompt user for DOB in YYYY-MM-DD format
- Assume the user was born at 00:00:00 on that date, and also assume the current time is midnight today (use datetime.date.today()).
- Compute how many mins have passed between those 2 dates(midnights)
- Print that integer as English words (not numerals) in the style of the Rent song
- exit via sys.exit (the program must not raise unhandled exceptions).

Input handling:
- parse function to break it up into 3 parts and return a datetime.date.

Computing:
- mins between the 2 dates: from start_date midnight to end_date midnight(2 args).
- Use end_date - start_date to get a timedelta, convert days → minutes, return rounded integer
- Out of range dates: ValueError and let main() call sys.exit().

number_to_words_no_and(n: int) -> str
- Convert the integer n to English words, ensuring there is no “and” in the result.
- Use the inflect library (e.g., inflect.engine().number_to_words) with the option to suppress the “and” word (e.g., andword="") so the output matches the requirement.
- Ensure consistent casing (lowercase) and handle edge cases like 0.
- format_minutes_line(words: str) -> str
- Format the final string to print

def main():
- Prompt user for input.
- Call parse_birthdate; on ValueError, sys.exit.
- Compute today = date.today().
- Compute minutes via minutes_between_dates.
- Convert to words with number_to_words_no_and.
- Print the final lyric-style line.
"""


from datetime import date
import sys
import inflect


p = inflect.engine()

def main():
    try:
        date_str = input("Date of Birth: ")
    except EOFError:
        # No input available (e.g., during automated tests)
        return

    try:
        dob = parse_DOB(date_str)
    except ValueError:
        sys.exit(1)

    today = date.today() #today at midnight
    minutes = mins_between(dob, today)
    words = num_english(minutes)
    output = format_words(words)
    print(output)

    sys.exit(0)

def parse_DOB(date_str: str) -> date:
    #Parse YYYY-MM-DD date into date object. Raise ValueError if invalid as per iso format
    #ISO format only (YYYY-MM-DD)
    birthdate = date.fromisoformat(date_str)
    return birthdate #date object


def mins_between(start_date: date, end_date: date) -> int:
    #calc mins lapsed(midnight to midnight)
    delta = end_date - start_date
    return round(delta.days * 24 * 60)

def num_english(n: int) -> str:
    #convert integer to str/words without "and".
    word = p.number_to_words(n, andword="")
    return word[0].upper() + word[1:]

def format_words(words: str) -> str:
    #format output string into f"{n} minutes"
    return f"{words} minutes"

if __name__ == "__main__":
    main()

# Function: convert
# expects a str in any of the 12-hour formats
# returns the corresponding str in 24-hour format
# AM and PM will be capitalized, there will be a space before each
"""
input format:
9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM

invalid format / time error: ValueError

the regex doesn’t require minutes, and if they’re missing, the program can default them to "00" when converting to 24-hour format.
"""
import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s: str) -> str: #str parameter and the function should return a str
    #RegEx pattern matches:
        # "r ^(\d{1,2}): start of the str pattern capturing 1 or 2 decimal digits(1, 13)
        # (?::(\d{2}))?: non-capturing 2 decimal digit minutes -> read literal ':' and its optional
            #the non-capturing behaviour comes from the fact that if it’s missing, match.group(n) for that group returns None
        # (AM|PM): AM or PM
        # to : matches the literal 'to' in the str input
        # (\d{1,2})
        # (?::(\d{2}))? 9 AM or 9:00 AM
        # (AM|PM)$
        # The non-capturing group as a capturing group inside of it which will be numbered(the minutes)

    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s, re.IGNORECASE) #flag to accept any am/pm format but returns upper()

    #invert what we want
    if not match:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = match.groups()

    #default minutes to 00 if not spcified/None
    m1 = int(m1) if m1 is not None else 00
    m2 = int(m2) if m2 is not None else 00
    h1 = int(h1)
    h2 = int(h2)
    p1 = p1.upper()
    p2 = p2.upper()

    #validate ranges
    if not (1 <= h1 <= 12) or not (0 <= m1 < 60): #if hrs arent between 1 and 12 and mins between 0 and 60
        raise ValueError

    if not (1 <= h2 <= 12) or not (0 <= m2 < 60):
        raise ValueError


    #convert to 24 hour format
    h1 = to_24hr_format(h1, p1)
    h2 = to_24hr_format(h2, p2)

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"
    # : --> intros a format specification
    # 0 --> pad with zeros if needed
    # 2 --> at least 2 digits wide

def to_24hr_format(hour: int, period: str) -> int:
    period = period.upper()
    if period == "AM":
     #midnight edge case
        return 0 if hour == 12 else hour

    elif period == "PM":
        return hour if hour == 12 else hour + 12
        """if hour != 12:
            return hour + 12 #add 12 to the hour to deal with PM sessions
        return 12 #otherwise return 12"""

    else:
        raise ValueError

if __name__ == "__main__":
    main()

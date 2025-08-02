#prompt user for day input formated as MM/DD/YYYY
#format output YYYY-MM-DD
#split input with / to account for month, day, year individually
#convert month, day, year to integers

#list of full months for validation and formatting
MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#functiont to parse numeric date input
def parse_numeric_date(date_input):
    try:
        #split input by / and strip whitespace
        month, day, year = date_input.strip().split("/")

        #store integer values of month, day, year
        month = int(month)
        day = int(day)
        year = int(year)

        if 1 <= month <= 12 and 1 <= day <= 31 and year >= 0:
            #return  year,, month, day in YY/MM/DD format
            return year, month, day #return as tuple
    except (ValueError, IndexError): #raise error if input is invalid
        return None #return None by catching invalid date format or wrong month name
    return None

#function to parse text date input: Month Day, year
def parse_text_date(date_input):
    try:
        if "," not in date_input:
            return None
        #split input at comma from the right only once and strip whitespace into month and day, year
        month_day, year = date_input.rsplit(",", 1)

        #split month_day into month and day
        month_name, day = month_day.strip().split()

        #strip whitespace from year
        year = year.strip() #strip whitespace from year

        #convert month to integer
        month = MONTHS.index(month_name) + 1 #index thru MONTHS list with month_name to get month index and since index starts at 0, add 1 to get month number
        day = int(day) #convert day to integer
        year = int(year) #convert year to integer

        if 1 <= month <= 12 and 1 <= day <= 31 and year >= 0:
            return year, month, day  #return as tuple
    except (ValueError, IndexError): #raise error if input is invalid
        return None
    return None  #return None by catching invalid date format or wrong month name


#function to keep prompting user for input until valid date is entered
def valid_input():
    while True:
        date_input = input("Date: ").strip()

        #try numeric date first then textual
        result = parse_numeric_date(date_input) or parse_text_date(date_input)
        if result:
            return result #return the valid date tuple

#function to format date with padding and print
def format_date(year, month, day):
    formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
    print(formatted_date)

def main():
    #get valid date input from user returned as tuple result
    year, month, day = valid_input()
    #format and print the date
    format_date(year, month, day)

if __name__ == "__main__":
    main()




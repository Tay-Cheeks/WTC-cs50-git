#reads a CSV file with pizza orders and outs a ASCII table with the orders using tabulate library

import csv #to read the csv file
import sys #for command line args and sys.exit
from tabulate import tabulate #for ASCII table

#reusable function to read CSV file and return a list of strings
#Args: filename(str): name if CSV file
#Returns: a list: each row of CSV file as a list of strings

def read_csv(filename):

    #empty list to store rows
    rows = []

    #open the file
    with open(filename) as file:
        reader = csv.reader(file) #csv reader object to read the csv file
        for row in reader: #iterate over each row in file
            rows.append(row) #append the new list with the row
    return rows

#main function to hande:
#1. command line args#
#2. read CSV file and validate input
#3. print ASCII table
def main():

    #validte command line args
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1] #get filename from command line args

#Validate file extension
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

#read CSV file
    try:
        rows = read_csv(filename) #call read_csv
    except FileNotFoundError:
        sys.exit("File does not exist")

#validate CSV content
    if len(rows) == 0:
        sys.exit("CSV file is empty")

# extract header and data
    headers = rows[0] # forst row is header, index 0
    data = rows[1:] #from index 1 to end are data rows

    print(tabulate(data, headers=headers, tablefmt = "grid")) #converts list of lists to table

if __name__ == "__main__":
    main()


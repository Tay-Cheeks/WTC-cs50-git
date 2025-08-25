#reads the before csv file with name and house and writes a new csv file with first name, last name and house

import csv
import sys
import os

def read_before_csv(input_file):
    #reads the before.csv file
    #args: filename(str): before.csv
    #returns:a list of dicttionaries with keys "first name", "last name" and "house"
    #raise filenotfounderror if file does not exist
    # since we have 2 files we're working with to call on command line, we dont have to hardcode opening the file

    with open(input_file, "r") as infile:
        reader = csv.DictReader(infile)
        return list(reader) #convert iterator to a list of dictionaries for processing

#function to split names into first and second names
def split_names(student): #parameter sudent(dict)
    """
    Splits a 'Last, First' name into a dictionary with 'first' and 'last'.
    Args:
        student (dict): Dictionary with keys 'name' and 'house'.
    Returns:
        dict: Dictionary with keys 'first', 'last', and 'house'.
    """
    last_first = student["name"]

    #1 ensures we only split into two parts: last name and everything else as first name.
    last, first = [part.strip() for part in last_first.split(",", 1)] #split "name" in dict into last ans first at the 1st comma
    return {"first": first, "last": last, "house": student["house"]} #return new dictionary with first, last and house(index thr it as we havent worked it)

#create a new csv file with first, last and name
def write_csv(output_file, students):
    #write a new csv file
    #args: output_files(str): after.csv and students(dict): list of dicts of first, last and house
    #returns:none

    fieldnames = ["first", "last", "house"] #headers for new csv file columns
    with open(output_file, "w",) as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader() #write headers for new file

        for student in students:
            writer.writerow(student) #write each student dict to new file

#main function to handle command line args, read file, process data and write new file
def main():

    #validate command line args
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    #cheeck if input file exisys
    if not input_file.endswith(".csv") or not output_file.endswith(".csv"):
        sys.exit("Not a CSV file")

    #read the before csv file
    try:
        students = read_before_csv(input_file)
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    #process each student to spllit names: list comprehension
    cleaned_students = [split_names(student) for student in students]

    #write the after csv file
    write_csv(output_file, cleaned_students)

if __name__ == "__main__":
    main()

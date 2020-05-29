import sys
import csv
from cs50 import SQL


def main():

    # Check for correct usage
    if len(sys.argv) != 2:
        print("Usage: import.py file.csv")
        return

    # Open database
    db = SQL("sqlite:///students.db")

    # Open csv with dict reader
    csvfile = open(sys.argv[1])
    reader = csv.DictReader(csvfile)

    for row in reader:
        # Check if middle name exists
        if len(row["name"].split()) == 3:
            # set names
            firstname = row["name"].split()[0]
            middlename = row["name"].split()[1]
            lastname = row["name"].split()[2]
        # else must be no middle name
        else:
            # set names with middle name as none
            firstname = row["name"].split()[0]
            middlename = None
            lastname = row["name"].split()[1]

        # insert names into db
        db.execute("INSERT INTO students (first, middle, last, house, birth) \
        VALUES (?, ?, ?, ?, ?)", firstname, middlename, lastname, row["house"], row["birth"])


main()

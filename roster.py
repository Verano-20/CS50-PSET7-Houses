import sys
from cs50 import SQL


def main():

    # Check usage
    if len(sys.argv) != 2:
        print("Usage: roster.py house")
        return

    # Open students database
    db = SQL("sqlite:///students.db")

    # Get list of all students in a given house
    houselist = db.execute(
        "SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last ASC, first ASC", sys.argv[1])

    # Print each student's details in the required format
    for i in range(len(houselist)):
        # Check if middle name is none
        if houselist[i]["middle"] == None:
            # Add name to a separate variable to simplify, exclusing middle name
            name = houselist[i]["first"] + " " + houselist[i]["last"]
        # else middle name exists
        else:
            # Add name to separate variable, including middle name
            name = houselist[i]["first"] + " " + houselist[i]["middle"] + " " + houselist[i]["last"]

        # Print name and birth year
        print(name + ", born " + str(houselist[i]["birth"]))


main()
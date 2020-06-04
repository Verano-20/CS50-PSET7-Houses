# CS50-PSET7-Houses
My solution for CS50x2020 problem set 7 - houses.

## import.py
Takes a CSV file containing a list of students' names, school houses and birth years, and import it into a SQLite database. Splits names into separate first, middle and last columns in the database.

Example usage:  
python import.py characters.csv

## roster.py
Prints a list of all students in a given house in alphabetical order by last name.

Example usage:  
python roster.py Gryffindor  
Hermione Jean Granger, born 1979  
Harry James Potter, born 1980  
Ginevra Molly Weasley, born 1981  
Ronald Bilius Weasley, born 1980  
...

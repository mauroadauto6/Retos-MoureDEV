import datetime as dt 

def friday13(month, year):
    date = dt.date(year, month, 13)
    return date.weekday() == 4

month = input("Enter a month: ")
year = input("Enter a year: ")

if friday13(int(month), int(year)):
    print(f"¡There is a Friday the 13th in {month}/{year}!")
else:
    print(f"There isn't a Friday the 13th in {month}/{year}.")
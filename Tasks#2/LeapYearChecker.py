year = int(input("Enter the year for checking \n"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Given year is a leap year")
else:
    print("Given year is not a leap year")

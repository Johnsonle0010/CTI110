## Leon Johnson

## 03/14/2024

## P3LAB

## This program will take the value entered and determined if it's a leap year.

## Declaed a variable for is_leap_year that equals fales

is_leap_year = False

# Input the year
year = int(input('Please Enter a year:' ))
##if-else statement to see if the year entered is a leap year

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    is_leap_year = True

## displays output state if year entered is a leap year base on is_leap_year 
if is_leap_year:
    print(f"{year} - leap year")
else:
    print(f"{year} - not a leap year")

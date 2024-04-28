## Leon Johnson

## 04/21/2024

## P5LAB



def days_in_feb(users_years):
   
   ## Calculates the number of days in February for a given year.

    ##users_years (int): The year for which to determine the number of days in February.

  ##  Returns:
     ##   int: Number of days in February (28 or 29 for leap years).##
    
    if users_years % 4 == 0:
        if users_years % 100 == 0:
            if users_years % 400 == 0:
                return 29  # Leap year (divisible by 400)
            else:
                return 28  # Not a leap year (divisible by 100 but not by 400)
        else:
            return 29  # Leap year (divisible by 4 but not by 100)
    else:
        return 28  # Not a leap year (not divisible by 4)

if __name__ == '__main__':
    user_input = int(input())
    print(f"{user_input} has {days_in_feb(user_input)} days in February.")

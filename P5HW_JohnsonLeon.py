#Leon Johnson

#04/25/2024

#P5HW

## This program will give the user a math quiz by generating random numbers.

# Import Random Numbers

import random
print("Welcome to Math Quiz\n\n")
#Displays the quiz menu
def display_menu():
    print("MAIN MENU")
    print("-"*20)
    print("1. Addition Random Numbers")
    print("2. Subtract Random Numbers")
    print("3. Exit")
#Ask the user to enter integers to add them.
def add_random_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result = num1 + num2
    print(f"{num1:>4}")
    print(f"+{num2:>3}\n")
#Tracks number of guesses 
    guesses = 0
    while True:
        answer = int(input("Enter your answer:\n "))
        guesses += 1
        if answer == result:
            print(f"Congratulations!!! Your answer is correct.\nNumber of guesses: {guesses}\n")
            break
        elif answer < result:
            print("Sorry, guess is too low.\n\nTry again.")
        else:
            print("Sorry, guess is too high.\n\nTry again.")
#Ask the user to enter integers to subtract them.
def subtract_random_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result = num1 - num2
    print(f"{num1:>4}")
    print(f"-{num2:>3}\n")
#Tracks number of guesses 
    guesses = 0
    while True:
        user_answer = int(input("Enter your answer:\n "))
        guesses += 1
        if user_answer == result:
            print(f"Congratulations!!! Your answer is correct.\nNumber of guesses: {guesses}\n")
            break
        elif user_answer < result:
            print("Sorry, guess is too low.\nTry again.")
        else:
            print("Sorry, guess is too high.\nTry again.")
        
#Asker user to chose a game from the game menu.
def main():
    while True:
        display_menu()
        choice = input("Please choose one of the menu options: ")
        if choice == '1':
            add_random_numbers()
        elif choice == '2':
            subtract_random_numbers()
        elif choice == '3':
            print("Thank you for playing... \nBye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
# Execute the main function 
if __name__ == "__main__":
    main()

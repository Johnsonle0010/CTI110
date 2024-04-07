##Leon Johnson

##04-06-2024

##P4LAB2



# Get input from user
first_integer = int(input())
second_integer = int(input())

# Check if second integer is less than the first
if second_integer < first_integer:
    print("Second integer can't be less than the first.")
else:
    # Output the first integer and subsequent increments of 5
    for i in range(first_integer, second_integer + 1, 5):
        print(i, end=" ")  # Output with a space after every integer

print()  # End the output with a newline

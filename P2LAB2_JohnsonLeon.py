 # Leon Johnson

 # 03/03/2024

 # P2LAB2

 # This program takes 4 floating-point and use a string format expression to convert to output.

 # Takes 4 floating-points numbers:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

 # prints product and their average with 0 digits:
print(f'{num1 * num2 * num3 * num4:.0f} {((num1 + num2 + num3 + num4) / 4):.0f}')
# prints product and their average with 4 digits
print(f'{num1 * num2 * num3 * num4:.3f} {((num1 + num2 + num3 + num4) / 4):.3f}')

 

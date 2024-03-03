# Leon Johnson

# 03/03/2024

# P2LAB1

# LAB: Driving cost (This program program will calculate the mile to gallon)


# Get the miles per gallon and cost of gas per gallon as an input.

miles_per_gallon = float(input("Enter miles per gallon: "))
cost_per_gallon = float(input("Enter cost per gallon: "))

# Take valus of cost of gas for 20, 75, and 500 miles.
gas_cost_20_miles = cost_per_gallon * 20 / miles_per_gallon
gas_cost_75_miles = cost_per_gallon * 75 / miles_per_gallon
gas_cost_500_miles = cost_per_gallon * 500 / miles_per_gallon


# Calculate and output the results with two decimal places


print(f"{gas_cost_20_miles:.2f}",f"{gas_cost_75_miles:.2f}", f"{gas_cost_500_miles:.2f}")



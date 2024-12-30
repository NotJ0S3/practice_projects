# PYTHON WEIGHT PROGRAM
# Let's create a python weight program
# First let's to ask for the user's weight
weight = float(input("What is your weight?: "))

# We also have ask for the unit to transform the weight
unit = input("Do you want to make the conversion to kilograms or pounds? (K/L): ")

# Acording to the answer we are going to make the conversion
if unit == "K":
    one_L_in_K = 0.453592
    result = weight * one_L_in_K
    unit = "Kgs."
    print(f"Your weight {weight}Lbs in kilograms is {round(result, 3)}{unit}")
elif unit == "L":
    one_K_in_L = 2.20462
    result = weight * one_K_in_L
    unit = "Lbs."
    print(f"Your weight {weight}Kgs in pounds is {round(result, 3)}{unit}")
else:
    print(f"{unit} was no valid!")

# PYTHON TEMPERATURE CONVERSION PROGRAM
# Let's create a python temperature conversion program
# We have to ask the user for the temperature
temp = float(input("What is the actual temperature🌡: "))

# We have to ask for what type of temperature the user is giving us
unit = input("Is the temperature in Celcius or Fahrenheit? (C/F): ")

# Acording with the answer we are going to do the conversion
if unit == "C":
    conversion = (temp * 9 / 5) + 32
    print(f"{temp}°C in Fahrenheit is {round(conversion, 2)}°F")
elif unit == "F":
    conversion = (temp - 32) * 5 / 9
    print(f"{temp}°F in Celcius is {round(conversion, 2)}°C")
else:
    print(f"{unit} is a invalid unit for temperature")
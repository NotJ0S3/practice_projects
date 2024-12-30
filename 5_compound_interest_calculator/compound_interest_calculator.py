# 🐍 PYTHON COMPUND INTEREST CALCULATOR 💵

# Let's create a compund interest calculator
# To calculate the final amount we have to create some variables
principle = 0    # Initial Principal Balance
rate = 0    # Interest Rate
time = 0    # Number of time periods elapsed

# We need to ask for the principle, rate and time and we have to check if the value is greater than 0,
# while is not we have to ask again
while True:
    principle = float(input("What is the principal amount?: "))
    if principle < 0:
        print("Principle have to be greater than 0")
    else:
        break

while True:
    rate = float(input("What is the interest rate amount?: "))
    if rate < 0:
        print("Rate have to be greater than 0")
    else:
        break

while True:
    time = float(input("What is the time in years?: "))
    if time < 0:
        print("Time have to be greater than 0")
    else:
        break

# Now we can to calculate the total amount whit this formula: A = P * (1 + r / n)^t
total_amount = principle * pow(1 + rate / 100, time)

print(f"The total amount after {time} year/s is: ${total_amount:.2f}")
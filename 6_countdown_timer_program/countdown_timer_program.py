# 🐍 PYTHON COUNTDOWN TIMER PROGRAM ⏰

# Let's create a python countdown program
# We will need to import the module time
import time

# Then let's to ask the user for the time in seconds
my_time = int(input("Enter the time in seconds, please:"))

# Now, we are going to create a for loop that iterate in a reverse way
# to show the countdown timer in hours, minutes and seconds
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60)
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP")
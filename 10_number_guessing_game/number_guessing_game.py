# 🐍 PYTHON NUMBER GUESSING GAME 🔢

# Let's create a python number guessing game
# We would need to impot the module random to get a random number between
# to parameters
import random

# We need variable with the attempts and the correct number
lowest_num = 1
highest_num = 10
correct_num = random.randint(lowest_num, highest_num)  
attempts = 3

# Now we have to explain the game and their rules
print("🐍 PYTHON NUMBER GUESSING GAME 🔢")
print("You have to guess the number")
print(f"The number is between {lowest_num} and {highest_num}")
print(f"And you have {attempts} attempts")

# With a while loop we are going to ask the user for a number between the parameters and
# acording with the number we will show a result
while True:
    user_option = int(input("Give me a number: "))
    
    if user_option >= lowest_num and user_option <= highest_num:
        if user_option == correct_num and attempts > 0:
            print("Thats the number! You win 🥳")
            break
        elif user_option != correct_num and attempts > 0:
            attempts -= 1
            if user_option > correct_num and attempts > 0:
                print("Too high, try again")
            elif user_option < correct_num and attempts > 0:
                print("Too low, try again")
            else:
                print("You lost! You don't have more attempts 😞")
                print(f"The number was {correct_num}")
                break
    else:
        print("Something went wrong. Try again!")

# 🐍 PYTHON  ROCK, PAPER, SCISSORS GAME 👊✋✌

# To create a rock, paper, scissors game we will need to import the module random first
import random

# We need a tuple for the posible options and variables for the score
options = ("rock", "paper", "scissors")
user_score = 0
pc_score = 0

# We will need to ask the user for their option and acording with that
# we will compare the user and pc options
# One point for who win the match and the first in get 3 points win the game

# Let's explain the game first
print("🐍 PYTHON  ROCK, PAPER, SCISSORS GAME 👊✋✌")
print("First to win 3 matchs win!")

while True:
    # Here we compare the score first to stop the game if someone won
    if user_score == 3: 
        print(f"Your score is {user_score} You won! 🥳")
        break
    elif pc_score == 3:
        print(f"Pc score is {pc_score} You lost! 😔")
        break
    
    # We declare a variable with an option of the posible options
    pc_option = random.choice(options)
    user_option = None
    
    # While the user option is not in the posible options the loop will be forever
    while user_option not in options:
        user_option = input("👊✋✌ Rock, Paper, Scissors shoot: ")
    
    # Acording if the user or pc win a match will get 1 point
    if user_option == "rock" and pc_option == "scissors":
        print(f"Pc chose ✌")
        print(f"You chose 👊")
        print("You win 🥳")
        user_score += 1
    elif user_option == "paper" and pc_option == "rock":
        print(f"Pc chose 👊")
        print(f"You chose ✋")
        print("You win 🥳")
        user_score += 1
    elif user_option == "scissors" and pc_option == "paper":
        print(f"Pc chose ✋")
        print(f"You chose ✌")
        print("You win 🥳")
        user_score += 1
    elif user_option == pc_option:
        print(f"Pc chose {pc_option}")
        print(f"You chose {user_option}")
        print("It's a tie for this match")
    else:
        print(f"Pc chose {pc_option}")
        print(f"You chose {user_option}")
        print("You lose! 😔")
        pc_score += 1
# 🐍PYTHON DICE ROLLER PROGRAM ⚂

# To create a dice roller program we would need the random module
import random

# We will need some special characters to create the dice
# ● ┌ ─ ┐ │ └ ┘

# Create the dictionarie with the dice faces
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

# We would need to ask the user for how many dice
# wants to roll and save the result on a list and
# show the total
dice = []
total = 0
num_of_dice = int(input("How many dice?:"))

# A for loop to roll each dice
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))
    
# A for loop inside another to print each line 
# of the dice in the dice art dictionarie 
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

# A for loop to sum all the totals in dice list
for die in dice:
    total += die

print(f"The total is: {total}")

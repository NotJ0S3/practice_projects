# 🐍 PYTHON CONCESSION STAND PROGRAM 🍿

# First let's create a menu

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fires": 2.50,
        "chips": 1.00,
        "pretzel": 3.00,
        "soda": 3.00,
        "lemonade": 4.25}

# We would need to track the items and the prices
# so we need to create a cart and total variables

cart = []
total = 0

# Now we have to display the menu
print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key: 10}: ${value}:.2f")
print("--------------------------")

# And acording with the item we are going to append
# the item to the cart if the food is in the menu
while True:
    food = input("Select an item (e to exit): ").lower()
    if food == "e":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("--------------------------")

# Here we are going to find the total of the food in the cart
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print("--------------------------")
print(f"Total is: ${total:.2f}")
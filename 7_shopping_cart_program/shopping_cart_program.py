# 🐍 PYTHON SHOPPING CART PROGRAM 🛒

# Let's create a shopping cart program
# We have to ask for items, amount of the item, and price of the item. 
# Also, create an option to show the items, total of items and total of price.

# First let's to declare our variables
foods = []
prices = []
quantity = []
total = []

# Now we have to show the menu and acording to the option we will add an item, delete an item,
# show items, show the total or exit.
while True:
    print("SHOPPING CART 🛒")
    print("1. Add item ✅")
    print("2. Remove item ❌")
    print("3. Show items 📄")
    print("4. Total prices 💸")
    print("5. Exit 💨")
    
    option = int(input("What do you want to do? (Select an option with the number): "))
    
    if option == 1:
        new_item = input("What is the name of the item?: ")
        new_price = float(input("What is the price of that item?: "))
        new_quantity = int(input("How many items of that item you will buy?: "))
        foods.append(new_item)
        prices.append(new_price)
        quantity.append(new_quantity)
        
    elif option == 2:
        remove_item = input("What is the name of the item you want to remove?: ")
        remove_price = float(input("What is the price of that item?: "))
        remove_quantity = int(input("How many were you going to buy?: "))
        
        if remove_item in foods and remove_price in prices and remove_quantity in quantity:
            foods.remove(remove_item)
            prices.remove(remove_price)
            quantity.remove(remove_quantity)
            print("Item added succesfully 😊")
        else:
            print("Something went wrong. Make sure of the name, price and quantity of the item 🤨")
            print(f"This is the items in the list: {foods} and their prices {prices}")
            
    elif option == 3:
        if foods == [] and prices == []:
            print("You haven't add any food or price 🤨")
        else:
            print(f"This is the list of foods: 🍎 {foods}\nAnd this is the list of prices for each food: 💵 {prices}")
        
    elif option == 4:
        for i in range(0, len(prices)):
            total.append(prices[i] * quantity[i])
                
        print(f"The total is: 💲{sum(total)} 💵")
        
    elif option == 5:
        print("Good bye! 👋")
        break
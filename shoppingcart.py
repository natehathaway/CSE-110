 
shopping_cart = []
shopping_price = []
action = 0
while action != "5":
    print("Welcome to the Shopping Cart Program!")
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    print("Please enter an action: ", end="")
    action = input()
    if action == "1":
        item = input("What item would you like to add?")
        price = int(input("what is the price of the item? "))
        shopping_cart.append(item)
        shopping_price.append(price)
        print(item.capitalize() + " has been added to the cart.")
    elif action == "2":
        print("The contents of the shopping cart are:")
        for i in range(len(shopping_cart)):
            print(f"{[i + 1]}. {shopping_cart[i]}: ${shopping_price[i]:.2f}")
    elif action == "3":
        delete = int(input("Which item would you like to remove? "))
        shopping_cart.pop(delete - 1)
        shopping_price.pop(delete - 1)
        print("Item removed.")   
    elif action == "4":
        total = sum(shopping_price)
        print(f"The total price of the items in the shopping cart is ${total:.2f}")

        
    


print("Thank you. Goodbye.")
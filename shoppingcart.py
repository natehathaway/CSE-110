 #what the program should look like

 #Welcome to the Shopping Cart Program!

#Please select one of the following: 
#1. Add item
#2. View cart
#3. Remove item
#4. Compute total
#5. Quit
#Please enter an action: 1
#What item would you like to add? bed
#'bed' has been added to the cart.

#Please select one of the following: 
#1. Add item
#2. View cart
#3. Remove item
#4. Compute total
#5. Quit
#Please enter an action: 1
#What item would you like to add? chair
#'chair' has been added to the cart.

#Please select one of the following: 
#1. Add item
#2. View cart
#3. Remove item
#4. Compute total
#5. Quit
#Please enter an action: 2
#The contents of the shopping cart are:
#bed
#chair
#blanket

#Please select one of the following: 
#1. Add item
#2. View cart
#3. Remove item
#4. Compute total
#5. Quit
#Please enter an action: 5
#Thank you. Goodbye.
 
 
#the user will be given a menu and have the ability to choose items from the menu. The options in the menu include the following:

#Add a new item
#Display the contents of the shopping cart
#Remove an item (only needed for the final project deliverable)
#Compute the total (only needed for the final project deliverable)
#Quit


#The user will be prompted to choose an option from the menu. The program will then perform the appropriate action.

#Have menu system that repeats until the user chooses quit.

#Create a list that will store the names of the items in the shopping cart.

#Complete the option to add the name of the item to the list.

#Complete the option to display the names of the items in the list.

shopping_cart = []
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
        print("What item would you like to add?")
        item = input()
        shopping_cart.append(item)
        print(item.capitalize() + " has been added to the cart.")
    elif action == "2":
        print("The contents of the shopping cart are:")
        for item in shopping_cart:
            print(item)
    


print("Thank you. Goodbye.")


#Inputs

child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
child = int(input("How many children are there? "))
adult = int(input("How many adults are there? "))
tax = float(input("What is the sales tax rate? "))

#Math

child_total = child_price * child
adult_total = adult_price * adult
grand_total = child_total + adult_total

#Subtotal

print (f"Subtotal: {grand_total}" )



#Inputs

child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
child = int(input("How many children are there? "))
adult = int(input("How many adults are there? "))
tax = float(input("What is the sales tax rate? "))

#Math

child_total = child_price * child
adult_total = adult_price * adult
sub_total = child_total + adult_total
sales_tax = sub_total * (tax/100)
total = sub_total + sales_tax


#Subtotal

print (f"Subtotal: ${sub_total:.2f}" )

#Sales Tax

print(f"Sales Tax: ${sales_tax:.2f}")

#Total

print(f"Total: ${total:.2f}")

#Payment Input

payment = float(input("What is the payment amount? "))

#Change
change = payment - total

print(f"Change: ${change:.2f}")
print("Enjoy your food! I hope it tasted good, becuase it doesn't taste good coming out of a microwave the next day!")








#Questions
from turtle import down


print("On a scale from 1-10...")
loan = int(input("How large is your loan? "))
credit = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))
decision = False

#Logic
if loan >= 5:
    if credit >= 7 and income >= 7:
        decision = True
    elif (credit >= 7 or income >= 7) and down_payment >= 5:
            decision = True
    else:
        decision = False

if loan < 5:
    if credit < 4:
        decision = False
    elif income or down_payment >= 7:
        decision = True
    elif income and down_payment >= 4:
        decision = True
    else:
        decision = False

#Display

if decision:
    print("Your loan is approved! Thanks for spending our money!")
else:
    print("Your loan was not approved. Sorry, you will have to spend your own money.")


input("press ENTER to exit")

#Create two lists, one for the names of the bank accounts, and one for the balances.

#Ask the user for the name of the bank account and then for it's current balance. Keep looping until the user types "quit" for the name of an account. For each one, add the name and the balance to the appropriate list.

#Loop through the lists using an index and display the name of the account with the balance next to it.

#Compute and display the total balance in all of the accounts and the average balance.

#Enter the names and balances of bank accounts (type: quit when done)
#What is the name of this account? checking
#What is the balance? 102.57
#What is the name of this account? savings
#What is the balance? 82.32
#What is the name of this account? emergency fund
#What is the balance? 200.00
#What is the name of this account? quit

#Account Information:
#checking - $102.57
#savings - $82.32
#emergency fund - $200.0

#Total: $384.89
#Average: $128.30



bank_accounts = []
bank_balances = []
bank_input = ""
while bank_input != "quit":
    bank_input = input("What is the name of this account?")
    bank_accounts.append(bank_input)
    if bank_input != "quit":
        bank_input = float(input("What is the balance?"))
        bank_balances.append(bank_input)

print()
for i in range(len(bank_accounts and bank_balances)):
    combined_list = bank_accounts[i]
    money = bank_balances[i]
    print(f"{i}. {combined_list:.2f} - ${money:.2f}")
print()
math = sum(bank_balances)
print(f"Total: ${math:.2f}")
count = len(bank_balances)
average = math / count
print(f"Average: ${average:.2f}")
print()

highest_account = None
highest_balance = -1
for i in range(len(bank_accounts)):
    account = bank_accounts[i]
    balance = bank_balances[i]

    if balance > highest_balance:
        highest_account = account
        highest_balance = balance

print(f"Highest balance: {highest_account:.2f} - ${highest_balance:.2f}")


again = input("Would you like to change the balance of an account? (yes/no)")
while again == "yes":
    change = int(input("What is the index of the account you want to change?"))
    change_input = input("What is the new balance?")
    bank_balances[change] = change_input
    print("Your account information is now: ")
    for i in range(len(bank_accounts and bank_balances)):
        print(f"{i}. {bank_accounts[i]:.2f} - ${bank_balances[i]:.2f}")
    again = input("Would you like to change the balance of an account? (yes/no)")

input("press ENTER to exit")
    


favorite_letter = input("What is your favorite letter? ")
word = "commitment"

for letter in word:
    if letter.lower() == favorite_letter.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()
#output is an underscore from previous program.

favorite_letter = input("What is your favorite letter? ")
word = "commitment"

for letter in word:
    if letter.lower() == favorite_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()


#stretch goal

quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

again = "yes"

while again == "yes":
    number = int(input("Please enter a number: "))
    for i, letter in enumerate(quote):
        if i % number == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    print()
    again = input("Would you like to enter another number? ")

print("Goodbye")
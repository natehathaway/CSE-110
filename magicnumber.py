from itertools import count
import random
again = "y"
while again.lower() == "y" :
    magic_number = random.randint(1, 100)


    number_guess = int(input("What is Your guess?"))
    count = 0
    while number_guess != magic_number:
        if number_guess < magic_number:
            print("Higher")
        else:
            print("Lower")
        number_guess = int(input("What is Your guess?"))
        count += 1

    print("You guessed it!")
    print(f"It took you {count} tries")

    again = input("Do you want to play again? (y/n)")


print("press ENTER to exit")





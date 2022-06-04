

#Welcome to the word guessing game!

#What is your guess? temple
#Your guess was not correct.
#What is your guess? moroni
#Your guess was not correct.
#What is your guess? mosiah
#Congratulations! You guessed it!
#It took you 3 guesses.

from itertools import count


secret_word = "nuggets"

print("Welcome to the word guessing game!")

word = input("What is your guess? ")
count = 0
while word != secret_word:
    print("Your guess was not correct.")
    word = input("What is your guess? ")
    count += 1

if word == secret_word:
    print("Congratulations! You guessed it!")
    print("It took you", count, "guesses.")


print("press ENTER to exit")
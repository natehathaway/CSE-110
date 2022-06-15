

#Welcome to the word guessing game!


from ast import While
from itertools import count


#variables
secret_word = "nuggets"
word = []
play = True

#Welcome and hint
print("Welcome to the word guessing game!")


# Fills in word with _ according to length of secret_word.
for letter in secret_word:
    print(" _", end="")
    word.append(" _")
print()
count = 0


#play loop will continue until user types "quit"
while play:
    guess = input("What is your guess? ").lower()
    count += 1
    if guess == "quit":
        break

    #Checks guess word against secret word
    for i in range(len(guess)):
        #if lettter is correct and correct place
        if enumerate(guess[i]) == enumerate(secret_word[i]):
            word[i] = secret_word[i].upper()
          
        #If letter is correct but in wrong place
        elif guess.lower()[i] in secret_word:
            word[i] = guess[i].lower()
          
    #Prints the word in it's current state.
    for letter in word:
        print(letter, end=" ")
    print()
    # Prints congratulations message after win condition.
    if guess == secret_word:
        print("Congratulations, you guessed the word!")
        print("It took you", count, "guesses.")
        break
print("Thanks for playing!")

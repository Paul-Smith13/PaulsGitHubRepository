#This program is a number guesser game.
#It allows the user to tell the computer what numbers they would like to guess between.
#The computer then selects a random number from that range and the user has to guess which number it is.
#If the user is incorrect the computer gives the user a hint, i.e. higher or lower.

from random import randint

print("""
This program allows you to select a range of numbers from which you will guess the
random number the computer has selected.
\n
The computer will give you hints as to whether you are higher or lower.
""")

lower_range = int(input("Lowest number: \n > "))
higher_range = int(input("Highest number: \n > "))
guess_range = (lower_range, higher_range)

print(f"You have chosen the number range {guess_range}.")

secret_number = randint(lower_range, higher_range)

print(f"Please guess a number between {guess_range}: ")

counter = 0
guesses_remaining = 10
guess = int(input("> "))
while guess != secret_number:
    
    counter += + 1
    guesses_remaining = 10 - counter
    print("Wrong. Please guess again.\n")
    print(f"You have guessed {counter} times. You have {guesses_remaining} guesses remaining.")
    if guess < secret_number:
        print("HINT: The secret number is higher.")
    else:
        print("HINT: The secret number is lower.")
           
    if guesses_remaining == 0:
        print(f"Wrong. \n That was your final guess. \n You are out of guesses. The number was {secret_number}")
        break
    guess = int(input("> "))
else:
    print(f"CORRECT!!! THE SECRET NUMBER WAS: {secret_number}.")


    


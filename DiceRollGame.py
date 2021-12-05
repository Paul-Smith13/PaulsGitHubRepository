#Dice Roll Game
from random import randint

def dice_roll():
    return randint(1,6)
    
def replay():
    restart = input("Would you like to reroll?")
    if restart == "yes" or restart == "y":
        replay()
    if restart == "no" or restart == "n":
        print("Exiting...")


roll = dice_roll()

print("Would you like to roll a dice?")

play_game = input("> ")

if play_game == "no":
    print("You chose not to roll a dice.")
    quit()

if play_game == "yes" or "Yes" or "y" or "Y" or "YES" or "yeah" or "Yeah":
    print(f"You rolled: \t {roll}")

replay()
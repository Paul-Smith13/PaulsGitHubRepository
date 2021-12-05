#Rock Paper Scissors game with the computer

#Imports the randint function from the random module
from random import randint


#Function that allows the computer to choose a number between 1 and 3
def computer_choice():
    comp_choice = randint(1,3)
    print("The computer chose: ", comp_choice)
    return comp_choice

def user_choice():
    player_choice = int(input("> "))
    print("You chose: ", player_choice)
    return player_choice
    

def what_beats_what(user_choice, computer_choice):
    if user_choice == 1 and computer_choice == 3:
        print("You chose Rock. The computer chose paper. Congratulations! YOU WON!!!")
    elif user_choice == 1 and computer_choice == 2:
        print("You chose Rock. The computer chose paper. YOU LOST.")
    elif user_choice == 2 and computer_choice == 3:
        print("You chose paper. The computer chose scissors. YOU LOST.")
    elif user_choice == 2 and computer_choice == 1:
        print("You chose paper. The computer chose scissors. Congratulations! YOU WON!!!")
    elif user_choice == 3 and computer_choice == 1:
        print("You chose scissors. The computer chose rock. YOU LOST.")
    elif user_choice == 3 and computer_choice == 2:
        print("You chose Scissors. The computer chose paper. Congratulations! YOU WON!!!")
    else:
        print("You both chose the same thing. DRAW.")
        

print("""This is a game of Rock, Paper, Scissors with the computer. \n
Rock = 1
Paper = 2
Scissors = 3
""")


what_beats_what(user_choice(), computer_choice())
import os
import random

def cls() :
    os.system("cls" if os.name=="nt" else "clear")

cls()

score_user, score_computer = 0,0

computer_choices = ["Stone", "Paper", "Scissors"]

while score_computer!=3 and score_user!=3 :
    print("User :", score_user, "\nComputer :",score_computer )
    print("Type Stone Paper or Scissors")
    
    user_input = str(input()).lower()
    computer_input = random.choice(computer_choices).lower()

    if user_input==computer_input :
        cls()
        print(f"You chose: {user_input.capitalize()}, Computer chose: {computer_input.capitalize()}")
        print("Same")
    elif user_input=="stone" and computer_input=="paper" :
        cls()
        print(f"You chose: {user_input.capitalize()}, Computer chose: {computer_input.capitalize()}")
        print("Computer Plus")
        score_computer += 1
    elif user_input=="stone" and computer_input=="scissors" :
        cls()
        print(f"You chose: {user_input.capitalize()}, Computer chose: {computer_input.capitalize()}")
        print("User Plus")
        score_user += 1
    elif user_input=="paper" and computer_input=="stone" :
        cls()
        print(f"You chose: {user_input.capitalize()}, Computer chose: {computer_input.capitalize()}")
        print("User Plus")
        score_user += 1
    elif user_input=="paper" and computer_input=="scissors" :
        cls()
        print(f"You chose: {user_input.capitalize()}, Computer chose: {computer_input.capitalize()}")
        print("Computer Plus")
        score_computer += 1
    elif user_input=="scissors" and computer_input=="stone" :
        cls()
        print(f"You chose: {user_input.capitalize()}, Computer chose: {computer_input.capitalize()}")
        print("Computer Plus")
        score_computer += 1
    elif user_input=="scissors" and computer_input=="paper" :
        cls()
        print(f"You chose: {user_input.capitalize()}, Computer chose: {computer_input.capitalize()}")
        print("User Plus")
        score_user += 1


if score_computer==3 :
    print("Computer Wins")
else :
    print("User Wins")





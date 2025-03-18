import os
import random

def c() :
    os.system("cls" if os.name=="nt" else "clear")

def print_opening_sequence() :
    print("Welcome to the Randomized Gambling Game")
    
    for _ in range(19) :
        print("-*", end="")
    else :
        print("-")

def print_score(score, lives) :
    print("Welcome to the Randomized Gambling Game")
    
    for _ in range(19) :
        print("-*", end="")
    else :
        print("-")

    print("\tSCORE :", score,"  LIVES :", lives, end="\n")

    for _ in range(19) :
        print("-*", end="")
    else :
        print("-")



"""
    Main 
"""

score_multiplier = 1
score = 0
lives = 3

c()
print_opening_sequence()
input("\n\nPress Enter to begin !")

while lives>0 :
    c()
    print_score(score, lives)   
    print("\n\n")
    
    while True :
        try :
            n =  int(input("Choose an Integer between 1 and 5 (both inclusive) : "))
        except ValueError :
            n = 0

        if n>5 or n<1 :
            print("[WARNING] -> Number should be between 1 and 5 (both inclusive)\n")
        else :
            break

    
    computer_choice = random.randint(1,5)
    if computer_choice == n :
        print(f"Computer Chose {n} as well. Life lost !")
        os.system("sleep 3")
        lives -= 1
        score_multiplier = 1
    else :
        print(f"You Chose {n}\nComputer Chose {computer_choice}")
        os.system("sleep 3")
        score += int(score_multiplier*1)
        score_multiplier += 10
    
print("GAME OVER !")







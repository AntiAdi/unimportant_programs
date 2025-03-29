import random
import os

def c() :
    os.system("cls" if os.name=="nt" else "clear")

c()
print("You have four options to choose from in each question :\n\t(A) (B) (C) (D)")
test_cases = int(input("Enter the number of total questions : "))
print("\nAssuming the MCQ answers to be truly random.")

answers = [0,0,0,0]
one_percent_of_test_cases = test_cases//100
percent_counter = 1
a = 0

for i in range(test_cases) :
    answers[random.randint(0,3)] += 1
    
    if i%one_percent_of_test_cases == 0 and i!=0 :
        print(f"{percent_counter}%", end=" ", flush=True)
        percent_counter += 1
        a += 1
        if a == 10 :
            print("")
            a = 0
if percent_counter!=101 :
    print(f"100%",flush=True)

print("\nAnswers :")
print(f"\tA = {answers[0]} & {(float(answers[0])*100)/test_cases}%")
print(f"\tB = {answers[1]} & {(float(answers[1])*100)/test_cases}%")
print(f"\tC = {answers[2]} & {(float(answers[2])*100)/test_cases}%")
print(f"\tD = {answers[3]} & {(float(answers[3])*100)/test_cases}%")
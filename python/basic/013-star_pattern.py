import os

def cls() :
    os.system("cls" if os.name=="nt" else "clear")

cls()

height = int(input("Star Size : "))

cls()

# Convert height to an odd integer
if height%2 == 0 :
    height += 1


for i in range(1, height+1, 2) :
    for j in range(1, int((height-i)/2) +1) :
        print(" ", end="")

    for j in range(1, i+1) :
        print("*", end="")

    print("")

for i in range(height-2, 0, -2) :
    for j in range(int((height-i)/2) +1, 1 , -1) :
        print(" ", end="")

    for j in range(i+1, 1, -1) :
        print("*", end="")

    print("")





    






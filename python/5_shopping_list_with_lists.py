import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_list (list):
    for i in range(0,len(list)):
        print(str(int(i)+1), "->"  , list[i])

shopping_list = []

clear_screen()

loop_flag = True
while(loop_flag):
    clear_screen()
    print_list(shopping_list)
    print("Type Y to add more and N to exit")
    
    if(input().lower() == "y"):
        item = input("Enter your new item : ")
        shopping_list.append(item)
    else:
        loop_flag = False
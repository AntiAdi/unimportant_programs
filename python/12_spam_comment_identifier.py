import os

def cls() :
    os.system("cls" if os.name=="nt" else "clear")


cls()


spam_checks = ["make a lot of money", "subscribe this", "buy now", "click this"]

print("Default spam checks are :", end=" ")
print(spam_checks)
print("Enter 'end' to exit, else keep adding custom spam checks and press enter after each :")

while 1 :
    user_input = (str)(input("Custom Spam Check : "))
    if(user_input.lower()=="end") :
        break
    else :
        spam_checks.append(user_input)


cls()


while 1 :
    print("Spam checks are :", end=" ")
    print(spam_checks, "\n\n")

    comment = str(input("Comment (enter 'end' to quit) : "))
    is_spam = False

    if comment.lower()=="end" :
        quit()


    for i in range(0, len(spam_checks)) :
        if comment.lower().find(spam_checks[i].lower()) != -1 :
            print("This is Spam !\n\n\n\n")
            is_spam = True
            break
    
    if is_spam == False :
        print("Not Spam !\n\n\n\n")




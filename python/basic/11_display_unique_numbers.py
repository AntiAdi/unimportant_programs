print("Keep typing numbers and pressing enter\nEnter 'END' to finish")

sett = set()

while(1) :
    input_ = (str)(input())
    if input_.lower() =="end" :
        break
    else :
        sett.add((int)(input_))
        
print("All unique numbers :\n", sett)



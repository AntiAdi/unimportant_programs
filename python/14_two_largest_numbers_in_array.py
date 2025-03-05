# def largest_num(list, index_left, current_largest) :
#     if index_left== (len(list)) :
#         return current_largest

#     if list[index_left] > current_largest :
#         return largest_num(list, index_left+1, list[index_left])
#     else :
#         return largest_num(list, index_left+1, current_largest)


# Pass not_check as +inf.
def two_largest_num(list, index_left, current_largest, not_check) :
    if index_left== (len(list)) and not_check==float("inf") :
        return current_largest, two_largest_num(list, 0, float("-inf"), current_largest)
    elif index_left== (len(list)) and not_check!=float("inf") :
        return current_largest

    if list[index_left] > current_largest  and not_check==float("inf") :
        return two_largest_num(list, index_left+1, list[index_left], not_check)
    elif list[index_left] <= current_largest  and not_check==float("inf") :
        return two_largest_num(list, index_left+1, current_largest, not_check)
    elif list[index_left] > current_largest and list[index_left]<not_check  and not_check!=float("inf") :
        return two_largest_num(list, index_left+1, list[index_left], not_check)
    else :
        return two_largest_num(list, index_left+1, current_largest, not_check)



print("Keep Entering Numbers and Press Enter after Each.\nType 'END' to Stop.")

array = []

while(1) :
    temp = input("")
    if temp.lower()=="end" :
        break
    else :
        array.append(int(temp))

print("Largest Number is :", two_largest_num(array, 0, float("-inf"), float("inf")))

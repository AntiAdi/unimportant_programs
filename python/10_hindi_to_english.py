num_of_words = (int)(input("How many words : "))

words = {}

for i in range(0, num_of_words):
    print("Word", i+1)
    eng = (str) (input("\tEnglish Word : "))
    hin = (str) (input("\tHindi Word : "))
 
    words[eng] = hin


while(1):
    num = (str)(input("Enter english word to search\n-1 to exit\n"))
    if num == "-1" :
        quit()
    else :
        if words.get(num) != None :
            print("Hindi :", words[num])
        else :
            print("Word not found!\n\n")

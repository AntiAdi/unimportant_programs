print("Who was on the titanic ?")
name1 = input()
print("And the other one ?")
name2 = input()

current_year = input("What year is it currently ?\n")

def function (name1, name2, curr_year):
    it_sank_years_before = int(int(curr_year) - 1912)
    print(name1 + " and " + name2 + " were on the Titanic that sank " + str(it_sank_years_before) + " years before.")

function(name1, name2, current_year)
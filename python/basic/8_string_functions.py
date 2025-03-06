name = "tommy shelby"

print("First name is Tommy ?", name.lower().startswith("tommy"))
print("Last name is Sharma ?", name.lower().endswith("sharma"))

#Slicing the name into a list
a_list = name.title().split(" ") 
print("Splitted name :", a_list)

num_of_spaces = name.count(" ")
print("Length of name =", len(name)-num_of_spaces)

# Making tommy a sharma
name_new = name.title().replace("Shelby", "Sharma")
print("New Name is", name_new)







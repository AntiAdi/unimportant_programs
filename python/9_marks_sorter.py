num_of_students = (int) (input ("Number of Students : "))

marks = []

for i in range(0, num_of_students):
    print("Student", i+1, "Marks :", end=" ")
    marks.append((int)(input()))

marks.sort()
print("Marks :", marks)
print("Highest Marks =", marks[-1])

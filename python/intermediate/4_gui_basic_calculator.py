from tkinter import *

#Defining functions to do the job.
def add() :
    x=float(input_1.get())
    y=float(input_2.get())
    Label(root, text=f"{x:.2f} + {y:.2f} = {x+y :.2f}", bg="black", fg="white", width=20).grid(row=2, column=0, columnspan=2)

def sub() :
    x=float(input_1.get())
    y=float(input_2.get())
    Label(root, text=f"{x:.2f} - {y:.2f} = {x-y:.2f}", bg="black", fg="white", width=20).grid(row=2, column=0, columnspan=2)

def mul() :
    x=float(input_1.get())
    y=float(input_2.get())
    Label(root, text=f"{x:.2f} x {y:.2f} = {(x*y) :.2f}", bg="black", fg="white", width=20).grid(row=2, column=0, columnspan=2)

def div() :
    x=float(input_1.get())
    y=float(input_2.get())
    Label(root, text=f"{x:.2f} / {y:.2f} = {float(float(x)/y):.2f}", bg="black", fg="white", width=20).grid(row=2, column=0, columnspan=2)



#Creating our root instance.
root = Tk()
root.title("Basic Calculator")
root.geometry("400x400")


#Creating the widgets.
input_1 = Entry(root)
input_2 = Entry(root)

add_button = Button(root, text="Add", command=add)
substract_button = Button(root, text="Substract", command=sub)
divide_button = Button(root, text="Divide", command=div)
multiply_button = Button(root, text="Multiply", command=mul)

label_1 = Label(root, text="Enter First Number")
label_2 = Label(root, text="Enter Second Number")



#Arranging widgets in grids.
input_1.grid(row=0,column=0)
input_2.grid(row=0,column=1)

label_1.grid(row=1, column=0)
label_2.grid(row=1, column=1)


divide_button.grid(row=3,column=0, columnspan=2)
multiply_button.grid(row=4,column=0, columnspan=2)
add_button.grid(row=5,column=0, columnspan=2)
substract_button.grid(row=6,column=0, columnspan=2)










#Main Loop Instance
root.mainloop()
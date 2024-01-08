from tkinter import * 
from tkinter import messagebox as bx

def submit():
    bx.showinfo("Submitted", "Thank you for submitting.") 
    master.destroy()


m = Tk()

master = Frame(bg='lightblue')
master.pack()

l1 = Label(master, text="Name: ", fg="red")
l2 = Label(master, text="Age: ", fg="blue")

l1.grid(row = 0, column = 0, pady=2)
l2.grid(row = 1, column = 0, pady=2)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row = 0, column = 1, pady=2)
e2.grid(row = 1, column = 1, pady=2)

btn = Button(master,text="Submit", command=submit)
btn.grid(row=3,column=1, pady=2)

mainloop()


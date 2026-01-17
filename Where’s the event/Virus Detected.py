from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showinfo("Alert", "Stop! Virus Found.")

Button = Button(root, text="Scan for Virus", command=msg,fg="purple",bg="white")
Button.place(x=40, y=80)

root.mainloop()
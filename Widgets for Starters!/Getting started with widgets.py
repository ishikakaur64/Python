from tkinter import *
from datetime import date

root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

lb1 = Label(text="Hey There!", fg="white", bg="#7BA8DE", height=1, width=300)

name_lb1 = Label(text="Full Name", bg="#B6F987")
name_entry=Entry()

def display():
    name = name_entry.get()
    global Message
    Message = "Welcome to the Application! /nToday's date is:"
    greet = "Hello "+name+"/n"

    text_box.insert(END, greet)
    text_box.insert(END, Message)
    text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text="Begin", command=display, height=1, bg="#2D3E4B")

lb1.pack()
name_lb1.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()
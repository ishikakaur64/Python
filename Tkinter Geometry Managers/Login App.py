from tkinter import *

root = Tk()
root.title('Login App')
root.geometry('400x400')

frame = Frame(master=root, height=200, width=360, bg="#d0efff")

lbl1 =Label (frame, text = "Full Name", bg="#186294", fg='white', width=12)
lb12 =Label (frame, text = "Email Id", bg="#C98CEA", fg='white', width=12) 
lb13=Label(frame, text = "Enter Password", bg="#ACE06D", fg='white', width=12)     

name_entry= Entry (frame)
email_entry =Entry(frame)
pass_entry= Entry (frame, show="*")

def display():
    name = name_entry.get()
    greet = "Hey "+name
    Message = "/nCongratulations for your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, Message)

textbox = Text(bg="#F8A9A9", fg="black")

btn = Button(text= "Create Account", command=display, bg="red")

frame.place(x=20,y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lb12.place(x=20, y=80)
email_entry.place (x = 1.5, y = 80 )
lb13.place (x =20, y =140 )
pass_entry.place(x = 150, y =140 )
btn.place(x=130, y = 210 )
textbox.place (y = 250)


root.mainloop()



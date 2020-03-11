
#Importing python library tkinter
from tkinter import *

window = Tk()
window.title("Welcome")

#Getting height and width of the desktop
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
print("width",width)
print("height",height)

#Setting height and width of the window
window.geometry("500x500")
window.configure(bg="white")

frm = Frame(window)
frm.pack()

lbl = Label(frm, text="Hello", font=("Times New Roman", 30))
lbl.grid(row=0, columnspan=2)
	
lbl2 = Label(frm, text="Enter Name: ", font=("Times New Roman", 20))
lbl2.grid(row=1, column=0)
	
txt = Entry(frm, width=10)
txt.grid(row=1, column=1)

#Function to be called
#on clicking the button
def clicked():
	display=("Welcome "+ txt.get())
	lbl.configure(text=display, bg="black", fg="white")
	#Destroying widgets
	lbl2.destroy()
	txt.destroy()
	btn.destroy()
	new_lbl=Label(frm, text="Thank you", font=("Times New Roman", 30))
	new_lbl.grid(row=1, column=0)
		
btn = Button(frm, text="Click me", bg="black", fg="white", bd=10, command=clicked)
btn.grid(row=2, columnspan=2)


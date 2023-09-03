# Import tkinter
from tkinter import *
from tkinter.ttk import *

# create a Tk() object
master = Tk()

# Set the gemoetry of main
master.geometry("400x200")




label = Label(master, text ="This is the main window")

label.pack(pady = 10)

# A button widget which will open a new window on button click
btn = Button(master, text ="Click to open a new window", command = openNewWindow)

btn.pack(pady = 10)

# mainloop, runs infinitely
mainloop()

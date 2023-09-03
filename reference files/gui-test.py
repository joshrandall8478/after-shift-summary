# Import tkinter
from tkinter import *
from tkinter.ttk import *

# create a Tk() object
master = Tk()

# Set the gemoetry of main
master.geometry("200x200")

# function to open a new window on button click
def openNewWindow():

    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(master)    

    # Set the title of the Toplevel widget
    newWindow.title("New Window")

    # Set the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    Label(newWindow, text ="This is a new window").pack()


label = Label(master, text ="This is the main window")

label.pack(pady = 10)

# A button widget which will open a new window on button click
btn = Button(master, text ="Click to open a new window", command = openNewWindow)

btn.pack(pady = 10)

# mainloop, runs infinitely
mainloop()

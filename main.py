# Import tkinter
from tkinter import *
from tkinter.ttk import *


# Create new task class
class task:
    def __init__(self, type, ticketNumber, location, issue, action, status):
        self.type = type
        self.ticketNumber = ticketNumber
        self.location = location
        self.issue = issue
        self.action = action
        self.status = status

# create a Tk() object
master = Tk()

# Parameters
master.title("New Summary")
master.geometry("400x200")

# Create a new window on button click to create tasks
def createTask():

    newWindow = Toplevel(master)

    newWindow.title("New Task")
    # Set window resolution
    newWindow.geometry("320x400")

    # Create dropdown menu for task type
    Label(newWindow, text="Task Type").grid(row=0, column=0, padx=20)
    type = StringVar(newWindow)
    type.set("Select a task type")
    typeDropdown = OptionMenu(newWindow, type, "Select what type of task", "Classroom Support", "Lab Support", "Housekeeping", "Other")
    typeDropdown.grid(row=0, column=1, padx=20)

    # Create input widgets with labels

    # Incident number
    Label(newWindow, text="Incident#").grid(row=1, column=0, padx=20)
    incidentNumber = Entry(newWindow)
    incidentNumber.grid(row=1, column=1, padx=20)

    # Location
    Label(newWindow, text="Location").grid(row=2, column=0, padx=20)
    location = Entry(newWindow)
    location.grid(row=2, column=1, padx=20)

    # Issue
    Label(newWindow, text="Issue").grid(row=3, column=0, padx=20)
    issue = Entry(newWindow)
    issue.grid(row=3, column=1, padx=20)

    # Action
    Label(newWindow, text="Action").grid(row=4, column=0, padx=20)
    action = Entry(newWindow)
    action.grid(row=4, column=1, padx=20)

    # Status
    Label(newWindow, text="Status").grid(row=5, column=0, padx=20)
    status = StringVar(newWindow)
    status.set("Select a status")
    statusDropdown = OptionMenu(newWindow, status, "Select current status", "Ongoing", "Resolved")
    statusDropdown.grid(row=5, column=1, padx=20)

    # Submit button
    submitTask = Button(newWindow, text="Submit Task", command=lambda: submitTask(type, incidentNumber, location, issue, action, status))
    submitTask.grid(row=6, column=1, padx=20)

    # Function to submit task
    def submitTask(type, incidentNumber, location, issue, action, status):
        # create new task object
        newTask = task(type, incidentNumber, location, issue, action, status)
        # add new task object to array
        tasks.append(newTask)
        # Print all data to console
        print(type.get())
        print(incidentNumber.get())
        print(location.get())
        print(issue.get())
        print(action.get())
        print(status.get())
        # Close window
        newWindow.destroy()



tasks = []

# Content
master.style = Style(master)
master.style.configure("My.TLabel", font=('Arial', 25))
label = Label(master, text ="After Shift Summary", style="My.TLabel")


label.pack(pady = 10)

btn = Button(master, text ="Create new task", command = createTask)

btnPadding = 10

btn.pack(pady=btnPadding)

# A button widget which will open a new window on button click
# btn = Button(master, text ="Click to open a new window", command = openNewWindow)

# btn.pack(pady = 10)

# mainloop, runs infinitely
mainloop()

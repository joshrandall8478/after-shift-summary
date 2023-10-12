# Import tkinter
from tkinter import *
from tkinter.ttk import *
import task


# def addTaskToMaster(task, taskType, ticketNumber, location, issue, action, status):
#     # Create task container that updates when new tasks are added to tasks list, and gives all details and information
#     taskContainer = Frame(master, borderwidth=2)
#     taskContainer.pack(pady = 10)

#     # Create task container content
#     taskContainerContent = Frame(taskContainer)
#     taskContainerContent.pack(pady = 10)

#     # Create task container header
#     taskContainerHeader = Frame(taskContainer)
#     taskContainerHeader.pack(pady = 10)

#     # Create task container header labels
#     taskContainerHeaderType = Label(taskContainerHeader, text="Type")
#     taskContainerHeaderType.pack(side=LEFT, padx=10)
#     taskContainerHeaderTicketNumber = Label(taskContainerHeader, text="Ticket Number")
#     taskContainerHeaderTicketNumber.pack(side=LEFT, padx=10)
#     taskContainerHeaderLocation = Label(taskContainerHeader, text="Location")
#     taskContainerHeaderLocation.pack(side=LEFT, padx=10)
#     taskContainerHeaderIssue = Label(taskContainerHeader, text="Issue")
#     taskContainerHeaderIssue.pack(side=LEFT, padx=10)
#     taskContainerHeaderAction = Label(taskContainerHeader, text="Action")
#     taskContainerHeaderAction.pack(side=LEFT, padx=10)
#     taskContainerHeaderStatus = Label(taskContainerHeader, text="Status")
#     taskContainerHeaderStatus.pack(side=LEFT, padx=10)


#     # Create task container content labels
#     taskContainerContentType = Label(taskContainerContent, text=taskType)
#     taskContainerContentType.pack(side=LEFT, padx=10)
#     taskContainerContentTicketNumber = Label(taskContainerContent, text=ticketNumber)
#     taskContainerContentTicketNumber.pack(side=LEFT, padx=10)
#     taskContainerContentLocation = Label(taskContainerContent, text=location)
#     taskContainerContentLocation.pack(side=LEFT, padx=10)
#     taskContainerContentIssue = Label(taskContainerContent, text=issue)
#     taskContainerContentIssue.pack(side=LEFT, padx=10)
#     taskContainerContentAction = Label(taskContainerContent, text=action)
#     taskContainerContentAction.pack(side=LEFT, padx=10)
#     taskContainerContentStatus = Label(taskContainerContent, text=status)
#     taskContainerContentStatus.pack(side=LEFT, padx=10)

#     # Create task container footer
#     taskContainerFooter = Frame(taskContainer)
#     taskContainerFooter.pack(pady = 10)

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
    taskType = StringVar(newWindow)
    taskType.set("Select a task type")
    typeDropdown = OptionMenu(newWindow, taskType, "Select what type of task", "Classroom Support", "Lab Support", "Housekeeping", "Other")
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
    submitTask = Button(newWindow, text="Submit Task", command=lambda: submitTask(taskType, incidentNumber, location, issue, action, status))
    submitTask.grid(row=6, column=1, padx=20)

    # Function to submit task
    def submitTask(taskType, incidentNumber, location, issue, action, status):
        # create new task object
        newTask = task(taskType, incidentNumber, location, issue, action, status)
        # add new task object to array
        tasks.append(newTask)
        # add new task to master window
        newTask.addTaskToMaster(taskType, incidentNumber, location, issue, action, status)
        # Print all data to console
        print(taskType.get())
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

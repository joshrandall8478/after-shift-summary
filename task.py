type = ""
ticketNumber = 0
location = ""
issue = ""
action = ""
status = ""

# Setters
def setType(newType):
    global type
    type = newType
def setTicketNumber(newTicketNumber):
    global ticketNumber
    ticketNumber = newTicketNumber
def setIssue(newIssue):
    global issue
    issue = newIssue
def setAction(newAction):
    global action
    action = newAction
def setStatus(newStatus):
    global status
    status = newStatus

# Getters
def getType():
    global type
    return type
def getTicketNumber():
    global ticketNumber
    return ticketNumber
def getIssue():
    global issue
    return issue
def getAction():
    global action
    return action
def getStatus():
    global status
    return status
class Task:
    def __init__(self, taskType, ticketNumber, location, issue, action, status):
        self.taskType = taskType
        self.ticketNumber = ticketNumber
        self.localtion = location
        self.issue = issue
        self.action = action
        self.status = status

    # Setters
    def setType(self, newType):
        self.taskType = newType
    def setTicketNumber(self, newTicketNumber):
        self.ticketNumber = newTicketNumber
    def setLocation(self, newLocation):
        self.location = newLocation
    def setIssue(self, newIssue):
        self.issue = newIssue
    def setAction(self, newAction):
        self.action = newAction
    def setStatus(self, newStatus):
        self.status = newStatus

    # Getters
    def getType(self):
        return self.taskType
    def getTicketNumber(self):
        return self.ticketNumber
    def getLocation(self):
        return self.location
    def getIssue(self):
        return self.issue
    def getAction(self):
        return self.action
    def getStatus(self):
        return self.status

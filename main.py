class task:
    def __init__(self, type, issue, action, status, ticketNumber):
        self.taskType = self.taskTypes[int(type)]
        self.taskIssue = issue
        self.taskAction = action
        self.taskStatus = self.taskStatuses[int(status)]
        self.taskTicketNumber = ticketNumber

    def __str__(self):
        return "Type: " + self.taskType + "\nIssue: " + self.taskIssue + "\nAction: " + self.taskAction + "\nStatus: " + self.taskStatus + "\nTicket Number: " + str(self.taskTicketNumber)
    


public class Task {

    // Private Fields
    
    private String taskType;
    private String[] taskTypes = {"Classroom Support Call", "Lab Support", "Housekeeping"};
    private String taskStatus;
    private String[] taskStatuses = {"Ongoing", "Resolved"};
    private String location;
    private String issue;
    private String action;
    private int incidentID;

    // Public Constructor

    public Task(int taskTypeNumber, String location, String issue, String action, int taskStatusNumber, int incidentID) {
        this.taskType = taskTypes[taskTypeNumber];
        this.location = location;
        this.issue = issue;
        this.action = action;
        this.taskStatus = taskStatuses[taskStatusNumber];
        this.incidentID = incidentID;
    }
    
    // Getters/Setters
    public String getTaskType() {
        return taskType;
    }
    public String getTaskStatus() {
        return taskStatus;
    }
    public String getLocation() {
        return location;
    }
    public String getIssue() {
        return issue;
    }
    public String getAction() {
        return action;
    }
    public int getIncidentID() {
        return incidentID;
    }
    public void setTaskType(int taskTypeNumber) {
        this.taskType = taskTypes[taskTypeNumber];
    }
    public void setTaskStatus(int taskStatusNumber) {
        this.taskStatus = taskStatuses[taskStatusNumber];
    }
    public void setLocation(String location) {
        this.location = location;
    }
    public void setIssue(String issue) {
        this.issue = issue;
    }
    public void setAction(String action) {
        this.action = action;
    }
    public void setIncidentID(int incidentID) {
        this.incidentID = incidentID;
    }

    
}

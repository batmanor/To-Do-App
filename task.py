import datetime
class Task():
    def __init__(self ,taskName : str,taskDueTime = None):
        today= datetime.date.today()
        if taskDueTime is None:
            taskDueTime =  today+ datetime.timedelta(days=10)
        self.taskName = taskName
        self.taskState = "Pending"
        self.creationTime = today
        self.taskDueTime = taskDueTime
    max = 0
    # setters
    def set_task_name(self,taskName:str): self.taskName = taskName
    def set_task_state(self, taskState:str): self.taskState = taskState
    def set_task_duetime(self, taskDueTime:datetime.date): self.taskDueTime = taskDueTime

    # getters
    def get_task_name(self): return self.taskName
    def get_task_state(self): return self.taskState
    def get_task_duetime(self): return self.taskDueTime
    def get_task_creation_time(self): return self.creationTime

    def __str__(self):
        return f"{self.taskName},{self.taskState},{self.creationTime},{self.taskDueTime},"

    #distructor
    def __del__(self):
        pass
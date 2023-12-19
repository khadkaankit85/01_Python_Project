# Display a menu with options such as adding a task, viewing tasks, marking tasks as completed, and quitting the application.
def menu():
    print("1. Add a Task.")
    print("2. View Tasks.")
    print("3. Marking Tasks as Completed.")
    print("4. Quit.")
    
# Task Management:

# Users should be able to add tasks with a description, due date, and priority.
# Tasks should have a status (e.g., incomplete or completed).
# def manager():
#     task=input("Task: ")
#     description=input("Description: ")  
#     due_date=input("")  
#     priority=input("")
class Task:
    def __init__(self,Task,description,due_date,not_selected,unupdated):
        self.task=Task
        self.description=description
        self.due_date=due_date
        self.priority=not_selected
        self.status=unupdated
        with open("taskproject.txt","a") as project_file:
            project_file.write(f"{self.task}-{self.description}-{self.due_date}-{self.priority}-{self.status}\n")
        
    def task_details(self):
        print(f"{self.task}: {self.description}")
        print(f"Due: {self.due_date}" )
        print(f"Status: {self.status}")
    
    
    
    
    
    
    
    
while True: 
 menu()
 selection=input("Enter Your Choice here: ")
 if int(selection)==1:
     print("Task: ")
     task=input("")
     print("Description: ")
     description=input("")
     print("due_date: ")
     due_date=input("")
     print("Priority")
     priority=input("")
     print("Status: ")
     status=input("")
     task1=Task(task,description,due_date,priority,status)
     task1.task_details()
 elif int(selection)==2:
     pass
 elif int(selection)==3:
     pass
 elif int(selection)==4:
     print("See You Around!!")
     break
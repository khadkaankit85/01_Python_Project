# Display a menu with options such as adding a task, viewing tasks, marking tasks as completed, and quitting the application.
from datetime import date
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
            project_file.write(f"{self.task}==={self.description}==={self.due_date}==={self.priority}==={self.status}\n")
        
    def task_details(self):
        print(f"{self.task}: {self.description}")
        print(f"Due: {self.due_date}" )
        print(f"Status: {self.status}")
        print()
    
    def task_viewer():
        with open("taskproject.txt","r") as tasks:
            for lines in tasks.readlines():
                newline=lines.split("===")
                print("Task: ",newline[0])
                print("Description: ",newline[1])
                print("Due Date: ",newline[2])
                print("Priority: ",newline[3])
                print("Status: ",newline[4])
                
    def ch_status():
        global full_list

        full_list=[]
        with open("taskproject.txt","r") as tasks:
            for lines in tasks.readlines():
                newline=lines.split("===")
                # print("Task: ",newline[0])
                # print("Description: ",newline[1])
                # print("Due Date: ",newline[2])
                # print("Priority: ",newline[3])
                # print("Status: ",newline[4])
                tasks_list=newline[0]
                full_list.append(tasks_list)
        print(full_list)
            
        select_one=input("Change the status of(Task Name): ").lower()
        while select_one not in full_list:
            
            print("Hint: Task should be in the list first('q' to quit)")
            select_one=input("Change the status of: ")
            if select_one=="q":
                break
        if select_one in full_list:
            
            new_status=input("Enter the new status for your task: ").lower()
            while new_status not in ["incomplete","completed"]: 
              print("Hint: enter incomplete or completed")
              new_status=input("Enter the new status for your task: ")
              
              
            # updated_task=(f"{self.task}==={self.description}==={self.due_date}==={self.priority}===completed\n")
            with open("taskproject.txt","r+") as changing_status:
        
                for lines in changing_status.readlines():
                    splitted=lines.split("===")
                    if select_one=="q":
                        break
                    elif select_one in splitted:
                        splitted.pop()
                        splitted.append(new_status)
                        print(f"Status changed to {new_status}:)\n")
                        newTask="===".join(splitted)
                        changing_status.write(newTask+"\n")
                        splitted=""
                        select_one=input("Change the status of(Task Name): ").lower()
                    
                
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
while True: 
 menu()
 selection=input("Enter Your Choice here: ")
 if int(selection)==1:
     print("Task: ")
     task=input("")
     print("Description: ")
     description=input("")
     
     
     #I wanna keep asking the user date unless he enters a correct one:)
     while True:
        print("due_date (YYYY-MM_DD): ")
        due_date_unformatted=input("")
        try:
            due_date= date.fromisoformat(due_date_unformatted)
            break
        except Exception as e:
            print(e)
            
            
     print("Priority")
     priority=input("")
     print("Status: ")
     status=input("")
     task1=Task(task,description,due_date,priority,status)
     task1.task_details()
     
 elif int(selection)==2:
     Task.task_viewer()
 
 elif int(selection)==3:
     Task.ch_status()
 
 elif int(selection)==4:
     print("See You Around!!")
     break
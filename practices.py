# from datetime import date, datetime
# date_=input("Enter date: ")
# print(type(date_))
# date_edited= date.fromisoformat(date_)
# print(dir(datetime))
# print(type(date_edited))


def task_viewer():
        with open("taskproject.txt","r") as tasks:
            for lines in tasks.readlines():
                newline=lines.split("===")
                print("Task: ",newline[0])
                print("Description: ",newline[1])
                print("Due Date: ",newline[2])
                print("Priority: ",newline[3])
                print("Status: ",newline[4])
            #  for task,description, due_date, priority, status in lines.split("==="):
            #      print(task,":",description)
            #      print(f"Due: {due_date}")
            #      print(f"Priority: {priority}")
            #      print(f"Status: {status}\n")
                 
task_viewer()
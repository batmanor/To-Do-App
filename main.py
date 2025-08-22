import datetime
import json 
from io import StringIO
from task import Task
# Simple To-Do App

def main():
    task_list = []

    programLoop(task_list)

def programLoop(task_list:list[Task]):
    print("---------- Welcome to the To-Do App! ----------")
    while True:
        print("What do you want to do?\n"
          " 1- Add a task.\n"
          " 2- Remove a task.\n"
          " 3- View all tasks.\n"
          " 4- View all done tasks.\n"
          " 5- View all pending tasks.\n"
          " 6- View all late tasks.\n"
          " 7- Refresh all tasks.\n"
          " 8- Exit the app.".title())
        print("------------------------------------------------")
        choice = input("Enter your choice: ").strip()
        match choice:
            case "1":
                add(task_list)
                if input("wanna show all tasks?(y/n): ".capitalize()).lower() == 'y':
                    view(task_list,"*")
            case "2":
                remove(task_list)
            case "3":
                view(task_list,"*")
            case "4":
                view(task_list,"Done")
            case "5":
                view(task_list,"Pending")
            case "6":
                view(task_list,"Late")
            case "7":
                refresh_tasks(task_list)
                print("all tasks refreshed.\ntasks:")
                view(task_list,"*")
            case "8":
                print("Exiting the app. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.\n")


def add(task_list:list[Task]):
    today = datetime.date.today()
    name = input("Enter the task name: ").strip()
    lifespan = input(f"Enter the task lifespan (press 'enter' for default: {10}): ").strip()
    if lifespan == '':
        days = 10
    else:
        try:
            days = int(lifespan)
            if days <= 0:
                print("Lifespan must be positive.")
                return
        except ValueError:
            print("Invalid number entered. Task not added.")
            return
    task = Task(name, today + datetime.timedelta(days=days))
    task_list.append(task)
    if len(name)>Task.max:
        Task.max = len(name)+2
        
    print(f"Task '{name}' added with due date {task.get_task_duetime()}.")



def remove(task_list:list[Task]):
    name = input("Enter the task name: ".capitalize()).lower().strip()
    for i, task in enumerate(task_list):
        if task.get_task_name().lower() == name.lower():
            del task_list[i]
            print(f"{name} deleted seccessfully".capitalize())
            return
    print(f"No task found with the name '{name}'.".capitalize())

def edit_date(task_list:list[Task]):
    today = datetime.date.today()
    name = input("Enter the task name: ".capitalize()).lower().strip()
    for i, task in enumerate(task_list):
        if task.get_task_name().lower() == name.lower():
            try:
                day_input = int(input("current end date is:{}, today:{}\nenter the new date(e.g :-1,+5,etc...): ".capitalize()).strip())
                newTime = today + datetime.timedelta(days=(day_input))
                if not is_late(newTime):
                    task.set_task_duetime(newTime)    
                else: 
                    print("you can't assign date older than today.")
                refresh_tasks(task_list)
                return
            except ValueError:
                print("Invalid date entered. date not edited.".capitalize())
                return
            except:
                print("Couldn't edit the task, try again.".capitalize())
                return
    print(f"No task found with the name '{name}'.".capitalize())

def mark_done(task_list:list[Task]):
    view(task_list,"Pending")
    name = input("Enter the task name from the above: ".capitalize()).lower().strip()
    for i, task in enumerate(task_list):
        if task.get_task_name().lower() == name.lower() and task.get_task_state()=="Pending":
            try:
                task.set_task_state("Done")
                print(f"{name} is marked as done!".capitalize())
                return
            except:
                print("Couldn't edit the task, try again.".capitalize())
                return
    print(f"No task found with the name '{name}'.".capitalize())

def is_late(maxDate:datetime.date):
    if datetime.date.today()> maxDate:
        return True
    return False

def view(task_list:list[Task],showedData:str):
    for i,task in enumerate(task_list,0):
        match showedData.lower():
            case "all"|"*": 
                print(f"{i},\t{task}.") 
            case "done":
                if task.get_task_state() == "Done":
                    print(f"{i},\t{task}.") 
            case "pending":
                if task.get_task_state() == "Pending":
                    print(f"{i},\t{task}.") 
            case "late":
                if task.get_task_state() == "Late":
                    print(f"{i},\t{task}.") 

def refresh_tasks(task_list:list[Task]):
    today = datetime.date.today()
    for task in task_list:
        if task.get_task_duetime() < today and task.get_task_state() == "Pending":
            task.set_task_state("Late") 
        if task.get_task_duetime() > today and task.get_task_state() == "Late":
            task.set_task_state("Pending") 

def update_all_tasks(task_list:list[Task]):
    today = datetime.date.today()
    for task in task_list:
        task.set_task_duetime(today+ datetime.timedelta(days=(10))) if task.get_task_state() == "Late" else None

if __name__ == "__main__":
    main()

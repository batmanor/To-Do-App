# Simple To-Do App 
#Start of taskManager class 
class TaskManager:
    def __init__(self):
        self.tasks = {} # {Name : State (Done/Pending)}
        self.longest_word = ""

    def add(self):
        task_name = input("Enter the task name: ").strip().lower()
        if task_name in self.tasks:
            print(f"'{task_name}' already exists.")
            return
        self.tasks[task_name] = "pending"
        if len(task_name) > len(self.longest_word):
            self.longest_word = task_name
        print(f"Task '{task_name}' added successfully.")

    def remove(self):
        task_name = input("Enter the task name to remove: ").strip().lower()
        if task_name not in self.tasks:
            print(f"Task '{task_name}' does not exist.")
            return
        if input("Are You Sure You Want To Remove Tha Task?(y/n)").lower() == 'y':
            del self.tasks[task_name]
            print(f"Task '{task_name}' removed successfully.")
        self.refresh_display()

    def display_all(self):
        if not self.tasks:
            print("No tasks found.\n")
            return
        print("\nAll Tasks:")
        for i, (name, state) in enumerate(self.tasks.items(), start=1):
            print(f"{i}. {name.ljust(len(self.longest_word))} : {state.capitalize()}")
        print()

    def display_done(self):
        found = False
        print("\nDone Tasks:")
        for name, state in self.tasks.items():
            if state == "done":
                print(f"{name.ljust(len(self.longest_word))} : {state.capitalize()}")
                found = True
        if not found:
            print("No done tasks.\n")

    def display_pend(self):
        found = False
        print("\nPending Tasks:")
        for name, state in self.tasks.items():
            if state == "pending":
                print(f"{name.ljust(len(self.longest_word))} : {state.capitalize()}")
                found = True
        if not found:
            print("No pending tasks.\n")

    def refresh_display(self):
        if self.tasks:
            self.longest_word = max(self.tasks, key=len)
        else:
            self.longest_word = ""
    def edit_state(self):
        pass
#End of taskManager class 

# create a global instance
task = TaskManager()

def main():
    print("---------- Welcome to the To-Do App! ----------")
    while True:
        print("What do you want to do?\n"
          " 1- Add a task.\n"
          " 2- Remove a task.\n"
          " 3- View all tasks.\n"
          " 4- View all done tasks.\n"
          " 5- View all pending tasks.\n"
          " 6- Refresh column size.\n"
          " 7- Exit the app.")  
        print("------------------------------------------------")
        choice = input("Enter your choice: ").strip()
        match choice:
            case "1":
                task.add()
                if input("wanna show all tasks?(y/n): ".capitalize()).lower() == 'y':
                    task.display_all()
            case "2":
                task.remove()
            case "3":
                task.display_all()
            case "4":
                task.display_done()
            case "5":
                task.display_pend()
            case "6":
                task.refresh_display()
                print("Column size refreshed.\n")
            case "7":
                print("Exiting the app. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

def print_menu():
    print('To-Do List Application\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit')

task_list = []

def add_task():
    task = input("Enter the task: ")
    task_list.append(task)
    print(f"'{task}' has been added to the list.")

def remove_task():
    rv_task = input("Enter the task to remove: ")
    task_list.remove(rv_task)
    print(f"'{rv_task} has been removed from the list.'")

def view_task():
    print("To-Do List:")
    for i, list in enumerate(task_list, start=1):
        print(f"{i}. {list}")

def exit_app():
    print("Exiting the application. Goodbye!")

# make sure if the input is int
def valid_int():
    choice = input("Enter your choice: ")
    if choice.isdigit() == False:
        print("Invalid input! Please enter the appropriate number.")
    else:
        choice = int(choice)

# make sure if the task to remove is in the list
def valid_rv():
    rv_task = input("Enter the task to remove: ")
    if rv_task in task_list:
        task_list.remove(rv_task)
        print(f"'{rv_task}' has been removed from the list.")
    else:
        print("The task is not in the list.")


from datetime import datetime

def print_menu():
    print('To-Do List Application\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit')


task_list = []
dict_task = {}
# dict_task = {'workout': {'priority': 'high', 'deadline': '2024-06-13', 'description': 'gym'},
#             'study': {'priority': 'medium', 'deadline': '2024-10-10', 'description': 'python'}
#              }


def new_add_task():
    while True:
        task = input("Enter the task: ")
        if task == "":
            print("Please enter a task.")
        else:
            break
    while True:
        priority = input("enter the priority (high, medium, low): ")
        if priority not in ("high", "medium", "low"):
            print("Invalid input! Please enter high, medium, or low.")
        else:
            break
    while True:
        deadline = input("enter the deadline (YYYY-MM-DD): ")
        try:
            datetime.fromisoformat(deadline)
            break
        except ValueError:
            print("Incorrect date format. It should be YYYY-MM-DD.")

    description = input("enter the description : ")

    task_sub_dict = {}
    task_sub_dict["priority"] = priority
    task_sub_dict["deadline"] = deadline
    task_sub_dict["description"] = description

    dict_task[task] = task_sub_dict

    print(f"dict_task >> {dict_task}")
    print(f"'{task}' has been added to the list.")

def add_task():
    task = input("Enter the task: ")
    task_list.append(task)
    priority = input("enter the priority (high, medium, low): ")
    deadline = input("enter the deadline (YYYY-MM-DD): ")
    description = input("enter the description : ")

    task_sub_dict = {}
    for i in task_list:
        task_sub_dict["priority"] = priority
        task_sub_dict["deadline"] = deadline
        task_sub_dict["description"] = description
        dict_task[i] = task_sub_dict

    print(f"dict_task >> {dict_task}")

    print(f"'{task}' has been added to the list.")


def remove_task():
    rm_task = input("Enter the task to remove: ")
    if rm_task in task_list:
        task_list.remove(rm_task)
        print(f"'{rm_task} has been removed from the list.'")
    else:
        print("The task is not in the list.")

def new_remove_task():
    rm_task = input("Enter the task to remove: ")

    if rm_task in dict_task:
        del dict_task[rm_task]
    else:
        print("task does not exist")
    print(f"dict_task >> {dict_task}")

def view_task():
    print("To-Do List:")
    for i, list in enumerate(task_list, start=1):
        print(f"{i}. {list}")

def new_view_task():
    print("new_view_task :")
    for k,v in dict_task.items():
        print(f"{k} : {v['priority']} - {v['deadline']} - {v['description']}")



def exit_app():
    print("Exiting the application. Goodbye!")


while True:
    print()
    print_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        # add_task()
        new_add_task()

    elif choice == '2':
        # remove_task()
        new_remove_task()

    elif choice == '3':
        # view_task()
        new_view_task()

    elif choice == '4':
        exit_app()
        break

    else:
        print("Invalid input! Please enter the appropriate number.")
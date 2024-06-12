from datetime import datetime

def print_menu():
    print('Advanced To-Do List Application\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Suggest Tasks\n5. Exit')

todo = []

def add_task():
    task_list = {}
    task_list["task"] = input("Enter the task: ")
    task = task_list["task"]
    while True:
        task_list["pri"] = input("Enter the priority (high, medium, low): ")
        if task_list["pri"] not in ["high", "medium", "low"]:
            print("Invalid input! Please enter high, medium, or low.")
        else:
            pri = task_list["pri"]
            break

    while True:
        task_list["due"] = input("Enter the deadline (YYYY-MM-DD): ")
        try:
            datetime.fromisoformat(task_list["due"])
            due = task_list["due"]
            break
        except ValueError:
            print("Incorrect date format. It should be YYYY-MM-DD.")
    print(f"'{task}' with priority '{pri}' and deadline '{due}' has been added to the list.")
    todo.append(task_list)

def remove_task():
    rm_task = input("Enter the task to remove: ")
    for i in todo:
        if i["task"] == rm_task:
            todo.remove(i)
            print(f"'{rm_task}' has been removed from the list.")
            break
    else:
        print("The task is not in the list.")

def view_task():
    print("To-Do List:")
    for i, task in enumerate(todo, start=1):
        print(f"{i}. {task['task']} - {task['pri']} - {task['due']}")

def suggest_task():
    print("Good afternoon! Here are some tasks you might want to work on: ")
    sort_pri = {'high': 0, 'medium': 1, 'low': 2}
    suggest = sorted(todo, key=lambda x: (x['due'], sort_pri[x['pri']]))
    for i in suggest:
        print(f"{i['task']} - {i['pri']} - {i['due']}")

def exit_app():
    print("Exiting the application. Goodbye!")


while True:
    print_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_task()

    elif choice == '2':
        remove_task()

    elif choice == '3':
        view_task()

    elif choice == '4':
        suggest_task()

    elif choice == '5':
        exit_app()
        break

    else:
        print("Invalid input! Please enter the appropriate number.")
    print()
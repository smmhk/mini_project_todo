from datetime import datetime

todo = []
task_list = {}

def add_task():
    task_list["task"] = input("Enter the task: ")  # enter the key
    task = task_list["task"]  # store key in task
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
    todo.append(task_list)


def remove_task():
    rm_task = input("Enter the task to remove: ")
    for i in range(len(todo)):
        if todo[i]["task"] == rm_task:
            del todo[i]
            print(f"'{rm_task}' has been removed from the list.")
        else:
            print("The task is not in the list.")


def view_task():
    print("To-Do List:")
    for i, task in enumerate(todo, start=1):
        print(f"{i}. {task['task']} - {task['pri']} - {task['due']}")
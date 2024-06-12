def print_menu():
    print('To-Do List Application\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit')


task_list = []


def add_task():
    task = input("Enter the task: ")
    task_list.append(task)
    print(f"'{task}' has been added to the list.")


def remove_task():
    rm_task = input("Enter the task to remove: ")
    if rm_task in task_list:
        task_list.remove(rm_task)
        print(f"'{rm_task} has been removed from the list.'")
    else:
        print("The task is not in the list.")


def view_task():
    print("To-Do List:")
    for i, list in enumerate(task_list, start=1):
        print(f"{i}. {list}")


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
        exit_app()
        break

    else:
        print("Invalid input! Please enter the appropriate number.")
    print()
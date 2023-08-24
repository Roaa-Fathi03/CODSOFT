# task_list = {1: 'AI', 2: 'CS', 3: 'DS', 4: 'DL', 5: 'Math', 6: 'PS'}
task_list = {}
finished_tasks = {}
count = len(task_list)
count_finished = 1


def display_task_list():
    print("=========== Task List ====================")
    for i, task in task_list.items():
        print(i, ' -> ', task)

    print('\n')


def display_finished_task_list():
    print("=========== Finished Task List ===========")
    for i, task in finished_tasks.items():
        print(i, ' -> ', task)

    print('\n')


def add_task():
    print("=========== Add Task =====================")
    task = str(input("Enter your task:"))
    global task_list, count
    count = len(task_list) + 1
    task_list[count] = task

    print("\n")


def update_task():
    print("=========== Update Task ==================")
    updated_order = int(input("Enter the task order to update: "))
    if updated_order in task_list:
        update = str(input("Enter your updated task:"))
        task_list[updated_order] = update
    else:
        print("Task order not found.")

    print('\n')


def finish_task():
    print("=========== Finish Task ==================")
    selected_order = int(input("Enter the task order to mark as done: "))
    global task_list, count_finished
    count_finished = len(finished_tasks) + 1

    if selected_order in task_list:
        finished_tasks[count_finished] = task_list[selected_order]
        del task_list[selected_order]
        task_list = list_counter(task_list)

    else:
        print("Task order not found.")

    print('\n')


def list_counter(task_dict):
    counter = 1
    new_task_list = {}
    for key, value in task_dict.items():
        new_task_list[counter] = value
        counter += 1
    return new_task_list


def delete_task():
    global task_list

    print("=========== Delete Task ==================")
    selected_order = int(input("Enter the task order to be deleted: "))

    if selected_order < len(task_list):
        print("deleted")
        del task_list[selected_order]
        task_list = list_counter(task_list)


def display_menu():
    choice = 1
    while choice < 4:
        display_task_list()
        display_finished_task_list()

        print("============ To Do Application ===========")
        print("Please choose from the list:")
        print("1. Add Task.")
        print("2. Update Task.")
        print("3. Select as done!")
        print("4. Delete Task.")
        print("5. End.")

        choice = int(input("Enter your choice: "))
        print('\n')

        if choice == 1:
            Add_task()
        elif choice == 2:
            Update_task()
        elif choice == 3:
            Finish_task()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            print("*** Thanks for using our App.***")
        else:
            print("Invalid choice.")

        print('\n')


display_menu()

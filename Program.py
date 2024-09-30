#TASK_TRACKER
#Add Task, Edit Task, Delete Task
#Task Status - In progress/Done
#List all tasks
#Filter tasks not done, in progress and done
#Task_ID, description, status, created, last_updated

import json, datetime, os

def clear_console():
    import os
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux
    else:
        os.system('clear')

file_path = 'C:\\Users\\meets\\Desktop\\BE Developer\\Projects\\demo.json'

def read_file():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        return []


def write_file(new_data):
    data = read_file()
    data.append(new_data)
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    return True

def status(num):
    if num == 1:
        return "To-do"
    elif num == 2:
        return "In-progress"
    elif num == 3:
        return "Done"

def task(id,desc,status):
    return {'task_id': id, 'task_desc': desc, 'status': status, 'create_date': f'{datetime.datetime.now()}', 'update_date': f'{datetime.datetime.now()}'}

def update_task(taskid, taskdesc):
    data = read_file()
    for items in data:
        if items["task_id"] == taskid:
            items["task_desc"] = taskdesc
            items["update_date"] = f'{datetime.datetime.now()}'

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    return True

def del_task(taskid):
    data = read_file()
    for index, items in enumerate(data):
        if items["task_id"] == taskid:
            del data[index]

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    return True

def status_update_task(taskid,taskstatus):
    data = read_file()
    for items in data:
        if items["task_id"] == taskid:
            items["status"] = taskstatus
            items["update_date"] = f'{datetime.datetime.now()}'

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    return True

def view_filtered_data(statusid):
    data = read_file()
    filtered_data = []
    for items in data:
        if items["status"] == status(statusid):
            filtered_data.append(items)
    return filtered_data

#===============================================================================================
#Program Start
if __name__ == "__main__":



    choice = True
    while choice:
        clear_console()
        print("Welcome to the Task Tracker:")
        print("Choose the below options (1-6):")
        print("1. Add New Task")
        print("2. Update existing task")
        print("3. Delete existing task")
        print("4. Update Task status")
        print("5. View all tasks")
        print("6. View tasks by status")
        print("7. Exit")

        input_choice = input("\nSelect option:\n")

        if input_choice == '1':
            print("\nEnter the Task Details below:")
            task_desc = input("Task Desc: ")
            task_status = status(1)
            task_id_list = []
            data = read_file()
            if len(data) == 0:
                task_id = 1
            else:
                [task_id_list.append(items["task_id"]) for items in data ]
                task_id_list.sort()
                task_id = task_id_list[-1] + 1

            new_task = task(task_id,task_desc,task_status)

            flag = write_file(new_task)
            if flag:
                print("Task added Successfully\n")
            else:
                print("Something went wrong!\n")

        elif input_choice == '2':
            data = read_file()
            update_choice = True
            task_id_list = []
            while update_choice:

                print("\nPlease find the list of tasks below:")
                print("Choose the task id which you need to edit:\n")
                for items in data:
                    task_id = items["task_id"]
                    task_desc = items["task_desc"]
                    task_status = items["status"]
                    task_id_list.append(task_id)

                    print(f"Task ID: {task_id}")
                    print(f"Task Desc: {task_desc}")
                    print(f"Task status: {task_status}")
                    print("\n")

                update_choice = input("\nSelect task id:\n")
                if not (update_choice.isdigit()):
                    clear_console()
                    print("Invalid Task ID")
                    update_choice = True
                    continue
                elif int(update_choice) in task_id_list:
                    selected_task = [items for items in data if items["task_id"] == int(update_choice)]
                    print(f"Task ID: {selected_task[0]["task_id"]}")
                    print(f"Task Desc: {selected_task[0]["task_desc"]}")
                    print(f"Task status: {selected_task[0]["status"]}")
                    print("\n")
                    task_desc = input("Please enter the updated task description:")

                    flag = update_task(selected_task[0]["task_id"],task_desc)
                    update_choice = False

                    if flag:
                        print("Task updated Successfully\n")
                    else:
                        print("Something went wrong!\n")

                else:
                    clear_console()
                    print("Invalid Task ID")
                    update_choice = True
                    continue

        elif input_choice == '3':
            data = read_file()
            delete_choice = True
            task_id_list = []
            while delete_choice:
                print("\nPlease find the list of tasks below:")
                print("Choose the task id which you need to delete:\n")
                for items in data:
                    task_id = items["task_id"]
                    task_desc = items["task_desc"]
                    task_status = items["status"]
                    task_id_list.append(task_id)

                    print(f"Task ID: {task_id}")
                    print(f"Task Desc: {task_desc}")
                    print(f"Task status: {task_status}")
                    print("\n")

                delete_choice = input("\nSelect task id:\n")
                if not (delete_choice.isdigit()):
                    clear_console()
                    print("Invalid Task ID")
                    delete_choice = True
                    continue
                elif int(delete_choice) in task_id_list:
                    selected_task = [items for items in data if items["task_id"] == int(delete_choice)]
                    print(f"Task ID: {selected_task[0]["task_id"]}")
                    print(f"Task Desc: {selected_task[0]["task_desc"]}")
                    print(f"Task status: {selected_task[0]["status"]}")
                    print("\n")

                    flag = del_task(selected_task[0]["task_id"])
                    delete_choice = False

                    if flag:
                        print("Task deleted Successfully\n")
                    else:
                        print("Something went wrong!\n")

                else:
                    clear_console()
                    print("Invalid Task ID")
                    delete_choice = True
                    continue

        elif input_choice == '4':
            data = read_file()
            status_choice = True
            task_id_list = []
            while status_choice:

                print("\nPlease find the list of tasks below:")
                print("Choose the task id for which you need to update the status:\n")
                for items in data:
                    task_id = items["task_id"]
                    task_desc = items["task_desc"]
                    task_status = items["status"]
                    task_id_list.append(task_id)

                    print(f"Task ID: {task_id}")
                    print(f"Task Desc: {task_desc}")
                    print(f"Task status: {task_status}")
                    print("\n")

                status_choice = input("\nSelect task id:\n")
                if not (status_choice.isdigit()):
                    clear_console()
                    print("Invalid Task ID")
                    status_choice = True
                    continue
                elif int(status_choice) in task_id_list:
                    selected_task = [items for items in data if items["task_id"] == int(status_choice)]
                    print(f"Task ID: {selected_task[0]["task_id"]}")
                    print(f"Task Desc: {selected_task[0]["task_desc"]}")
                    print(f"Task status: {selected_task[0]["status"]}")
                    print("\n")

                    new_status_choice = True
                    while new_status_choice:
                        new_status_choice = input("Please choose the updated task status:\n 1 - To-do\n 2 - In-progress\n 3 - Done\n")
                        if not (new_status_choice.isdigit()):
                            clear_console()
                            print("Invalid Status ID")
                            new_status_choice = True
                            continue
                        elif int(new_status_choice) in [1,2,3]:
                            flag = status_update_task(selected_task[0]["task_id"],status(int(new_status_choice)))
                            new_status_choice = False
                            status_choice = False
                            if flag:
                                print("Task status updated Successfully\n")
                            else:
                                print("Something went wrong!\n")
                        else:
                            clear_console()
                            print("Invalid Status ID")
                            new_status_choice = True
                            continue

                else:
                    clear_console()
                    print("Invalid Task ID")
                    status_choice = True
                    continue

        elif input_choice == '5':
            data = read_file()
            for items in data:
                task_id = items["task_id"]
                task_desc = items["task_desc"]
                task_status = items["status"]

                print(f"Task ID: {task_id}")
                print(f"Task Desc: {task_desc}")
                print(f"Task status: {task_status}")
                print("\n\n")

        elif input_choice == '6':

            new_choice = True
            while new_choice:
                status_choice = input("Please choose the task status to view tasks:\n 1 - To-do\n 2 - In-progress\n 3 - Done\n")
                if not (status_choice.isdigit()):
                    clear_console()
                    print("Invalid Status ID")
                    new_choice = True
                    continue
                elif int(status_choice) in [1, 2, 3]:

                    data_list = view_filtered_data(int(status_choice))
                    if not(data_list):
                        print("No task Found\n")
                    else:
                        for items in data_list:
                            task_id = items["task_id"]
                            task_desc = items["task_desc"]
                            task_status = items["status"]

                            print(f"Task ID: {task_id}")
                            print(f"Task Desc: {task_desc}")
                            print(f"Task status: {task_status}")
                            print("\n\n")

                    new_choice = False

                else:
                    clear_console()
                    print("Invalid Status ID")
                    new_choice = True
                    continue

        elif input_choice == '7':
            print("Thanks for using the task tracker")
            break

        else:
            print("Invalid Input")
            input_choice = True

        if input_choice == '7':
            break
        else:
            continue

else:
    print("Program cannot be executed")



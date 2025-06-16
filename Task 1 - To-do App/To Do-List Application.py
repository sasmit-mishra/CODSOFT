# To Do-List Application

def task_management():
    tasks = []
    tasks_num = int(input("Enter number of tasks: "))

    for i in range(1, tasks_num + 1):
        tasks_name = input(f"Enter task {i}: ")  
        tasks.append(tasks_name)
    print("")

    print("Today's tasks are:", tasks)  
    print("")

    while(True):
        input_from_user = int(input(
        "Enter 1 : For adding more tasks ""\n"
        "Enter 2 : To remove the task""\n"
        "Enter 3 : To upgrade any task " "\n"
        "Enter 4 : To view all the tasks""\n"
        "Enter 5 : To exit / close the app ""\n""\n"
        ))

        if (input_from_user == 1):
            print("")
            new_tasks = input("Enter the new task you want to add : ")
            tasks.append(new_tasks)
            print("")
            print("Now todays tasks are : ",tasks)
            print("")

        elif (input_from_user == 2):
            print("")
            new_tasks = input("Enter the new task you want to remove : ")
            print("")
            if (new_tasks in tasks):
                tasks.remove(new_tasks)
                print("")
            else:
                print("Task not found ")
                print("")
            print("Now todays tasks are : ",tasks)
            print("")

        elif (input_from_user == 3):
            print("")
            unupgraded_task = input("Enter the task you want to upgrade :")
            upgraded_task = input("Enter the task you want to place instead of the last one : ")
            print("")
            if(unupgraded_task in tasks):
                print("")
                index = tasks.index(unupgraded_task)
                tasks[index] = upgraded_task
            else:
                print("")
                print("Task not found ")
                print("")
            
            print("Now todays tasks are : ",tasks)
            print("")

        elif (input_from_user == 4) :
            print("")
            print("Todays tasks are : ",tasks)
            print("")

        elif (input_from_user == 5):
            print("The APP closes sucessfully ")
            break

        else:
            print("Invalid input! Enter the value between 1 to 5 ")
            print("")

task_management()

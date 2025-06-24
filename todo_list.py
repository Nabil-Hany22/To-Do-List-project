# Start the program
# Ask the user: add, view, remove, or exit
# If command == "add", prompt the user to enter a task name, then print "Task was added"
# If command == "view", then:
#     - If there are tasks, display them
#     - Else, print "There are no tasks"
# If command == "remove", then:
#     - If there are tasks, prompt the user to enter the task name and remove it
#     - Else (if the task name is not found), print "Task not found"
# If command == "exit", then break the program (exit the while loop)
# Else, print "Invalid command"

todo_list = []

while(True):
    user_command = input("Enter A Command (add , view , remove , exit ): ")
    if(user_command == "add"):
        task = input("Enter your task: ")
        todo_list.append(task)
        print("The Task was added successfully")
    elif(user_command == "view"):
        if not todo_list:
            print("There are no tasks to display")
        else :
            for task in todo_list:
                print(task)
    elif(user_command == "remove"):
        if not todo_list:
            print("There are no tasks to remove: ")
        elif todo_list:
            task = input("Enter the task name to remove")
            if task in todo_list:
                todo_list.remove(task)
                print("The Task was removed successfully")
            else:
                print("Task not found")
    elif(user_command == "exit"):
        break
    else:
        print("invalid command")
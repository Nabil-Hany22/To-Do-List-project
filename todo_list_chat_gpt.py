# To-Do List App using Functions in Python Terminal

# Initialize an empty list to store tasks
todo_list = []

# Function to add a new task to the list
def add_task():
    task = input("Enter your task: ").strip()
    todo_list.append(task)
    print("✅ The task was added successfully.\n")

# Function to display all tasks
def view_tasks():
    if not todo_list:
        print("📭 There are no tasks to display.\n")
    else:
        print("📝 Your tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
        print()  # Empty line for formatting

# Function to remove tasks (either one or all)
def remove_task():
    if not todo_list:
        print("📭 There are no tasks to remove.\n")
        return  # نخرج من الدالة مباشرة لو فاضية

    # نسأل المستخدم هل عايز يحذف كل المهام ولا واحدة بس
    choice = input("Do you want to remove (one) task or (all) tasks? ").strip().lower()

    if choice == "all":
        todo_list.clear()
        print("🧹 All tasks have been removed successfully.\n")

    elif choice == "one":
        task = input("Enter the task name to remove: ").strip()
        if task in todo_list:
            todo_list.remove(task)
            print("🗑️ The task was removed successfully.\n")
        else:
            print("❌ Task not found.\n")


# Function to show the main menu and handle user commands
def main():
    while True:
        # Ask user for a command
        command = input("Enter a command (add, view, remove, exit): ").strip().lower()

        # Match the command to the correct function
        if command == "add":
            add_task()
        elif command == "view":
            view_tasks()
        elif command == "remove":
            remove_task()
        elif command == "exit":
            print("👋 Goodbye! Have a productive day!")
            break
        else:
            print("⚠️ Invalid command. Please try again.\n")

# Start the program
main()

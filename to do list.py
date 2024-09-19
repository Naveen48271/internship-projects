# To-Do List Application

def display_menu():
    """Displays the main menu for the To-Do list application."""
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Exit")

def view_tasks(tasks):
    """Displays all tasks in the To-Do list."""
    if not tasks:
        print("\nYour To-Do list is empty.")
    else:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Adds a new task to the To-Do list."""
    new_task = input("\nEnter the task you want to add: ")
    tasks.append(new_task)
    print(f"Task '{new_task}' has been added to your To-Do list.")

def update_task(tasks):
    """Updates an existing task in the To-Do list."""
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number you want to update: "))
        if 1 <= task_num <= len(tasks):
            updated_task = input("Enter the updated task: ")
            tasks[task_num - 1] = updated_task
            print(f"Task {task_num} has been updated to '{updated_task}'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Deletes a task from the To-Do list."""
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number you want to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' has been removed from your To-Do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def to_do_list_app():
    """Main function to run the To-Do list application."""
    tasks = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye! Thanks for using the To-Do List App.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Start the To-Do list application
to_do_list_app()

import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from tasks.json file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        tasks = json.load(file)
    return tasks

def save_tasks(tasks):
    """Save tasks to tasks.json file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    """Add a new task to the tasks list."""
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (low, medium, high): ")
    
    tasks = load_tasks()
    task_id = len(tasks) + 1
    new_task = {
        "id": task_id,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{description}' added successfully!")

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("Current tasks:")
    for task in tasks:
        print(f"- ID: {task['id']}, Description: {task['description']}, Due Date: {task['due_date']}, Priority: {task['priority']}, Completed: {task['completed']}")

def update_task():
    """Update task details."""
    task_id = int(input("Enter task ID to update: "))
    tasks = load_tasks()
    task_updated = False
    for task in tasks:
        if task['id'] == task_id:
            description = input(f"Enter new description ({task['description']}): ").strip() or task['description']
            due_date = input(f"Enter new due date ({task['due_date']}): ").strip() or task['due_date']
            priority = input(f"Enter new priority ({task['priority']}): ").strip() or task['priority']
            task['description'] = description
            task['due_date'] = due_date
            task['priority'] = priority
            task_updated = True
            break
    if task_updated:
        save_tasks(tasks)
        print(f"Task {task_id} updated successfully!")
    else:
        print(f"Task with ID {task_id} not found.")

def complete_task():
    """Mark a task as completed."""
    task_id = int(input("Enter task ID to mark as completed: "))
    update_task_status(task_id, True)

def delete_task():
    """Delete a task."""
    task_id = int(input("Enter task ID to delete: "))
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully!")

def update_task_status(task_id, completed):
    """Update task status (completed or not)."""
    tasks = load_tasks()
    task_updated = False
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = completed
            task_updated = True
            break
    if task_updated:
        save_tasks(tasks)
        print(f"Task {task_id} marked as {'completed' if completed else 'incomplete'} successfully!")
    else:
        print(f"Task with ID {task_id} not found.")

def main():
    while True:
        print("\n===== Todo List Manager =====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            complete_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()

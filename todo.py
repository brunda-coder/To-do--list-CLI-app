import os

TASK_FILE = "tasks.txt"

# Load tasks from file (create file if missing)
def load_tasks():
    if not os.path.exists(TASK_FILE):
        open(TASK_FILE, "w").close()
        return []
    with open(TASK_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found. Add a new one!\n")
        return
    print("\n==== Your Tasks ====")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

# Add new task
def add_task(tasks):
    new_task = input("Enter task: ").strip()
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        print("✅ Task added successfully!\n")
    else:
        print("⚠️ Empty task not added.\n")

# Mark task as completed
def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            completed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🎉 '{completed}' marked as completed!\n")
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

# Delete a specific task
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            deleted = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️ '{deleted}' deleted successfully!\n")
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

# Main menu loop
def main():
    tasks = load_tasks()
    while True:
        print("==== To-Do List App ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye! Keep hustling!\n")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
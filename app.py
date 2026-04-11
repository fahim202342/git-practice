# Simple To-Do List App

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"✓ Added: {task}")

def view_tasks():
    if not tasks:
        print("No tasks!")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def remove_task(index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"✓ Removed: {removed}")
    else:
        print("Invalid task number!")

def main():
    while True:
        print("\n" + "="*30)
        print("TO-DO LIST")
        print("="*30)
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("\nChoice (1-4): ")
        
        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            try:
                idx = int(input("Task number to remove: "))
                remove_task(idx)
            except ValueError:
                print("Invalid input!")
        elif choice == '4':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

# To-Do List
# Add, complete, delete, and review your daily tasks

tasks = []


def add_task():
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty!")
        return

    priorities = {"1": "High", "2": "Medium", "3": "Low"}

    print("\nPriority Levels:")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    choice = input("Choose priority: ").strip()
    if choice not in priorities:
        print("Invalid priority!")
        return

    tasks.append({"title": title, "priority": priorities[choice], "done": False})
    print(f"\nAdded task: {title}")


def view_tasks():
    if not tasks:
        print("\nNo tasks added yet!")
        return

    print(f"\n{'No.':<5} {'Status':<10} {'Priority':<10} Task")
    print("-" * 55)
    for index, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "Pending"
        print(f"{index:<5} {status:<10} {task['priority']:<10} {task['title']}")


def mark_completed():
    view_tasks()
    if not tasks:
        return

    try:
        index = int(input("\nEnter task number to mark completed: "))
        if not 1 <= index <= len(tasks):
            print("Invalid task number!")
            return
    except ValueError:
        print("Please enter a valid number!")
        return

    task = tasks[index - 1]
    if task["done"]:
        print("Task is already completed!")
        return

    task["done"] = True
    print(f"Completed task: {task['title']}")


def delete_task():
    view_tasks()
    if not tasks:
        return

    try:
        index = int(input("\nEnter task number to delete: "))
        if not 1 <= index <= len(tasks):
            print("Invalid task number!")
            return
    except ValueError:
        print("Please enter a valid number!")
        return

    removed = tasks.pop(index - 1)
    print(f"Deleted task: {removed['title']}")


def task_summary():
    if not tasks:
        print("\nNo tasks added yet!")
        return

    total = len(tasks)
    completed = sum(task["done"] for task in tasks)
    pending = total - completed

    priority_counts = {"High": 0, "Medium": 0, "Low": 0}
    for task in tasks:
        if not task["done"]:
            priority_counts[task["priority"]] += 1

    print("\nTask Summary")
    print("-" * 30)
    print(f"Total tasks:      {total}")
    print(f"Completed tasks:  {completed}")
    print(f"Pending tasks:    {pending}")
    print("\nPending by priority:")
    print(f"High:   {priority_counts['High']}")
    print(f"Medium: {priority_counts['Medium']}")
    print(f"Low:    {priority_counts['Low']}")


def main():
    print("=" * 40)
    print("          TO-DO LIST")
    print("=" * 40)

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Completed")
        print("4. Delete Task")
        print("5. Task Summary")
        print("6. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            task_summary()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
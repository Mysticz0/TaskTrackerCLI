import argparse

def add_task(task):
    print("Task added successfully")

def update_task(task):
    print("Task updated successfully")

def delete_task(task):
    print("Task deleted successfully")

def mark_task_in_progress(task):
    print("Task marked as in progress")

def mark_task_done(task):
    print("Task marked as done")

def list_tasks():
    print("Listing all tasks")

def list_tasks_by_status(status):
    print(f"Listing all tasks by {status}")

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    parser.add_argument("command", choices=["add", "update", "delete", "mark-in-progress", "mark-done", "list", "list-by-status"])
    parser.add_argument("task", nargs="?", help="Task description")
    parser.add_argument("--status", help="Task status")
    args = parser.parse_args()

    if args.command == "add":
        if not args.task:
            print("Error: Task description is required")
            return
        add_task(args.task)

    elif args.command == "update":
        if not args.task:
            print("Error: Task description is required")
            return
        update_task(args.task)

    elif args.command == "delete":
        if not args.task:
            print("Error: Task description is required")
            return
        delete_task(args.task)

    elif args.command == "mark-in-progress":
        if not args.task:
            print("Error: Task description is required")
            return
        mark_task_in_progress(args.task)

    elif args.command == "mark-done":
        if not args.task:
            print("Error: Task description is required")
            return
        mark_task_done(args.task)

    elif args.command == "list":
        list_tasks()

    elif args.command == "list-by-status":
        if not args.status:
            print("Error: Status is required")
            return
        list_tasks_by_status(args.status)

    else:
        print("Error: Invalid command")
        return
    
if __name__ == "__main__":
    main()
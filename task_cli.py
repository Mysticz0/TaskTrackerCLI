import argparse
import json
import datetime as dt
from pathlib import Path

START_ID = 1

def init():
    file_path = Path("tasks.json")
    if not file_path.is_file():
        f = open("tasks.json", "w")
        json.dump({"tasks" : []}, f, indent=2)
        f.close()
        
def add_task(task):

    description = task
    status = "todo"
    timestamp = str(dt.datetime.now(dt.timezone.utc))

    with open("tasks.json", "r") as f:
        data = json.load(f)

    temp = data["tasks"]
    if temp == []:
        id = START_ID
    else:
        id = temp[-1]["id"] + 1
    
    new_task = {"id" : id, "description" : description, "status" : status, "created_at" : timestamp, "updated_at" : timestamp}
    temp.append(new_task)

    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Task added successfully")

def update_task(id, task):
    
    new_description = task

    with open("tasks.json", "r") as f:
        data = json.load(f)
    
    temp = data["tasks"]
    if temp == []:
        print(f"No task with ID = {id}")
        return
    
    for t in temp:
        if t["id"] == id:
            t["description"] = new_description
            with open("tasks.json", "w") as f:
                json.dump(data, f, indent=2)
            print("Task updated successfully")
            return
    
    print(f"No task with ID = {id}")


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
    init()

    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)
    add_p = subparsers.add_parser("add")
    add_p.add_argument("task")

    update_p = subparsers.add_parser("update")
    update_p.add_argument("id", type=int)
    update_p.add_argument("task")

    delete_p = subparsers.add_parser("delete")
    delete_p.add_argument("id", type=int)

    subparsers.add_parser("mark-in-progress").add_argument("id", type=int)
    subparsers.add_parser("mark-done").add_argument("id", type=int)

    list_p = subparsers.add_parser("list")
    list_p.add_argument("status", choices=["todo", "in-progress", "complete"], nargs='?')
    
    args = parser.parse_args()

    if args.command == "add":
        add_task(args.task)

    elif args.command == "update":
        update_task(args.id, args.task)

    elif args.command == "delete":
        delete_task(args.task)

    elif args.command == "mark-in-progress":
        mark_task_in_progress(args.task)

    elif args.command == "mark-done":
        mark_task_done(args.task)

    elif args.command == "list":
        if args.status is None:
            list_tasks()
        else:
            list_tasks_by_status(args.status)

    else:
        print("Error: Invalid command")
        return
    
if __name__ == "__main__":
    main()
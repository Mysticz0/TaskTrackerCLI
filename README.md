# Task Tracker CLI

A simple command-line task tracker written in Python. Tasks are stored locally in a `tasks.json` file in the current working directory.

## Requirements

- Python 3.7+
- No third-party dependencies (uses only the standard library)

## Installation

Clone the repository and run the script directly with Python:

```bash
git clone <repo-url>
cd task-tracker-cli
python task_cli.py --help
```

## Usage

The CLI is invoked as `python task_cli.py <command> [arguments]`. On first run, a `tasks.json` file is automatically created in the current directory.

### Add a task

```bash
python task_cli.py add "Buy groceries"
```

### Update a task

```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
```

### Delete a task

```bash
python task_cli.py delete 1
```

### Mark a task as in-progress or done

```bash
python task_cli.py mark-in-progress 1
python task_cli.py mark-done 1
```

### List tasks

List all tasks:

```bash
python task_cli.py list
```

List tasks filtered by status (`todo`, `in-progress`, or `done`):

```bash
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done
```

## Task Properties

Each task is stored with the following fields:

- `id` — Unique integer identifier
- `description` — Short description of the task
- `status` — One of `todo`, `in-progress`, or `done`
- `createdAt` — UTC timestamp of creation
- `updatedAt` — UTC timestamp of last update

## Storage

All tasks are persisted in a `tasks.json` file in the directory where the command is run. The file is created automatically on first use.

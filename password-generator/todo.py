import click # to Create a cli
import json # to save and load tasks from a file
import os # to check if the file exists

TODO_FILE = "todo.json"

def load_tasks():
        if os.path.exists(TODO_FILE):
            with open(TODO_FILE, "r") as file:
             return json.load(file)
        return []
        

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file,indent=4)

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task":task,"done": False})
    save_tasks(tasks)
    click.echo(f"Task added successfully: {task}")

@click.command()
def list_tasks():
    """List all the tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks found")
        return 
    for index, task in enumerate(tasks,1):
        status = "✅" if task["done"] else "❌"
        click.echo(f"{index}. {task['task']} [{status}]")

cli.add_command(add)
cli.add_command(list_tasks)  #✅ fixed now 'list_tasks' is registred with CLI

if __name__== '__main__':
     cli()

    
def load_tasks(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename):
    with open(filename, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def display_menu():
    print("\nTo-Do List Manager")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        print(f'Added: {task}')
    else:
        print('Empty task not added.')
    return tasks

def remove_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f'Removed: {removed}')
        else:
            print('Invalid number.')
    except ValueError:
        print('Invalid input.')
    return tasks

def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)
    while True:
        display_menu()
        choice = input('Select (1-4): ')
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            tasks = add_task(tasks)
            save_tasks(tasks, filename)
        elif choice == '3':
            tasks = remove_task(tasks)
            save_tasks(tasks, filename)
        elif choice == '4':
            print('Exiting. Goodbye!')
            break
        else:
            print('Invalid option.')

if __name__ == "__main__":
    main()

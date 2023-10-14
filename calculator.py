# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Input from the user
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")import os

# Function to display the to-do list
def display_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

# Function to add a task to the to-do list
def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Added: {task}")

# Function to remove a task from the to-do list
def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Removed: {removed_task}")
    else:
        print("Invalid task index. Please try again.")

# Function to save the to-do list to a file
def save_todo_list(todo_list, filename="todo_list.txt"):
    with open(filename, "w") as file:
        for task in todo_list:
            file.write(f"{task}\n")
    print("To-do list saved to 'todo_list.txt'")

# Function to load the to-do list from a file
def load_todo_list(filename="todo_list.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            todo_list = [line.strip() for line in file]
        print("To-do list loaded from 'todo_list.txt'")
        return todo_list
    else:
        return []

# Main function
def main():
    todo_list = load_todo_list()

    while True:
        print("\nTo-Do List:")
        display_todo_list(todo_list)

        print("\nMenu:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Save to file")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == "2":
            task_index = int(input("Enter the task index to remove: "))
            remove_task(todo_list, task_index)
        elif choice == "3":
            save_todo_list(todo_list)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()

        continue

    operation = input("Choose an operation (+, -, *, /): ")

    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation. Please choose a valid operation.")
        continue

    # Perform the calculation based on the user's choice
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)

    # Display the result
    print("Result: ", result)

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        break
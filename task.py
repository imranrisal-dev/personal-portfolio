FILE_NAME = "employees.txt"


# Function 1: Add Employee
def add_employee(name, emp_id, salary):
    """Adds employee data to file"""
    with open(FILE_NAME, "a") as file:   # append mode---
        file.write(f"{name} | {emp_id} | {salary}\n")
    
    return "Employee Added Successfully"


# Function 2: View Employees
def view_employees():
    """Reads and returns all employee data"""
    try:
        with open(FILE_NAME, "r") as file:   # read mode---
            data = file.readlines()

        if not data:
            return "No employee records found."

        return data

    except FileNotFoundError:
        return "File not found. No records yet."



def display_data(data):
    """Reusable function to display employee records"""
    for line in data:
        print(line.strip())


# Menu Function
def menu():
    while True:
        print("\n===== Employee Salary Management System =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Exit")

        choice = input("Choose Option: ")

        if choice == "1":
            name = input("Enter Name: ")
            emp_id = input("Enter ID: ")
            salary = input("Enter Salary: ")

            result = add_employee(name, emp_id, salary)
            print(result)

        elif choice == "2":
            result = view_employees()

            if isinstance(result, list):
                print("\n--- Employee Records ---")
                display_data(result)
            else:
                print(result)

        elif choice == "3":
            print("Exiting Program...")
            break

        else:
            print("Invalid choice! Try again.")
menu()
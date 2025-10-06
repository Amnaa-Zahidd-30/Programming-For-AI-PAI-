try:

    name = input("Enter employee name: ")
    cnic = input("Enter employee CNIC number: ")
    age = input("Enter employee age: ")
    salary = input("Enter employee salary: ")

    with open('employee.txt', 'w') as fileObj:
        fileObj.write("Employee Biodata\n")
        fileObj.write("----------------\n")
        fileObj.write("Name: " + name + "\n")
        fileObj.write("CNIC: " + cnic + "\n")
        fileObj.write("Age: " + age + "\n")
        fileObj.write("Salary: " + salary + "\n")

    print("Employee biodata saved successfully in 'employee.txt'.")

    contact = input("Enter employee contact number to append: ")

    with open('employee.txt', 'a') as fileObj:
        fileObj.write("Contact: " + contact + "\n")

    print("Contact number appended successfully.")

    print("\nReading the file content")
    with open('employee.txt', 'r') as fileObj:
        content = fileObj.read()
        print(content)

except FileNotFoundError:
    print("Error: The file 'employee.txt' was not found.")
except PermissionError:
    print("Error: You don't have permission to access this file.")
except ValueError:
    print("Error: Invalid input. Please enter valid data types.")
except Exception as e:
    print("An unexpected error occurred:", e)


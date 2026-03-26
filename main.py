import os

file_name = "students.txt"

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    with open(file_name,"a") as file:
        file.write(name + "," + roll + "\n")

    print("Student added successfully")


def view_students():
    if not os.path.exists(file_name):
        print("No records found")
        return

    with open(file_name,"r") as file:
        data = file.readlines()

    for student in data:
        name,roll = student.strip().split(",")
        print("Name:",name," Roll:",roll)


def search_student():
    roll = input("Enter roll number: ")

    with open(file_name,"r") as file:
        data = file.readlines()

    found = False

    for student in data:
        name,r = student.strip().split(",")

        if r == roll:
            print("Student found:",name)
            found = True

    if not found:
        print("Student not found")


def delete_student():
    roll = input("Enter roll number: ")

    with open(file_name,"r") as file:
        data = file.readlines()

    with open(file_name,"w") as file:
        for student in data:
            name,r = student.strip().split(",")

            if r != roll:
                file.write(student)

    print("Student deleted if existed")


while True:

    print("\n1 Add Student")
    print("2 View Students")
    print("3 Search Student")
    print("4 Delete Student")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        break

    else:
        print("Invalid choice")

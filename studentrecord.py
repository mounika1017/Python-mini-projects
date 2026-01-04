students = []
def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }
    students.append(student)
    print("Student record added successfully.\n")
def display_students():
    if not students:
        print("No student records found.\n")
        return
    print("Student Records:")
    for s in students:
        print("Roll:", s["roll"], "Name:", s["name"], "Marks:", s["marks"])
    print()
def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s["roll"] == roll:
            print("Record Found:")
            print("Roll:", s["roll"], "Name:", s["name"], "Marks:", s["marks"])
            print()
            return
    print("Student record not found.\n")
def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student record deleted successfully.\n")
            return
    print("Student record not found.\n")
while True:
    print("---- Student Record Management ----")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.\n")

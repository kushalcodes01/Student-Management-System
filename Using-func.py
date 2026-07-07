students = []

def add_student():
    name = input("Enter the name of student :")
    roll = int(input("Enter the roll no. :"))

    students.append([name,roll])
    print("Stuydent added successfully")

def view_students():
    if len(students) ==0:
        print("no student found")
        return
    print("\n ------Student List--------")

    for student in students:
        print("Name:",student[0])
        print("Roll:",student[1])
        print("------------------")
    
    print()


def search_student():
    search_name=input("Enter the name to search:")

    found = False
    for student in students:
        if student[0].lower() == search_name.lower():
            print("\n Student Found")
            print("Name:",student[0])
            print("Roll:",student[1])
            found = True
            break
    if not found:
        print("Student not found.\n")


while True:
    print("---Student Management System-----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Students")
    print("4. Exit")

    choice = input("Enter your Choice:")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()
    
    elif choice == "3":
        search_student()
    
    elif choice == "4":
        print("Thank you using the system")
        break
    else:
        print("Invalid choice. Try Again.\n")
students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully!")

    elif choice == "2":
        print("\nStudent List:")
        
        if len(students)==0:
            print("No students found.")
        else:
            print(students)

    elif choice == "3":
        
        search_name = input("Enter Student name to search:")

        if search_name in students:
            print("Student Found")
        else:
            print("Student Not Found")
    elif choice == "4":
        print("Exiting program......")
        break

    else:
        print("Invalid choice!")
        
    
FILE_NAME = "student.txt"
while True:
    print("\n--- Student Performance System---")
    print("1. Add Student")
    print("2. View all Students")
    print("3. Search Student by ID")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        student_id = input("Enter Student ID: ")
        student_name = input("Enter Student Name: ")
        marks = int(input("Enter Marks: "))
        if marks>= 95:
            grade = "O"
        elif marks>= 90:
            grade  = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        else:
            grade = "D"
        with open(FILE_NAME, "a") as file :
            file.write(f"{student_id},{student_name},{marks},{grade}\n")
        print("Student saved successfully.")
        
        
        
        
    elif choice == "2":
        try:
            with open(FILE_NAME,"r") as file :
                lines = file.readlines()
            if len(lines) == 0:
                print("No student records found.")
            else:
                print("\n--ALL Students---")
                for line in lines:
                    student_id,student_name,marks,grade = line.strip().split(",")
                    print(f"ID: {student_id} | Name: {student_name} | Marks: {marks} | Grade: {grade}")
        except FileNotFoundError:
            print("No file fount yet . Add a student first.")
        except Exception: 
            print("Some other error occured")
    elif choice == "3":
        search_id = input("Enter Student ID to search: ")
        found = False

        try:
            with open(FILE_NAME, "r")as file:
                lines = file.readlines()
            for line in lines:
                student_id, student_name , marks  , grade = line.strip().split(",")
                if student_id == search_id:
                    print("\nStudent Found🎉🤩")
                    print(f"ID:{student_id} | Name: {student_name} | Marks: {marks} | Grade: {grade} ")
                    found = True
                    break
            if not found:
                print("Student not found.")
        except FileNotFoundError:
            print('No file found yet, Add a student first.') 
    elif choice == '4':
        print("Exiting")
        break
    


    



    
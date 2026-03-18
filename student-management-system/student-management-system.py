students = []
while True:
    try:
        # choice your option
        option = input("Choice: add, show, search, delete, break: ")


        # add student
        if option == "add":
            name = input("Enter your name: ")
            Id = int(input("Enter your ID: "))
            class1 = int(input("Enter your class: "))
            cgpa = float(input("Enter your CGPA: "))

            student = {
                "name" : name,
                "id" : Id,
                "class1" : class1,
                "cgpa" : cgpa
            }
            students.append(student)
        
        # show student
        elif option == "show":
            for student in students:
                print(f"Name: {student["name"]}, ID: {student["id"]}, Class: {student["class1"]}, CGPA: {student["cgpa"]}")

        # Search id
        elif option == "search":
            search_id = int(input("Enter your id: "))
            found = False
            for student in students:
                if student["id"] == search_id:
                    print(student)
                    found = True
                    break
            if not found:
                print("Not Found")

        # delete id
        elif option == "delete":
            delete_id = int(input("Enter your delete id: "))
            found = False
            for student in students:
                    if student["id"] == delete_id:
                        students.remove(student)
                        print("Student deleted")
                        found = True
                        break

            if not found:
                print("Not found") 

        # break 
        elif option == "break":
            break
            
    # if input invalid input
    except ValueError:
        print("Invalid input")
for student in students:
    print(student)

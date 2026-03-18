# Employee Management System
# 1 Add Employee
# 2 Show Employees
# 3 Search Employee
# 4 Delete Employee
# 5 Update Employee
# 5 Exit

from tabulate import tabulate
class Employee:
    def __init__(self, name, emp_id, department, position, salary, phone, email):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.position = position
        self.__salary = salary
        self.phone = phone
        self.email = email

    def get_salary(self):
        return self.__salary

    def show(self):
        print("-"* 40)
        print(f"Name: {self.name},\nID: {self.emp_id}\nDepartment: {self.department}\nPosition: {self.position}\nSalary: {self.get_salary()}\nPhone: {self.phone}\nEmail {self.email}")
        print("-" * 40) 

class Office_manager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        name = input("Enter employee name: ")
        emp_id = int(input("Enter employee id: "))

        for employee in self.employees:
            if employee.emp_id == emp_id:
                print("Employee ID already exists.")
                return

        department = input("Enter employee department: ")
        position = input("Enter employee position: ")
        while True:
            try:
                salary = float(input("Enter employee salary: "))
                if salary <=0:
                    print("Salary must be positive number, try again.")
                    continue
                break
            
            except ValueError:
                print("Please enter numeric value.")
        
        
        phone = input("Enter employee phone number: ")
        email = input("Enter employee email: ")
        if "@" not in email or "." not in email:
            print("Invalid email address")
            print("*" * 40)
            return


        print("=" * 40)
        emp = Employee(name, emp_id, department, position, salary, phone, email)
        self.employees.append(emp)
        print("Employee added successfully!")
        print("=" * 40)

    def show_all_emp(self):
        if not self.employees:
            print("No employee found")
            return
        
        table = []
        for emp in self.employees:
            table.append(
                [
                    emp.emp_id,
                    emp.name,
                    emp.department,
                    emp.position,
                    emp.get_salary(),
                    emp.phone,
                    emp.email
                ]
            )
        headers = ["ID", "Name", "Department", "Position", "Salary", "Phone", "Email"]
        print(tabulate(table, headers = headers, tablefmt= "grid"))
        
        print(f"\nTotal Employee {len(self.employees)}")

        # for i, emp in enumerate(self.employees, start=1):
        #     print("\nEmployee", i) 
        #     emp.show()
        

    def search_emp(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.show()
                return
        table = []
        for emp in self.employees:
            table.append(
                [
                    emp.emp_id,
                    emp.name,
                    emp.department,
                    emp.position,
                    emp.get_salary(),
                    emp.phone,
                    emp.email
                ]
            )
        headers = ["ID", "Name", "Department", "Position", "Salary", "Phone", "Email"]
        print(tabulate(table, headers = headers, tablefmt= "grid"))
        print("No employee found with this id")

    def del_emp(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                print("Employee has been deleted")
                return
        print("Employee not found")

    # update employee info
    def update_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print("Leave blank if you don't want to change value")

                name = input("Enter employee name: ")
                new_id = (input("Enter employee id: "))
                if new_id:
                    new_id = int(new_id)
                    for employee in self.employees:
                        if employee.emp_id == new_id:
                            print("Employee id already exists.")
                            return

                    emp.emp_id = new_id

                # for employee in self.employees:
                #     if employee.emp_id == emp_id:
                #         print("Employee ID already exists.")
                #         return

                department = input("Enter employee department: ")
                position = input("Enter employee position: ")
                while True:
                    try:
                        salary = float(input("Enter employee salary: "))
                        if salary <=0:
                            print("Salary must be positive number, try again.")
                            continue
                        break
                    
                    except ValueError:
                        print("Please enter numeric value.")
                
                phone = input("Enter employee phone number: ")
                email = input("Enter employee email: ")
                if "@" not in email or "." not in email:
                    print("Invalid email address")
                    print("*" * 40)
                    return
                
                if name:
                    emp.name = name
                if new_id:
                    emp.emp_id = new_id
                if department:
                    emp.department = department
                if position:
                    emp.position = position
                if salary:
                    emp._Employee__salary = salary
                if phone:
                    emp.phone = phone
                if email:
                    emp.email = email
                print("Employee update successfully!")
                return
        print("Employee not found")


# object call
manager = Office_manager()
while True:
    try:
        # choice your option
        option = input(
        "\n 1. Add Employee"
        "\n 2. Show All Employees"
        "\n 3. Search Employee by ID"
        "\n 4. Delete Employee by ID"
        "\n 5. Update Employee"
        "\n 6. Exit"
        "\nEnter your choice: "
        )

        if option == "1":
            manager.add_employee()

        elif option == "2":
            manager.show_all_emp()

        elif option == "3":
            emp_id = int(input("Enter employee id: "))
            manager.search_emp(emp_id)

        elif option == "4":
            emp_id = int(input("Enter employee id: "))
            manager.del_emp(emp_id)

        elif option == "5":
            update = int(input("Enter update ID: "))
            manager.update_employee(update)

        elif option.lower() in ["6","break","exit","q"]:
            print("Exit...")
            break
        else:
            print("Invalid Choice, please try again")

    except Exception as e:
        print("Invalid input, please try again", e)


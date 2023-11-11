class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee Details:")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")

# Creating instances of the Employee class for different employees
employee1 = Employee(name="John Doe", employee_id="E001", salary=50000)
employee2 = Employee(name="Jane Smith", employee_id="E002", salary=60000)
employee3 = Employee(name="Bob Johnson", employee_id="E003", salary=55000)

# Displaying employee details for each instance
employee1.display_details()
print("----------------------")
employee2.display_details()
print("----------------------")
employee3.display_details()

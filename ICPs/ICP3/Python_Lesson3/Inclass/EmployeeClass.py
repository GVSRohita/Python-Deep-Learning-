class Employee:
    data_member = 0
    total_salary = 0
    total_average_salary = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        self.email = name + '.' + family + '@company.com'

        Employee.data_member = Employee.data_member + 1
        Employee.total_salary = Employee.total_salary + self.salary

    def averageSalary(self):
        self.total_average_salary = Employee.total_salary / Employee.data_member
        print("The employee Average salary is : ", self.total_average_salary)

    def fullname(self):
        return '{} {}'.format(self.name, self.family)


# Inheriting the Employee class
class FullTimeEmployee(Employee):
    # Redefining the full name function
    def fullname(self):
        return '{} {} {}'.format(self.name, self.family, self.department)


if __name__ == '__main__':
    # emp_1 and emp_2 are  the instance created for Employee class
    emp_1 = Employee('Divya', 'bandari', 5, 'computer science')
    emp_2 = Employee('Harsha', 'Maddhula ', 10, 'computer science')
    # Fte_1 and Fte_2 are the instance created for FullTimeEmployee class
    Fte_1 = FullTimeEmployee('Roshana', 'Goparaju', 15, 'Developer')
    Fte_2 = FullTimeEmployee('Deeksha', 'bandari', 20, 'software Engineering')
    # fullname = Employee()
    print(emp_1)
    print(emp_1.name)
    print(emp_1.fullname())
    print("The count of the employees", Employee.data_member)
    # Inheriting the properties of employee class
    print(Fte_1.name)
    print(Employee.total_salary)
    emp_1.averageSalary()
    Fte_1.fullname()
    print("The full name of the Fte employee is :", Fte_1.fullname())
    print("The count of the employees is : ", Employee.data_member)

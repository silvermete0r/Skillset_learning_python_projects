# Агрегация - это когда один объект содержит ссылку на другой объект. 

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

class Employee:
    def __init__(self, name):
        self.name = name

department = Department("Отдел разработки")
employee1 = Employee("Алихан Мусаев")
employee2 = Employee("Жанара Касымова")

department.add_employee(employee1)
department.add_employee(employee2)

for employee in department.employees:
    print(employee.name)






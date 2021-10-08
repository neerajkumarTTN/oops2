class Employee:
    raise_percentage=10
    def __init__(self,salary):
        self.salary=salary

    def raise_salary(self):
        self.salary=(self.salary+(self.salary)*Employee.raise_percentage/100)
        return self.salary

    @classmethod
    def raise_percent(self,raise_by):
        Employee.raise_percentage+=raise_by
        return Employee.raise_percentage

emp1=Employee(100000)
print(Employee.raise_percent(5))
print(emp1.raise_salary())


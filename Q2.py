class Employee:
    raise_percentage=10
    def __init__(self):
        pass
        
    def raise_salary(self,salary):
        self.salary=salary
        self.salary=(self.salary+(self.salary)*self.raise_percentage/100)
        return self.salary
emp1=Employee()
print(emp1.raise_salary(10000))
    



class Employee:
    def __init__(self,first_name,last_name,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary
        #self.email_id=first_name+"."+last_name+"@tothenew.com"
    @property
    def email_id(self):
        return f"{self.first_name}{self.last_name}@tothenew.com"
emp1=Employee("neeraj","kumar",1200)
emp2=Employee("ajay","singh",2500)
print(emp1.email_id)
print(emp2.email_id)
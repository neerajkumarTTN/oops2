class Vehicle:
    def __init__(self,make,mileage,capacity):
         self.make=make
         self.mileage=mileage
         self.capacity=capacity
        
    def __repr__(self):
        return f"{self.make} has mileage of {self.mileage} and capacity :{self.capacity}"
    def get_fare(self):
        print("fare of parent class")

class Car(Vehicle):
    def __init__(self,make,mileage,capacity):
        Vehicle.__init__(self,make,mileage,capacity)
    def get_fare(self):
        print("fare of car class")

class Bus(Vehicle):
    def __init__(self,make,mileage,capacity):
        Vehicle.__init__(self,make,mileage,capacity)
    def get_fare(self):
        print(" fare of Bus class")
bus1=Bus("Volvo",20,15)
car1=Car("Jaguar",15,15)
print(car1)
print(bus1)
print(bus1.get_fare())
print(car1.get_fare())
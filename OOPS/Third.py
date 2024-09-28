class Car:
    def __init__(self,brand,model) :
        self.brand=brand
        self.model=model

    def fullname(self):
        return f"{self.brand}; {self.model};{self.battery_size}"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

my_new=ElectricCar("tesla","s","232ke")
# print(my_new.battery_size)
print(my_new.fullname())
        

# my=Car("swift","maruti")
# print(my.model)
# print(my.fullname())
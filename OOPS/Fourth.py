class Car:
    def __init__(self,brand,model) :
        self.__brand=brand
        self.model=model

    def get_brand(self):
        return self.__brand+'hello'

    def fullname(self):
        return f"{self.__brand}; {self.model}: {self.batter_size}"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

my_new=ElectricCar("tesla","s","232ke")
print(my_new.get_brand())
# print(my_new.fullname())
        

# my=Car("swift","maruti")
# print(my.model)
# print(my.fullname())
class Car:

    Total=0

    def __init__(self,brand,model) :
        self.__brand=brand
        self.model=model
        Car.Total +=1
    def get_brand(self):
        return self.__brand+'hello'

    def fullname(self):
        return f"{self.__brand}; {self.model}: {self.batter_size}"
    
    def Fuel_type(self):
        return "Disel and petrol"
    
    @staticmethod
    def dis ():
        return "car is use fulll for long trip"
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def Fuel_type(self):
        return "Electtric Charge"


my_new=ElectricCar("tesla","s","232ke")
print(my_new.Fuel_type())

disel=Car("maruti","Swift")
print(disel.Fuel_type())

print(Car.Total)

print(my_new.dis())
print(Car.dis())

# print(my_new.fullname())
        

# my=Car("swift","maruti")
# print(my.model)
# print(my.fullname())
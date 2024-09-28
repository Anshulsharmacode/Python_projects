class Car:

    Total=0

    def __init__(self,brand,model) :
        self.__brand=brand
        self.__model=model
        Car.Total +=1
    def get_brand(self):
        return self.__brand+'hello'

    def fullname(self):
        return f"{self.__brand}; {self.__model}: {self.batter_size}"
    
    def Fuel_type(self):
        return "Disel and petrol"
    
    @staticmethod
    def dis ():
        return "car is use fulll for long trip"
    
    @property
    def model(self):
        return self.__model
        


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def Fuel_type(self):
        return "Electtric Charge"


# my_new=ElectricCar("tesla","s","232ke")



# print(isinstance(my_new,Car))
# print(isinstance(my_new,ElectricCar))
# print(my_new.Fuel_type())

# disel=Car("maruti","Swift")

# disel.model="tata"
# print(disel.model)

# print(my_new.fullname())
        

# my=Car("swift","maruti")
# print(my.model)
# print(disel.Fuel_type())

# print(Car.Total)

# print(my_new.dis())
# print(Car.dis())
# print(my.fullname())

class Battery :
    def Battery_info(self):
        return "this is a battery"
    

class Engine:
    def engine_info(self):
        return "this is engine"
    
class Electric_Car_Two(Battery,Engine,Car):
    pass

my_tt=Electric_Car_Two("Tesle","models")

print(my_tt.engine_info())
print(my_tt.Battery_info())
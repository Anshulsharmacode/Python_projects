class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def fullname(self):
        return(f"{self.brand}: {self.model}")


bg=Car("toyota", "volvo")
print(bg.model)
print(bg.fullname())
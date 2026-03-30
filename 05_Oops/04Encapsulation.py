class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def full_name(self):
        return f"brand: {self.__brand}, model: {self.__model}"
    def get_brand(self):
        return self.__brand
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_car =Car("BMW","Gclass")
print(my_car.full_name())
print(my_car.get_brand())
my_tesla =ElectricCar("Tesla","model s","85kwh")
print(my_tesla.full_name()) 
print(my_tesla.get_brand())       
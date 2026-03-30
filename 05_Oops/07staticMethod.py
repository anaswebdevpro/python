


class Car:
    total_cars = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1

    def full_name(self):
        return f"brand: {self.__brand}, model: {self.__model}"
    
    def get_brand(self):
        return self.__brand
    
    
    def fuel_type(self):
        return "petrol"
    
    @staticmethod
    def general_desc():
        return "This is car general information (static method)"
    






class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):        
        return "electricity"





my_car =Car("BMW","Gclass")
print(my_car.full_name())
print(my_car.get_brand())
print(my_car.fuel_type())


my_tesla =ElectricCar("Tesla","model s","85kwh")
print(my_tesla.full_name()) 
print(my_tesla.get_brand())       
print(my_tesla.fuel_type())
# total cars is a class variable that is shared by all instances of the class
print(Car.total_cars)


# static method can be called on the class itself rather than on an instance of the class
print(Car.general_desc())
print(my_car.general_desc())
print(my_tesla.general_desc())

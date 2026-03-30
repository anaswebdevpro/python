class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"brand: {self.brand}, model: {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        # super allow to access all the inherited values 
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    # def full_name(self):
    #     return f"brand: {self.brand}, model: {self.model}, battery size: {self.battery_size}"

my_car =Car("BMW","Gclass")   
print(my_car.full_name()) 

my_tesla =ElectricCar("Tesla","model s","85kwh")
print(my_tesla.full_name())   
# full name method is inherited by the Car class 
print(my_tesla.brand)
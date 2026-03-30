class Car:
  def __init__(self,userbrand,usermodel):
    self.brand =userbrand
    self.model =usermodel

  def greet(self):
   return  f"this car name {self.brand},model name is {self.model}"
    








my_car =Car("toyota","corolla")
print(my_car.brand)
print(my_car.model)

car2 = Car("mercedese","gclass")
print(car2.brand)
print(car2.model)

print(car2.greet())
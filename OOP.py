class Car:
    def __init__(self,color,brand,number):
        self.color = color
        self.brand = brand
        self.number = number
    
    def color_of_car(self):
        print(self.color)

Car1 = Car('pink','Pinto',233)
# print(Car1.color_of_car())
print(Car1.color)
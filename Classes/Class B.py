class Vehicle:
    def __init__(self, color):
        self.color = color
        
    def honk(self):
        return "Honk Honk!"
    
class Car(Vehicle):
    def __init__(self, color, brand):
        super().__init__(color)
        self.brand = brand
        
my_car = Car('red', 'Toyota')
print(my_car.honk())

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        
        
    def honk(self):
        return "Beep beep!"
    
my_car = Car('red', 'Toyoto')
print(my_car.honk())
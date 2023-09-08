#multi_line inheritance example
class car:
    def __init__(self , name , model , fuel):
        self.name = name
        self.model = model
        self.fuel = fuel
        
class BMW(car):
    def __init__(self , name , model , fuel , feature , color):
        super().__init__(name , model , fuel)
        self.feature = feature
        self.color = color

class audi(BMW):
    def __init__(self , name , model , fuel , feature , color ,made_in):
        super().__init__(name , model , fuel , feature , color)
        self.made_in  = made_in
        
    def show_car_details(self):
        print(f"The name of the car is {self.name}. The model of the car is {self.model}. The fuel of the car is {self.fuel}. The feature of the car is {self.feature}. The color of the car is {self.color}. The car is made in {self.made_in}")

x2 = audi('THAR' , '2017' , 'Diesel' , 'Automatic' , 'Pink' , 'Turkey')
x2.show_car_details()
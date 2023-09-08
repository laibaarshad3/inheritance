#single inheritance
class vehicle:
    def __init__(self , cost , hp):
        self.cost = cost
        self.hp = hp
        
class car(vehicle):
    def __init__(self , mileage , hp , cost , tyres):
        super().__init__(cost , hp)
        self.tyres = tyres
        self.mileage = mileage
    def show_car_details(self):
        print("i am a car")
        print("the tyres of the car is :" , self.tyres)
        print("the mileage of the car is :" , self.mileage)
        print("i am a vehicle")
        print("cost of a vehicle is : " , self.cost)
        print("hp of a vehicle is : " , self.hp)
        
x3 = car(34 , 45 , 65 , 4)
x3.show_car_details()
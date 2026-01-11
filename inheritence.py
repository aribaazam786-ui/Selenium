class carOne:
    def brand (self):
        print("Toyota")
    def color (self):
        print("Red")

class carTwo(carOne):
    def move(self):
        print("Car is moving")

class carThree(carTwo):
    def engine(self):
        print("Engine")

obj = carThree()
obj.brand()
obj.color()
obj.move()
obj.engine()
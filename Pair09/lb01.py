class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*self.width+2*self.height
    def info(self):
        return print(f"{self.width} x {self.height}: площа = {self.area()}, периметр = {self.perimeter()}")

while(True):
    try:
        a, b = map(float, input().strip().split(", "))
        rect = Rectangle(a, b)
        rect.info()
    except: break
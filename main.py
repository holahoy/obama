class Line:
    def __init__(self, x1 = 10, x2 = 20, y1 = 10, y2 = 20):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def multiply(self, time = 1):
        self.x1 = self.x1 * time
        self.x2 = self.x2 * time
        self.y1 = self.y1 * time
        self.y2 = self.y2 * time
    
    def width(self):
        x = self.x2 - self.x1
        y = self.y2 - self.y1

        return (x * x + y * y) ** 0.5
    
    def center(self):
        xc = (self.x1 + self.x2) / 2
        yc = (self.y1 + self.y2) / 2

        return [xc, yc]

    def show(self):
        print(f"x1 = {self.x1}")
        print(f"x2 = {self.x2}")
        print(f"y1 = {self.y1}")
        print(f"y2 = {self.y2}")


x1 = float(input("x1: "))
x2 = float(input("x2: "))
y1 = float(input("y1: "))
y2 = float(input("y2: "))

line = Line(x1 = x1, x2 = x2, y1 = y1, y2 = y2)

print(f"Line width is: {line.width()}")
print(f"Line center is: {line.center()} \n")

multiply = int(input("Enter how many times you want to increase the line: "))
line.multiply(multiply)

line.show()
print(f"Line width is: {line.width()}")
print(f"Line center is: {line.center()} \n")

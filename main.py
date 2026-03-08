class Line:
    def __init__(self, x1 = 10, x2 = 20, y1 = 10, y2 = 20):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def width(self):
        x = self.x2 - self.x1
        y = self.y2 - self.y1

        return (x * x + y * y) ** 0.5
    
    def center(self):
        xc = (self.x1 + self.x2) / 2
        yc = (self.y1 + self.y2) / 2

        return [xc, yc]

line = Line(x1 = 3, x2 = 10, y1 = 5, y2 = 10)
print(f"Line width is: {line.width()}")
print(f"Line center is: {line.center()}")
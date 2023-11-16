class Myshape:
    def __init__(self,side = 0 , width = 0 , lenth = 0, radius =0):
        self.side = side
        self.width = width
        self.lenth = lenth
        self.radius = radius

    def calculation_square(self):
        area1 = self.side * self.side
        print(area1)

    def calculation_rectangle(self):
        area2 = self.width * self.lenth
        print(area2)
    
    def calculation_circle(self):
        area3 = self.radius * self.radius * 3.14
        print(area3)
    
s1 = Myshape(5)
s1.calculation_square()

r1 = Myshape(0,3,6)
r1.calculation_rectangle()

c1 = Myshape(0,0,0,3)
c1.calculation_circle()



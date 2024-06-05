from math import sqrt
from classtools import AttrDisplay

class Figure(AttrDisplay):

    def __init__(self, name, hight = 0, lenght = 0, radius = 0):
        self.name = name
        self.hight = hight
        self.lenght = lenght
        self.radius = radius

    def GetPerimeter(self):
        pass

    def GetArea(self):
        pass

    #def __str__(self):
        #return f'--Figure: {self.name} H={self.hight} L={self.lenght} R={self.radius} P={self.GetPerimeter()} A={self.GetArea()}'

class Circle(Figure):

    def __init__(self, name):
        super().__init__(name, hight = 0, lenght= 0, radius = 3)

    def GetPerimeter(self):
        return 2*3.14*self.radius

    def GetArea(self):
        return 3.14*(self.radius**2)
        

class Triangle(Figure):

    def __init__(self, name):
        super().__init__(name, hight = 2, lenght = 3, radius = 0)

    def GetPerimeter(self):
        return round(self.hight+self.lenght+sqrt(self.hight**2+self.lenght**2), 2)

    def GetArea(self):
        return 0.5*self.hight*self.lenght

    
if __name__ == '__main__':

    circle = Circle('Circle')
    triangle = Triangle('Triangle')
    print('--All Tree--')
    for obj in (circle,triangle):
        print(obj)
        print('Area-', obj.GetArea(), 'Perimeter-', obj.GetPerimeter())
       






    
    

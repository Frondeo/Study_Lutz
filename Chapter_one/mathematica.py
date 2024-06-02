class Mathematica:
    def __init__(self, name, perimeter, area):
        self.name = name
        self.perimeter = perimeter
        self.area = area

    def calculate_area(self):
        return self.perimeter ** 2

    def __str__(self):
        return (f'{self.__class__.__name__} {self.name}, is perimeter {self.perimeter} and area {self.calculate_area()}')


class Figure(Mathematica):
    def __init__(self, name):
        super().__init__(name, 30, 2)


if __name__ == '__main__':
    triangle = Figure('Triangle')
    print(triangle)

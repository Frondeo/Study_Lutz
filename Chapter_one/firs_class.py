class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


class SecondClass(FirstClass):
    def display(self):
        print('Current value is "%s"' %self.data)


class ThirdClass(SecondClass):
    def __init__(self, value): #for initiate new object
        self.data = value

    def __add__(self,other): #for summ (+) by new object
        return ThirdClass(self.data + other)

    def __str__(self): #for print() and etc.
        return '[ThirdClass: %s]' %self.data

    def mul(self, other):
        self.data *= other

class Auto:
    def __init__(self, name, model, powerfull):
        self.name = name
        self.model = model
        self.powerfull = powerfull

    def __str__(self):
        return (f'{self.__class__.__name__} is {self.name} have engine {self.powerfull} kW ')


class Sedan(Auto):
    def __init__(self, name):
        super().__init__(name, 'Sport',54 )

if __name__ == '__main__':
    vesta =Sedan('Vesta')

    print(vesta)
class Auto:
    def __init__(self, name, model, powerfull):
        self.name = name
        self.model = model
        self.powerful = powerfull

    def __str__(self):
        return (f'abracadabra')


class Vesta(Auto):
    def __init__(self, name):
        super().__init__(name, 'sedan',54 )

if __name__ == '__main__':
    vesta = Vesta('Vesta')

    print(vesta)
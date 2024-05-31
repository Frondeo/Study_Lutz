class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def says(self):
        print(f'{self.name} says: "Hello everybody!"')


if __name__ == '__main__':
    andrey = Human('Andrey', 45)
    irisha = Human('Irisha', 43)

    #print(type(andrey))
    andrey.says()
    print(irisha.name)
    print(irisha.age)

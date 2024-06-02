class Animal:
    def make_noise(self):
        print('shhh')


class Cat(Animal):
    def make_noise(self):
        print('Miow!')


class Dog(Animal):
    def make_noise(self):
        print('Guff!')


def noise(animal: Animal):
    animal.make_noise()


if __name__ == '__main__':
   noise(Cat())
   noise(Dog())
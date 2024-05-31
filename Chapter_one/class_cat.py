class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f'{self.name} says: Meow!')


if __name__ == '__main__':
    tom = Cat('Tom', 2)
    angel = Cat('Angel', 1)

    tom.meow()
    angel.meow()


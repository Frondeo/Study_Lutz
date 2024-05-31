class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def guf(self):
        print(f'{self.name} says: Guf!')


if __name__ == '__main__':
   bibi = Dog('BiBi', 3)
   magie = Dog('Magie', 2)

   bibi.guf()
   magie.guf()
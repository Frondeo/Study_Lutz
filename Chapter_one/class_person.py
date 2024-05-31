class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    # def set_age(self):
    # def get_age(self):
    def describe(self):
        print(f'I am {self._first_name} {self._last_name}. I am {self._age} years old.')


if __name__ == '__main__':
    ivan = Person('Ivan', 'Yakushkin', 18)
    ivan.describe()

class Emploee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def cal_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return (f'{self.__class__.__name__} {self.name}, pay salary is {self.salary} and bonus {self.bonus} %. ' \
                f'Total bonus is {self.cal_total_bonus()} rub.')


class Cleaner(Emploee):
    def __init__(self, name):
        super().__init__(name, 15000, 1)


class Manager(Emploee):
    def __init__(self, name):
        super().__init__(name, 45000, 10)


class CEO(Emploee):
    def __init__(self, name):
        super().__init__(name, 105000, 100)


if __name__ == '__main__':
    masha = Cleaner('Mariya Ivanovna')
    igor = Manager('Igor Stanislavovich')
    director = CEO('Sergey Ivanovich')
    print(masha)
    print(igor)
    print(director)

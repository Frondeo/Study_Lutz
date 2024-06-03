class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def cal_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return (f'{self.__class__.__name__} {self.name}, pay salary is {self.salary} and bonus {self.bonus} %. ' \
                f'Total bonus is {self.cal_total_bonus()} rub.')


def calc_bonuses(employees: list[Employee]):  # polimorph
    for employee in employees:
        print(f'Calc bonuses for {employee.name} it is {employee.cal_total_bonus()}')


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, 15000, 1)


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 45000, 10)


class CEO(Employee):
    def __init__(self, name):
        super().__init__(name, 105000, 100)

    def cal_total_bonus(self):
        return self.salary // 100 * self.bonus * 2


if __name__ == '__main__':
    masha = Cleaner('Mariya Ivanovna')
    igor = Manager('Igor Stanislavovich')
    director = CEO('Sergey Ivanovich')
    print(masha)
    print(igor)
    print(director)
    a_list = [masha, igor, director]
    calc_bonuses(a_list)

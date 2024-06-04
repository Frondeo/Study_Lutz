class Person:
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def LastName(self):
        return self.name.split('_')[-1]

    def GiveRaise(self, percent, bonus = 1.0):
        self.pay = int(self.pay * (percent))

    def __repr__(self):
        return '--Person: %s, %s, %s' % (self.name, self.job, self.pay)
    
class Manager(Person):
    def __init__(self, name, pay):
        super().__init__(name, 'manager', pay)
        
    def GiveRaise(self, percent, bonus = 1.3):
        super().GiveRaise(percent + bonus)

class Department:
    def __init__(self, *args):
        self.members = list(args)

    def AddMember(self, person):
        self.members.append(person)

    def GiveRaises(self, percent):
        for person in self.members:
            person.GiveRaise(percent)
    def ShowAll(self):
        print('--All Tree--')
        for person in self.members:
            print(person)


        
if __name__ == '__main__':

    bob = Person('Bob_Smith')
    sue = Person('Sue_Jones', job = 'developer', pay = 100_000)
    tom = Manager('Tom_Jones', 100_000)

    development = Department(bob, sue)
    development.AddMember(tom)
    development.GiveRaises(1.1)
    development.ShowAll()








    

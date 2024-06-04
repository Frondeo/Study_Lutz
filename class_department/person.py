from classtools import AttrDisplay

class Person(AttrDisplay):

    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def LastName(self):
        return self.name.split('_')[-1]

    def GiveRaise(self, percent, bonus = 1.0):
        self.pay = int(self.pay * (percent))

    #def __repr__(self):
        #return '--Person: %s, %s, %s' % (self.name, self.job, self.pay)
    
class Manager(Person):
   
    def __init__(self, name, pay):
        super().__init__(name, 'manager', pay)
        
    def GiveRaise(self, percent, bonus):
        super().GiveRaise(percent + bonus)
        #Person.GiveRaise(self, percent + bonus)
        #self.pay = int(self.pay * (percent + bonus))

    #def __getattr__(self, attr):
        #return getattr(self.person, attr)

    #def __repr__(self):
        #return str(self.person)
  
if __name__ == '__main__':

    bob = Person('Bob_Smith')
    sue = Person('Sue_Jones', job = 'developer', pay = 100_000)
    tom = Manager('Tom_Jones', 100_000)

    #print(bob.name, bob.job, bob.pay)
    #print(sue.name, sue.job, sue.pay)
    #print(tom.name, tom.job, tom.pay)
    print('--All tree--')
    for obj in (bob, sue, tom):
        obj.GiveRaise(1.1, 1.3)
        print(obj)

    

    
    

from person import Person, Manager
import shelve

bob = Person('Bob_Smith')
sue = Person('Sue_Jones', job = 'developer', pay = 100_000)
tom = Manager('Tom_Jones', 100_000)


db = shelve.open('person_db')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()

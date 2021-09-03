# Polymorphism is an important feature of class definition in Python that is utilized when you have commonly named
# methods across classes or subclasses. This permits functions to use entities of different types at different times.
# So, it provides flexibility and loose coupling so that code can be extended and easily maintained over time.

# print(len('Hello'))
# print(dir('Hello'))


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('{0} eats {1}'.format(self.name, food))


class Dog(Animal):
    def fetch(self, thing):
        print('{0} goes after {1}!'.format(self.name, thing))

    def show_affection(self):
        print('{0} wags tail'.format(self.name))


class Cat(Animal):
    def swatstring(self):
        print('{0} shreds the string!'.format(self.name))

    def show_affection(self):
        print('{0} purrs'.format(self.name))


for a in (Dog('Rover'), Cat('Fluffy'), Cat('Paka'), Dog('Scott')): a.show_affection()

# The “show_affection” behaviors is polymorphic in the sense that it acted differently depending on the animal

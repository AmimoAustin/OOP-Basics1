# 1st example
class Date(object):  # base/parent class
    def get_date(self):
        return '2021-08-31'


class Time(Date):  # sub class inheriting functions from date class
    def get_time(self):
        return '00:00:00'


date = Date()
print('Get date from the Date Class: ', date.get_date())
time = Time()
print('Get time from Time Class: ', time.get_time())
print('Get date from Time Class by inheriting Date class method: ', time.get_date())
print('\n')


# second example

class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('%s is eating %s.  ' % (self.name, food))


class Dog(Animal):

    def fetch(self, thing):
        print('%s goes after the %s!' % (self.name, thing))


class Cat(Animal):

    def swatstring(self):
        print('%s shreds the string!' % self.name)


d = Dog('Ranger')
c = Cat('Meow')

d.fetch('ball')
c.swatstring()
d.eat('dog food')
c.eat('cat food')

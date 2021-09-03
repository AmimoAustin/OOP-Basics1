" Major branches of OOP are Inheritance, Polymorphism, Abstraction, and Encapsulation"


#

class MyClass(object):
    var = 7


# Create first instance of MyClass


this_obj = MyClass()
print(this_obj.var)
# Another instance of MyClass
that_obj = MyClass()
print(10 + that_obj.var)


class Age(object):
    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age


zack = Age()
zack.setAge(45)
print(zack.getAge())

zack.setAge("Forty Five")
print(zack.getAge())


# Python calls __init__ during the instantiation to define an additional attribute that should occur when a class is
# instantiated that may be setting up some beginning values for that object or running a routine required on
# instantiation

class MyClass(object):
    def __init__(self, age, number):
        self.age = age
        self.number = number


x = MyClass(22, 1)
print(x.age, x.number)


# working with class and instance data
# class data is shared among all instances. Instance data works only for the instance.

class InstanceCounter(object):
    count = 0  # This is a class data and is accessible to all instances

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count


a = InstanceCounter(9)
b = InstanceCounter(31)
c = InstanceCounter(80)
d = InstanceCounter(7)
for obj in (a, b, c, d):
    print('val of obj: %s' % (obj.get_val()))  # The %s operator lets you add a value into a Python string
    print('count: %s:' % (obj.get_count()))

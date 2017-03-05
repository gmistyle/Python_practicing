#6.1
class Thing():
    pass
print(Thing)

thing = Thing()
print(thing)

#6.2
class Thing2():
    letters = 'abc'
print(Thing2.letters)

#6.3

class Thing3():
    def __init__(self, letters):
        self.letters = letters

ex = Thing3('jimmy')
Thing3.letters
ex.letters

#6.4
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

ex1 = Element('Hydrogen', 'H', 1)

#6.5
element_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
ex2=Element(**element_dict)

#6.6
class Element2(Element):
    def dump(self):
        print(self.name)
        print(self.symbol)
        print(self.number)

hydrogen = Element2(**element_dict)

#6.7
print(hydrogen)

class Element3(Element2):
    def __str__(self):
        return ('name=%s, symbol=%s, number=%s' %\
                (self.name, self.symbol, self.number)
#magic method " __str__ " must return a string
hydrogen2 = Element3(**element_dict)

print(hydrogen2)

#6.8
class Element4():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number

example = Element4(**element_dict)
example.name

#6.9
class bear():
    def eats(self):
        return 'berries'

class rabbit():
    def eats(self):
        return 'clovers'

class octothorpe():
    def eats(self):
        return 'campers'

b = bear()
r = rabbit()
o = octothorpe()

print(b.eats())
print(r.eats())
print(o.eats())

#6.10

class laser():
    def does(self):
        return 'disintegrate'

class claw():
    def does(self):
        return 'crush'

class smartphone():
    def does(self):
        return 'ring'

class robot():
    def __init__(self):
        self.laser = laser()
        self.claw = claw()
        self.smartphone = smartphone()

    def does(self):
        return '''My laser, to %s.\nMy claw, to %s.\nMy smartphone, to %s.''' \
%(self.laser.does(), self.claw.does(), self.smartphone.does())

print(robot().does())
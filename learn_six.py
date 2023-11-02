class Animal:

    def voice(self):
        pass


class Cat(Animal):

    def voice(self):
        return 'Мяу'


class Dog(Animal):

    def voice(self):
        return 'Гав'


class Cow(Animal):

    def voice(self):
        return 'Му'


c = Cat()
d = Dog()
k = Cow()

print(c.voice())
print(d.voice())
print(k.voice())

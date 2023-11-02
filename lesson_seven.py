class Animal:

    counter = 0

    def __init__(self) -> None:
        Animal.counter += 1

    def voice(self):
        pass

    @staticmethod
    def get_animal_counter():
        return Animal.counter


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
print(Animal.get_animal_counter())

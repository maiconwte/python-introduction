class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} is making sound"

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.name} is amamentando"

class Ave(Animal):
    def voar(self):
        return f"{self.name} is voando"

class Dog(Mamifero):
    def make_sound(self):
        return "Woof"

dog = Dog("Rex")

print(dog.make_sound())


class Bat(Mamifero, Ave):
    def make_sound(self):
       return super().make_sound()

bat = Bat("Batman")

print(bat.make_sound())
print(bat.amamentar())
print(bat.voar())
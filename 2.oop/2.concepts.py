# Herança, Polimorfismo, Encapsulamento, Abstração,

class Animal:
    def __init__(self, name):
        self.name = name
    # Polimorfismo
    def make_sound(self):
        pass

class Dog(Animal):
    # Polimorfismo
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    # Polimorfismo
    def make_sound(self):
        return "Meow"

dog = Dog("Rex")
cat = Cat("Whiskers")

animals = [dog, cat]
for animal in animals:
    print(f"{animal.name} says {animal.make_sound()}")

class Conta:
    def __init__(self):
        # Encapsulamento
        self.__saldo = 0  # Atributo privado (encapsulado)

    def depositar(self, valor):  # Interface pública
        if valor > 0:  # Validação protegida
            self.__saldo += valor

    def ver_saldo(self):  # Acesso controlado
        return self.__saldo

conta = Conta()
conta.depositar(100)
print(conta.ver_saldo())

from abc import ABC, abstractmethod

class Veiculo(ABC):
    # Abstração
    @abstractmethod
    def mover(self):
        pass
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    # Polimorfismo
    def mover(self):
        return "Carro movendo..."

    def ligar(self):
        return "Carro ligando..."

    def desligar(self):
        return "Carro desligando..."

class Moto(Veiculo):
    def mover(self):
        return "Moto movendo..."

    def ligar(self):
        return "Moto ligando..."

    def desligar(self):
        return "Moto desligando..."

veiculos = [Carro(), Moto()]

for veiculo in veiculos:
    print(veiculo.mover())
    print(veiculo.ligar())
    print(veiculo.desligar())
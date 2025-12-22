class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau guau!")

# Uso
firulais = Perro("Firulais")
firulais.comer()   # Firulais está comiendo. (método heredado)
firulais.ladrar()  # Firulais dice: ¡Guau guau! (método propio)
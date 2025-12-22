# Clase base con un método común
class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido genérico...")

# Clases hijas que sobrescriben (override) el método
class Perro(Animal):
    def hacer_sonido(self):
        print("¡Guau guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("¡Miau miau!")

class Vaca(Animal):
    def hacer_sonido(self):
        print("¡Muuu!")

# Función que usa polimorfismo: acepta cualquier objeto que tenga hacer_sonido()
def escuchar_animal(animal):
    animal.hacer_sonido()  # El mismo método, pero el comportamiento depende del objeto real

# Uso del polimorfismo
animales = [
    Perro(),
    Gato(),
    Vaca(),
    Animal()  # También funciona con la clase base
]

for animal in animales:
    escuchar_animal(animal)
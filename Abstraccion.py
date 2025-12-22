from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

# Uso
c = Circulo(5)
r = Rectangulo(4, 6)

print(f"Área del círculo: {c.area():.2f}")      # Área del círculo: 78.54
print(f"Área del rectángulo: {r.area()}")        # Área del rectángulo: 24
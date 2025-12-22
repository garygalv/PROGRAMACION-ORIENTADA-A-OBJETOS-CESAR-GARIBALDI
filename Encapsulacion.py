class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Getter (para leer la edad de forma controlada)
    @property
    def edad(self):
        return self._edad

    # Setter (para modificar la edad con validación)
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
            print(f"Edad actualizada a {nueva_edad} años")
        else:
            print("Edad no puede ser negativa")

# Uso
p = Persona("Carlos", 25)

print(p.edad)           # 25 (usa el getter automáticamente)
p.edad = 30             # Edad actualizada a 30 años (usa el setter)
print(p.edad)           # 30

p.edad = -5             # Edad no puede ser negativa
print(p.edad)           # Sigue siendo 30 (no se modificó)
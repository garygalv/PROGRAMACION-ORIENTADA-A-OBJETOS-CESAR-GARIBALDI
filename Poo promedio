# Programa para calcular el promedio semanal de temperaturas
# Usando Programación Orientada a Objetos (POO)
# Se aplica encapsulamiento (atributos privados con _)
# Autor: [Cesar Garibaldi]
# Fecha: 14/12/2025

class DiaClima:
    """
    Clase que representa el clima de un día específico.
    Encapsula el nombre del día y la temperatura.
    """
    def __init__(self, dia):
        self._dia = dia                    # Atributo encapsulado (protegido)
        self._temperatura = 0.0            # Atributo encapsulado
    
    def ingresar_temperatura(self):
        """Método para ingresar la temperatura del día con validación."""
        while True:
            try:
                temp = float(input(f"{self._dia}: "))
                self._temperatura = temp
                break
            except ValueError:
                print("Error: Ingrese un número válido.")
    
    def obtener_temperatura(self):
        """Método getter para obtener la temperatura (encapsulamiento)."""
        return self._temperatura
    
    def __str__(self):
        return f"{self._dia}: {self._temperatura} °C"

class SemanaClima:
    """
    Clase que representa una semana completa de clima.
    Contiene 7 objetos de DiaClima y métodos para calcular el promedio.
    """
    def __init__(self):
        dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        self._dias_clima = [DiaClima(dia) for dia in dias]  # Composición de objetos
    
    def ingresar_datos(self):
        """Método para ingresar temperaturas de todos los días."""
        print("Ingrese las temperaturas diarias (en °C):")
        for dia in self._dias_clima:
            dia.ingresar_temperatura()
    
    def calcular_promedio(self):
        """Método que calcula y retorna el promedio semanal."""
        temperaturas = [dia.obtener_temperatura() for dia in self._dias_clima]
        return sum(temperaturas) / len(temperaturas)
    
    def mostrar_resultado(self):
        """Método para mostrar todas las temperaturas y el promedio."""
        print("\n" + "="*50)
        print("Temperaturas de la semana:")
        for dia in self._dias_clima:
            print(dia)
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal es: {promedio:.2f} °C")
        print("="*50)

def main():
    print("=== Cálculo de Promedio Semanal del Clima (POO) ===\n")
    
    semana = SemanaClima()
    semana.ingresar_datos()
    semana.mostrar_resultado()

# Ejecutar el programa
if __name__ == "__main__":
    main()
# clima_poo.py
# Programa que calcula el promedio semanal usando POO

class ClimaSemanal:
    """
    Clase que representa el clima de una semana.
    Aplica encapsulamiento con atributos privados.
    """
    
    def __init__(self):
        # Atributo privado para almacenar las temperaturas
        self.__temperaturas = []
        self.__dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def ingresar_temperatura(self, dia: int, temp: float):
        """
        Ingresa la temperatura de un día específico.
        dia: número del día (1 a 7)
        """
        if 1 <= dia <= 7:
            if len(self.__temperaturas) < dia:
                # Rellenamos con None si faltan días anteriores
                self.__temperaturas.extend([None] * (dia - len(self.__temperaturas)))
            self.__temperaturas[dia - 1] = temp
        else:
            print("Día inválido. Debe ser entre 1 y 7.")

    def obtener_promedio(self) -> float:
        """
        Calcula y retorna el promedio semanal.
        Solo considera los días ingresados.
        """
        temps_validas = [t for t in self.__temperaturas if t is not None]
        if not temps_validas:
            return 0.0
        return sum(temps_validas) / len(temps_validas)

    def mostrar_reporte(self):
        """
        Muestra un reporte completo con temperaturas y promedio.
        """
        print("\n" + "="*50)
        print("Reporte Semanal - Programación Orientada a Objetos")
        print("="*50)
        
        for i, temp in enumerate(self.__temperaturas):
            dia = self.__dias[i]
            if temp is not None:
                print(f"{dia}: {temp:.1f} °C")
            else:
                print(f"{dia}: No ingresada")
        
        promedio = self.obtener_promedio()
        print("-"*50)
        print(f"Promedio semanal: {promedio:.2f} °C")
        print("="*50)

def main():
    print("=== Cálculo de promedio semanal - POO ===\n")
    
    clima = ClimaSemanal()
    
    print("Ingrese las temperaturas de la semana (puede omitir días):")
    for i in range(7):
        dia = i + 1
        while True:
            try:
                temp = input(f"{clima._ClimaSemanal__dias[i]} (deje en blanco para omitir): ")
                if temp.strip() == "":
                    break
                clima.ingresar_temperatura(dia, float(temp))
                break
            except ValueError:
                print("Por favor, ingrese un número válido o deje en blanco.")
    
    clima.mostrar_reporte()

if __name__ == "__main__":
    main()
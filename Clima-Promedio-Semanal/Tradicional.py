# clima_tradicional.py
# Programa que calcula el promedio semanal de temperaturas usando programación tradicional (funciones)

def obtener_temperaturas():
    """
    Solicita al usuario las temperaturas de 7 días.
    Retorna una lista con las 7 temperaturas.
    """
    temperaturas = []
    print("Ingrese las temperaturas de la semana (7 días):")
    for dia in range(1, 8):
        while True:
            try:
                temp = float(input(f"Día {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Calcula y retorna el promedio de una lista de temperaturas.
    """
    if not temperaturas:
        return 0
    return sum(temperaturas) / len(temperaturas)

def mostrar_resultado(promedio):
    """
    Muestra el promedio semanal con formato claro.
    """
    print("\n" + "="*40)
    print(f"Promedio semanal de temperaturas: {promedio:.2f} °C")
    print("="*40)

def main():
    print("=== Cálculo de promedio semanal - Programación Tradicional ===\n")
    temps = obtener_temperaturas()
    promedio = calcular_promedio(temps)
    mostrar_resultado(promedio)

if __name__ == "__main__":
    main()
# PROGRAMACION-ORIENTADA-A-OBJETOS-CESAR-GARIBALDI
SEGUNDO SEMETRE UEA PARALELO D
# Comparación: Programación Tradicional vs POO en Python

## Programación Tradicional (Procedural)
- **Estructura**: Basada en funciones independientes que operan sobre datos (listas).
- **Ventajas**:
  - Código más simple y directo.
  - Fácil de entender para programas pequeños.
  - Menos líneas de código en casos básicos.
- **Desventajas**:
  - Los datos y funciones están separados → difícil mantener en programas grandes.
  - Menos reutilizable si se quiere extender (ej. agregar más datos por día).

## Programación Orientada a Objetos (POO)
- **Estructura**: Datos y comportamientos agrupados en clases (encapsulamiento).
- **Conceptos aplicados**:
  - **Encapsulamiento**: Atributos privados (`_temperatura`) accesibles solo por métodos.
  - **Composición**: La clase `SemanaClima` contiene objetos `DiaClima`.
  - **Abstracción**: Métodos claros como `calcular_promedio()`.
- **Ventajas**:
  - Código más organizado, modular y mantenible.
  - Fácil de extender (podríamos agregar herencia, ej. clase para pronóstico).
  - Mejor representa entidades del mundo real (un "día" con su temperatura).
- **Desventajas**:
  - Más código para problemas simples.
  - Curva de aprendizaje inicial mayor.

## Conclusión
La programación tradicional es ideal para scripts rápidos y simples.  
La POO brilla en proyectos grandes, donde la organización, reutilización y mantenimiento son clave.  
Ambos paradigmas son válidos en Python, que es multiparadigma.

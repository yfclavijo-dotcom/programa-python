"""
Problema 1: Evaluación del nivel de compromiso de sesiones de clientes
Curso: Programación - Fase 5 (Evaluación Final POA)
Universidad Nacional Abierta y a Distancia (UNAD)
"""


def clasificar_compromiso(duracion: int, clics: int) -> str:
    """
    Calcula la clasificación de compromiso de una sesión según su duración
    (en segundos) y el número de clics realizados.

    Parámetros:
        duracion (int): Duración de la sesión en segundos.
        clics (int): Cantidad de clics registrados en la sesión.

    Retorna:
        str: Nivel de compromiso ("Alto", "Medio" o "Bajo").
    """
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


def generar_informe(matriz_sesiones: list) -> None:
    """
    Recorre la matriz de sesiones e imprime en consola un informe
    con el ID de cada cliente y su clasificación final de compromiso.
    """
    print("=" * 44)
    print("     INFORME DE COMPROMISO DE CLIENTES")
    print("=" * 44)
    print(f"{'ID Cliente':<18} | {'Nivel de Compromiso':<20}")
    print("-" * 44)

    for sesion in matriz_sesiones:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]

        nivel = clasificar_compromiso(duracion, clics)
        print(f"{id_cliente:<18} | {nivel:<20}")

    print("=" * 44)


# Datos iniciales: Matriz con formato [ID del Cliente, Duración (s), Número de clics]
sesiones_clientes = [
    ["CLI-101", 240, 12],  # Alto: duración > 180 y clics > 8
    ["CLI-102", 45, 5],    # Bajo: duración < 60
    ["CLI-103", 150, 6],   # Medio: caso intermedio
    ["CLI-104", 200, 2],   # Bajo: clics < 3
    ["CLI-105", 180, 9],   # Medio: duración igual a 180 (no estrictamente > 180)
    ["CLI-106", 310, 15],  # Alto: duración > 180 y clics > 8
]


if __name__ == "__main__":
    generar_informe(sesiones_clientes)
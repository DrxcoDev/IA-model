import numpy as np
import random

# Generar un mapa aleatorio con valores entre 0 y 10
game_map = [random.randint(0, 10) for _ in range(12)]

# Imprimir el mapa con símbolos
for index, block in enumerate(game_map):
    symbol = '.' if block > 5 else '+'
    print(symbol, end=' ')

    # Salto de línea cada 4 elementos para mantener la forma de la cuadrícula
    if (index + 1) % 4 == 0:
        print()

# Mostrar los valores generados para referencia
print("\nValores del mapa:", game_map)

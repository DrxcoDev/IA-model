import numpy as np
import random


def random_terrain(x):
    if 0 < 1:
        for index, block in enumerate(x):
            symbol = '.' if block > 5 else '+'
            print(symbol, end=' ')


            if (index + 1) % 4 == 0:
                print()
                
        print("\nValores del mapa:", x)

if __name__ == "__main__":
    game_map = [random.randint(0, 10) for _ in range(12)]
    random_terrain(game_map)



import random


def generar_array_sin_repeticion(max_mount,limit):
    random_mount = random.sample(range(1, max_mount + 1), max_mount)
    return random_mount[:limit]

import time

def barra_carga(part, total, tamano = 30):
    frac = part / total
    completed = int(frac * tamano)
    missing = tamano - completed
    bar = f"[{'*'*completed}{'-'*missing}]{frac:.2%}"
    print(bar)

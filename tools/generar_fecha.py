from datetime import datetime, timedelta
import random

def obtener_fecha_random(ano_inicial,año_final):
    fecha_inicial = datetime(ano_inicial, 1, 1)
    fecha_final = datetime(año_final,12,31)
    
    diferencia = fecha_final - fecha_inicial
    
    random_dias = random.randint(0, diferencia.days)
    
    random_fecha = fecha_inicial + timedelta(days=random_dias)
    
    return random_fecha

def obtener_fecha_hora_random(ano_inicial,año_final):
    fecha_inicial = datetime(ano_inicial, 1, 1)
    fecha_final = datetime(año_final,12,31)
    
    diferencia = fecha_final - fecha_inicial
    
    random_dias = random.randint(0, diferencia.days)
    
    random_fecha = fecha_inicial + timedelta(days=random_dias)
    
    # Generar una hora al azar entre 0 y 23 (horas enteras)
    random_hora = random.randint(0, 23)
    
    random_fecha_hora = random_fecha.replace(hour=random_hora, minute=0, second=0, microsecond=0)
    
    return random_fecha_hora
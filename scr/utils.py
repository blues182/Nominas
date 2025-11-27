# src/utils.py

from datetime import datetime

def convertir_hora(hora_str):
    """
    Convierte una cadena de hora (formato 'HH:MM') a un objeto datetime.
    """
    return datetime.strptime(hora_str, '%H:%M')

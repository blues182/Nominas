# src/procesamiento.py

from datetime import datetime, timedelta

def calcular_nomina(df):
    """
    Calcula la nómina, horas normales, horas extras, deducciones, etc.
    """
    # Convertir las horas de entrada y salida a tipo datetime
    df['Hora entrada'] = pd.to_datetime(df['Hora entrada'], format='%H:%M')
    df['Hora salida'] = pd.to_datetime(df['Hora salida'], format='%H:%M')
    
    # Calcular horas trabajadas
    df['Horas trabajadas'] = (df['Hora salida'] - df['Hora entrada']).dt.total_seconds() / 3600
    
    # Lógica para horas extras, deducciones y otros cálculos
    df['Pago total'] = df.apply(calcular_pago, axis=1)
    
    return df

def calcular_pago(row):
    """
    Calcula el pago total para cada empleado considerando horas extras, tardanza y demás reglas.
    """
    horas_normales = 8  # Horas normales de trabajo en días de semana
    pago_base = row['Sueldo base mensual'] / 30 / horas_normales  # Pago por hora base
    
    # Supongamos que si trabajó horas extras
    if row['Horas trabajadas'] > horas_normales:
        horas_extras = row['Horas trabajadas'] - horas_normales
        pago_total = (horas_normales * pago_base) + (horas_extras * pago_base * 1.5)
    else:
        pago_total = row['Horas trabajadas'] * pago_base
    
    # Si trabajó horas extras en sábado, se paga doble
    if row['Dia'] == 'Sábado':
        pago_total *= 2
    
    # Si trabajó horas extras en domingo, se paga 2.5X
    if row['Dia'] == 'Domingo':
        pago_total *= 2.5
    
    # Si llega tarde, se le hacen deducciones (por ejemplo, 1.5X en Recursos Humanos y Finanzas)
    if row['Tarde']:
        deduccion = row['Tarde horas'] * pago_base * 1.5
        pago_total -= deduccion
    
    return pago_total

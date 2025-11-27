# tests/test_processing.py

import pytest
import pandas as pd
from src.procesamiento import calcular_nomina

# Crear un DataFrame de ejemplo para las pruebas
@pytest.fixture
def ejemplo_df():
    data = {
        'Nombre': ['Juan', 'Ana', 'Pedro'],
        'Sueldo base mensual': [30000, 25000, 28000],
        'Hora entrada': ['08:00', '08:00', '08:00'],
        'Hora salida': ['17:00', '18:00', '16:00'],
        'Dia': ['Lunes', 'Martes', 'Miércoles'],
        'Tarde': [False, False, True],
        'Tarde horas': [0, 0, 1]
    }
    return pd.DataFrame(data)

def test_calcular_nomina(ejemplo_df):
    # Calcula la nómina con la función de procesamiento
    df_calculado = calcular_nomina(ejemplo_df)

    # Verifica que el cálculo del pago total sea correcto
    assert df_calculado['Pago total'].iloc[0] == 30000 / 30 / 8 * 8  # El primer empleado no tiene horas extras
    assert df_calculado['Pago total'].iloc[1] == 25000 / 30 / 8 * 9  # Segundo empleado tiene horas extras
    assert df_calculado['Pago total'].iloc[2] == 28000 / 30 / 8 * 8 + (1 * 28000 / 30 / 8 * 1.5)  # Tercer empleado con tardanza

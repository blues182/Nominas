# tests/test_excel_handler.py

import pytest
import pandas as pd
from src.excel_handler import cargar_datos, guardar_datos
from io import BytesIO

def test_cargar_datos():
    # Simular un archivo Excel en memoria
    data = {'Nombre': ['Juan', 'Ana'], 'Sueldo base mensual': [30000, 25000]}
    df = pd.DataFrame(data)
    with BytesIO() as b:
        df.to_excel(b, index=False, engine='openpyxl')
        b.seek(0)
        # Verifica que se pueda cargar el archivo correctamente
        result = cargar_datos(b)
        assert result.equals(df)  # Compara el DataFrame cargado con el original

def test_guardar_datos():
    # Crear un DataFrame de prueba
    data = {'Nombre': ['Juan', 'Ana'], 'Sueldo base mensual': [30000, 25000]}
    df = pd.DataFrame(data)
    # Verificar que guardar_datos no lance excepciones
    try:
        output = guardar_datos(df)
        assert isinstance(output, bytes)  # Asegúrate de que el archivo es devuelto como bytes
    except Exception as e:
        pytest.fail(f"Error al guardar datos: {e}")

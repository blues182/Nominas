# src/excel_handler.py

import pandas as pd
import io

def cargar_datos(archivo):
    """
    Carga los datos desde el archivo Excel.
    """
    try:
        # Leer el archivo Excel con pandas
        df = pd.read_excel(archivo)
        return df
    except Exception as e:
        raise Exception(f"Error al cargar el archivo Excel: {e}")

def guardar_datos(df):
    """
    Guarda los datos procesados en un archivo Excel y devuelve el archivo en formato bytes.
    """
    try:
        # Guardar el DataFrame en un buffer de memoria (en lugar de un archivo en disco)
        output = io.BytesIO()
        df.to_excel(output, index=False, engine='openpyxl')
        output.seek(0)
        return output.getvalue()  # Retorna el archivo Excel en formato bytes
    except Exception as e:
        raise Exception(f"Error al guardar el archivo Excel: {e}")

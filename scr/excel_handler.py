# src/excel_handler.py

import pandas as pd

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
    Guarda los datos procesados en un archivo Excel nuevo.
    """
    try:
        df.to_excel('nomina_calculada.xlsx', index=False)
    except Exception as e:
        raise Exception(f"Error al guardar el archivo Excel: {e}")

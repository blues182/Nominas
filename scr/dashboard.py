# src/dashboard.py

import streamlit as st
import pandas as pd
from src.excel_handler import cargar_datos, guardar_datos
from src.procesamiento import calcular_nomina

def mostrar_dashboard():
    """
    Muestra la interfaz de usuario para cargar el archivo Excel, mostrar los resultados
    y permitir la descarga del archivo procesado.
    """
    st.title("Aplicación de Cálculo de Nómina Semanal")

    # Cargar el archivo Excel
    archivo = st.file_uploader("Sube el archivo Excel de empleados", type=["xlsx"])

    if archivo is not None:
        # Leer los datos del archivo cargado
        try:
            df = cargar_datos(archivo)
            st.write("Datos cargados correctamente:")
            st.dataframe(df.head())  # Muestra las primeras filas del archivo cargado

            # Procesar la nómina
            df_calculado = calcular_nomina(df)

            # Mostrar los resultados calculados
            st.write("Nómina calculada:")
            st.dataframe(df_calculado)

            # Descargar el archivo con los resultados calculados
            st.download_button(
                label="Descargar archivo con resultados",
                data=guardar_datos(df_calculado),  # Exportar el archivo procesado
                file_name="nomina_calculada.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        except Exception as e:
            st.error(f"Error al procesar el archivo: {e}")

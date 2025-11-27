# src/dashboard.py

import streamlit as st

def mostrar_dashboard(df):
    """
    Muestra los resultados de la nómina en un dashboard con Streamlit.
    """
    st.title("Dashboard de Nómina")
    
    # Mostrar tabla con los datos calculados
    st.write("Nómina Calculada:")
    st.dataframe(df)
    
    # Aquí puedes agregar gráficos, resúmenes u otros análisis que desees visualizar
    st.write(f"Total a pagar: {df['Pago total'].sum():,.2f} MXN")

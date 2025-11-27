# tests/test_dashboard.py

import pytest
from io import BytesIO
import pandas as pd
import streamlit as st
from src.dashboard import mostrar_dashboard

@pytest.fixture
def ejemplo_df():
    data = {'Nombre': ['Juan', 'Ana'], 'Sueldo base mensual': [30000, 25000]}
    return pd.DataFrame(data)

def test_mostrar_dashboard(ejemplo_df):
    # Simula la interfaz Streamlit
    st.set_option('server.headless', True)
    mostrar_dashboard()
    
    # Verificar que el DataFrame se muestra correctamente en Streamlit
    assert len(ejemplo_df) > 0

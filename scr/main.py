# src/main.py

from src.excel_handler import cargar_datos, guardar_datos
from src.procesamiento import calcular_nomina
from src.dashboard import mostrar_dashboard

def main():
    """
    Función principal que coordina la carga, procesamiento y visualización de los datos.
    """
    # Solicitar al usuario el nombre del archivo Excel
    archivo = input("Introduce el nombre del archivo Excel (ejemplo: empleados.xlsx): ")
    
    try:
        # Cargar los datos desde el archivo Excel
        print("Cargando los datos desde el archivo...")
        df = cargar_datos(archivo)
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return
    
    # Procesar la nómina: calcular horas trabajadas, horas extras, deducciones, etc.
    print("Procesando la nómina...")
    try:
        df_calculado = calcular_nomina(df)
    except Exception as e:
        print(f"Error en el cálculo de la nómina: {e}")
        return
    
    # Mostrar el dashboard con los resultados
    print("Mostrando el dashboard...")
    mostrar_dashboard(df_calculado)
    
    # Guardar el archivo con los resultados calculados
    print("Guardando los resultados en un archivo Excel...")
    try:
        guardar_datos(df_calculado)
        print("Los resultados se han guardado correctamente en 'nomina_calculada.xlsx'")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        return

if __name__ == "__main__":
    # Ejecutar la aplicación
    main()

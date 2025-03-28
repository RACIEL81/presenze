import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

# Configuración de la conexión a MySQL
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "123456"
DB_NAME = "mi_base_de_datos"
TABLE_NAME = "mi_tabla"

# Ruta del archivo Excel (CORREGIDA)
ARCHIVO_EXCEL = r"C:\Users\eamd2\Desktop\presenze-1.xlsx"

# Leer datos desde el archivo Excel
def cargar_datos_excel(ruta_excel):
    try:
        df = pd.read_excel(ruta_excel, engine='openpyxl')
        print("Datos cargados correctamente desde Excel.")
        return df
    except Exception as e:
        print(f"Error al leer el archivo Excel: {e}")
        return None

# Subir datos a MySQL
def subir_datos_mysql(df):
    try:
        engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")
        df.to_sql(TABLE_NAME, con=engine, if_exists='replace', index=False)
        print("Datos subidos correctamente a MySQL.")
    except Exception as e:
        print(f"Error al subir datos a MySQL: {e}")

# Ejecutar el proceso
def main():
    df = cargar_datos_excel(ARCHIVO_EXCEL)
    if df is not None:
        subir_datos_mysql(df)

if __name__ == "__main__":
    main()

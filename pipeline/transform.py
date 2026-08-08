import pandas as pd
import logging

def transformar_ventas(ventas):

    ventas['fecha'] = pd.to_datetime(ventas['fecha'], errors='coerce')
    ventas['unidades'] = pd.to_numeric(ventas['unidades'], errors='coerce')
    ventas['precio_unitario'] = pd.to_numeric(ventas['precio_unitario'], errors='coerce')

    total_invalidos = ventas[['fecha', 'unidades', 'precio_unitario']].isna().any(axis=1).sum()

    ventas = ventas.dropna(subset=['fecha', 'unidades', 'precio_unitario'])
    
    total_duplicados = ventas.duplicated().sum()
    ventas = ventas.drop_duplicates()

    ventas = ventas.reset_index(drop=True)
    
    if total_invalidos > 0:
        logging.warning(f"se eliminaron {total_invalidos} registros invalidos de ventas.")

    if total_duplicados > 0:
        logging.warning(f"se eliminaron {total_duplicados} duplicados de ventas")

    return ventas



def transformar_datos(datos):
    ventas = datos['ventas']

    ventas = transformar_ventas(ventas)

    datos['ventas'] = ventas

    return datos
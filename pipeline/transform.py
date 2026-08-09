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

def transformar_clientes(clientes):
    clientes['cliente'] = clientes['cliente'].str.strip().str.title()

    clientes['ciudad'] = clientes['ciudad'].str.strip().str.title()

    clientes['segmento'] = clientes['segmento'].str.strip().str.title()
    clientes['segmento'] = clientes['segmento'].fillna('Sin Segmento')


    return clientes

def transformar_productos(productos):
    productos['producto'] = productos['producto'].str.strip().str.title()
    productos['categoria'] = productos['categoria'].str.strip().str.title()
    productos['costo_unitario'] = pd.to_numeric(productos['costo_unitario'], errors='coerce')

    total_invalidos = productos['costo_unitario'].isna().sum()

    productos = productos.dropna(subset=['costo_unitario'])

    productos = productos.reset_index(drop=True)

    if total_invalidos > 0:
        logging.warning(f"Se eliminaron {total_invalidos} con costo_unitario invalido")

    return productos

def transformar_datos(datos):
    ventas = datos["ventas"]
    ventas = transformar_ventas(ventas)
    datos["ventas"] = ventas

    clientes = datos["clientes"]
    clientes = transformar_clientes(clientes)
    datos["clientes"] = clientes

    productos = datos["productos"]
    productos = transformar_productos(productos)
    datos["productos"] = productos

    return datos
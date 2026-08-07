import pandas as pd
import logging

def cargar_datos():
    try:
        ventas = pd.read_csv('data/input/ventas.csv')
        logging.info("Datos de ventas cargados correctamente.")
    except FileNotFoundError:
        logging.error("Archivo de ventas no encontrado.")
        ventas = None

    try:
        clientes = pd.read_csv('data/input/clientes.csv')
        logging.info("Datos de clientes cargados correctamente.")
    except FileNotFoundError:
        logging.error("Archivo de clientes no encontrado.")
        clientes = None

    try:
        productos = pd.read_csv('data/input/productos.csv')
        logging.info("Datos de productos cargados correctamente.")
    except FileNotFoundError:
        logging.error("Archivo de productos no encontrado.")
        productos = None

    if ventas is None or clientes is None or productos is None:
        logging.error("Error al cargar los datos. Verifique los archivos.")
        return None
    
    return {
        "ventas": ventas,
        "clientes": clientes,
        "productos": productos
    }
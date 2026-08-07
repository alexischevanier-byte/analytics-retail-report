import pandas as pd
import logging  

def validar_columnas(df, columnas_requeridas, nombre_archivo):
    columnas_presentes = df.columns.tolist()

    columnas_faltantes = []

    for columna in columnas_requeridas:
        if columna not in columnas_presentes:
            columnas_faltantes.append(columna)

    if columnas_faltantes:
        logging.error(f"Columnas faltantes en {nombre_archivo} : {columnas_faltantes}")
        return False

    logging.info(f"Todas las columnas requeridas están presentes en {nombre_archivo}.")
    return True

def validar_nulos(df, columnas_criticas, nombre_archivo):
    columnas_con_nulos = []

    for columna in columnas_criticas:
        if df[columna].isnull().any():
            columnas_con_nulos.append(columna)

    if columnas_con_nulos:
        logging.error(f"Columnas criticas con valores nulos en {nombre_archivo} : {columnas_con_nulos}")
        return False

    logging.info(f"No se encontraron valores nulos criticos en {nombre_archivo}.")
    return True


def validar_datos(datos):
    validaciones = {
        "ventas": ["id_venta","fecha","id_cliente","id_producto","unidades","precio_unitario"],
        "clientes": ["id_cliente","cliente","ciudad","segmento"],
        "productos": ["id_producto","producto","categoria","costo_unitario"]
    }

    validacion_correcta = True

    for nombre_archivo, columnas_requeridas in validaciones.items():

        if nombre_archivo not in datos:
            logging.error(f"Datos de {nombre_archivo} no encontrados.")
            validacion_correcta = False
            continue

        if not validar_columnas(datos[nombre_archivo], columnas_requeridas, nombre_archivo):
            validacion_correcta = False
            continue

        if not validar_nulos(datos[nombre_archivo]):
            validacion_correcta = False

    return validacion_correcta

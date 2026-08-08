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
        logging.warning(f"Columnas con valores nulos en {nombre_archivo} : {columnas_con_nulos}")
        return True

    logging.info(f"No se encontraron valores nulos criticos en {nombre_archivo}.")
    return True

def validar_nulos_no_criticos(df, columnas_no_criticas,nombre_archivo):
    columnas_con_nulos = []

    for columna in columnas_no_criticas:
        if df[columna].isnull().any():
            columnas_con_nulos.append(columna)
    
    if columnas_con_nulos:
        logging.warning(f"Valores nulos no criticos en {nombre_archivo} : {columnas_con_nulos}")
    return True

def validar_numericos(df, columnas_numericas, nombre_archivo):
    columnas_con_error = []

    for columna in columnas_numericas:
        serie_numerica = pd.to_numeric(df[columna], errors='coerce')
        valores_invalidos = df[columna].notna() & serie_numerica.isna()

        if valores_invalidos.any():
            columnas_con_error.append(columna)

    if columnas_con_error:
        logging.warning(f"Tipo incorrecto en {nombre_archivo} : {columnas_con_error}")
        return True

    logging.info(f"Todas las columnas numericas son validas en {nombre_archivo}.")
    return True

def validar_fechas(df, columnas_fecha, nombre_archivo):
    columnas_con_error = []

    for columna in columnas_fecha:
        fecha_convertida = pd.to_datetime(df[columna], errors='coerce')
        valores_invalidos = df[columna].notna() & fecha_convertida.isna()

        if valores_invalidos.any():
            columnas_con_error.append(columna)

    if columnas_con_error:
        logging.warning(f"Tipo incorrecto en {nombre_archivo} : {columnas_con_error}")
        return True
    
    logging.info(f"Todas las columnas de fecha son validas en {nombre_archivo}.")
    return True

def validar_duplicados(df, nombre_archivo):
    total_duplicados = df.duplicated().sum()
    if total_duplicados > 0:
        logging.warning(f"Existen {total_duplicados} filas duplicadas en {nombre_archivo}.")
    else:
        logging.info(f"No existen filas duplicadas en {nombre_archivo}.")



def validar_datos(datos):
    validaciones = {
        "ventas": [
            "id_venta",
            "fecha",
            "id_cliente",
            "id_producto",
            "unidades",
            "precio_unitario"
        ],
        "clientes": [
            "id_cliente",
            "cliente",
            "ciudad",
            "segmento"
        ],
        "productos": [
            "id_producto",
            "producto",
            "categoria",
            "costo_unitario"
        ]
    }

    columnas_criticas = {
        "ventas": [
            "id_venta",
            "fecha",
            "id_cliente",
            "id_producto",
            "unidades",
            "precio_unitario"
        ],
        "clientes": [
            "id_cliente"
        ],
        "productos": [
            "id_producto",
            "costo_unitario"
        ]
    }

    columnas_no_criticas = {
    "ventas": [],
    "clientes": ["cliente", "ciudad", "segmento"],
    "productos": ["producto", "categoria"]
}

    columnas_numericas = {
    "ventas": [
        "unidades",
        "precio_unitario"
    ],
    "clientes": [],
    "productos": [
        "costo_unitario"
    ]
}

    columnas_fecha = {
    "ventas": [
        "fecha"
    ],
    "clientes": [],
    "productos": []
}

    validacion_correcta = True

    for nombre_archivo, columnas_requeridas in validaciones.items():

        if nombre_archivo not in datos:
            logging.error(f"Datos de {nombre_archivo} no encontrados.")
            validacion_correcta = False
            continue

        if not validar_columnas(
            datos[nombre_archivo],
            columnas_requeridas,
            nombre_archivo
        ):
            validacion_correcta = False
            continue

        validar_nulos(
            datos[nombre_archivo],
            columnas_criticas[nombre_archivo],
            nombre_archivo
        )


        validar_nulos_no_criticos(
            datos[nombre_archivo],
            columnas_no_criticas[nombre_archivo],
            nombre_archivo
        )

        validar_numericos(
            datos[nombre_archivo],
            columnas_numericas[nombre_archivo],
            nombre_archivo
        )
        validar_fechas(
            datos[nombre_archivo],
            columnas_fecha[nombre_archivo],
            nombre_archivo
        )

        validar_duplicados(
            datos[nombre_archivo],
            nombre_archivo
        )


    return validacion_correcta
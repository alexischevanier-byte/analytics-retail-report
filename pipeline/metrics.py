import logging

def calcular_ventas_totales(dataset_completo):
    ventas_totales = (dataset_completo['unidades'] * dataset_completo['precio_unitario']).sum()
    return ventas_totales

def calcular_unidades_vendidas(dataset_completo):
    unidades_vendidas = (dataset_completo['unidades']).sum()
    return unidades_vendidas

def calcular_costo_total(dataset_completo):
    costo_total = (dataset_completo['unidades'] * dataset_completo['costo_unitario']).sum()
    return costo_total

def calcular_utilidad(dataset_completo):
    ventas_totales = calcular_ventas_totales(dataset_completo)
    costo_total = calcular_costo_total(dataset_completo)
    utilidad = ventas_totales - costo_total
    return utilidad

def calcular_margen(dataset_completo):
    ventas_totales = calcular_ventas_totales(dataset_completo)
    utilidad = calcular_utilidad(dataset_completo)

    if ventas_totales != 0:
        margen = (utilidad / ventas_totales) * 100
        return margen
    else:
        return 0

def calcular_ticket_promedio(dataset_completo):
    ventas_totales = calcular_ventas_totales(dataset_completo)
    cantidad_transacciones = dataset_completo['id_venta'].nunique()

    if cantidad_transacciones != 0:
        ticket_promedio = ventas_totales / cantidad_transacciones
        return ticket_promedio
    else:
        return 0

def calcular_ventas_por_categoria(dataset_completo):
    ventas_por_categoria = (dataset_completo['unidades'] * dataset_completo['precio_unitario']).groupby(dataset_completo['categoria']).sum()
    return ventas_por_categoria

def calcular_ventas_por_segmento(dataset_completo):
    ventas_por_segmento = (dataset_completo['unidades'] * dataset_completo['precio_unitario']).groupby(dataset_completo['segmento']).sum()
    return ventas_por_segmento


def calcular_metricas(dataset_completo):
    ventas_totales = calcular_ventas_totales(dataset_completo)
    unidades_vendidas = calcular_unidades_vendidas(dataset_completo)
    costo_total = calcular_costo_total(dataset_completo)
    utilidad = calcular_utilidad(dataset_completo)
    margen = calcular_margen(dataset_completo)
    ticket_promedio = calcular_ticket_promedio(dataset_completo)
    ventas_por_categoria = calcular_ventas_por_categoria(dataset_completo)
    ventas_por_segmento = calcular_ventas_por_segmento(dataset_completo)

    logging.info("Metricas calculadas correctamente")
    return {
        "ventas_totales": ventas_totales,
        "unidades_vendidas" : unidades_vendidas,
        "costo_total" : costo_total,
        "utilidad" : utilidad,
        "margen" : margen,
        "ticket_promedio" : ticket_promedio,
        "ventas_por_categoria" : ventas_por_categoria,
        "ventas_por_segmento" : ventas_por_segmento
    }
    


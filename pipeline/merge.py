import pandas as pd
import logging



def unir_clientes(ventas,clientes):

    clientes_duplicados = clientes['id_cliente'].duplicated().sum()
    if clientes_duplicados > 0:
        logging.warning(f"existen {clientes_duplicados} clientes duplicados en clientes")

    ventas = ventas.merge(clientes, on='id_cliente', how='left', indicator='estado_merge')
    clientes_desconocidos = (ventas['estado_merge'] == 'left_only').sum()

    if clientes_desconocidos > 0:
        logging.warning(f"hay {clientes_desconocidos} clientes desconocidos en ventas")
        
    ventas.loc[ventas['estado_merge'] == 'left_only', 'cliente'] = 'Cliente Desconocido'
    ventas.loc[ventas['estado_merge'] == 'left_only', 'ciudad'] = 'Ciudad desconocida'
    ventas.loc[ventas['estado_merge'] == 'left_only', 'segmento'] = 'Sin Segmento'

    ventas = ventas.drop(columns=['estado_merge'])

    return ventas

def unir_productos(ventas,productos):

    ventas = ventas.merge(productos, on='id_producto', how='left', indicator='estado_merge')
    productos_desconocidos = (ventas['estado_merge'] == 'left_only').sum()

    if productos_desconocidos > 0:
        logging.warning(f"existen {productos_desconocidos} productos sin informacion")
        ventas = ventas.drop(ventas.loc[ventas['estado_merge'] == 'left_only'])
        ventas = ventas.reset_index(inplace=True)

    return ventas
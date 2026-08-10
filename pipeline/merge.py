import pandas as pd
import logging

def unir_clientes(ventas,clientes):
    ventas = ventas.merge(clientes, on='id_cliente', how='left', indicator='estado_merge')
    clientes_desconocidos = (ventas['estado_merge'] == 'left_only').sum()

    if clientes_desconocidos > 0:
        logging.warning(f"hay {clientes_desconocidos} clientes desconocidos en ventas")
        
    ventas.loc[ventas['estado_merge'] == 'left_only', 'clientes'] = 'Cliente Desconocido'
    ventas.loc[ventas['estado_merge'] == 'left_only', 'ciudad'] = 'Ciudad desconocida'
    ventas.loc[ventas['estado_merge'] == 'left_only', 'segmento'] = 'sin segmento'

import pandas as pd
import logging

def generar_reporte(dataset_completo, metricas):
    df_metricas = pd.DataFrame(
        list(metricas.items()),
        columns=['Metrica', 'Valor']
    )

    ruta_salida = "data/output/analytics_retail_report.xlsx"

    try:
        with pd.ExcelWriter(ruta_salida, engine='openpyxl') as writer:
            dataset_completo.to_excel(
                writer,
                sheet_name='Datos Completos',
                index=False
            )

            df_metricas.to_excel(
                writer,
                sheet_name='Metricas',
                index=False
            )

        logging.info(f"Reporte generado y guardado en: {ruta_salida}")

    except PermissionError:
        logging.error(f"No se puede guardar el archivo en {ruta_salida}. Verifique que el archivo no esté abierto")
        raise SystemExit
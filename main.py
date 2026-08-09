from pipeline.extract import cargar_datos
from pipeline.validate import validar_datos
from pipeline.transform import transformar_datos
import logging

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Iniciando el proceso de carga de datos.")
    datos = cargar_datos()
    if datos is None:
        logging.error("No se pudieron cargar los datos. Terminando el programa.")
        raise SystemExit("Error al cargar los datos. Verifique los archivos de entrada.")

    datos_validos = validar_datos(datos)
    if not datos_validos:
        logging.error("Validación de datos fallida. Terminando el programa.")
        raise SystemExit("Error en la validación de datos. Verifique los archivos de entrada.")

    datos_transformados = transformar_datos(datos)
    print(datos_transformados['ventas'])
    print(datos_transformados['clientes'])
    print(datos_transformados['productos'])

if __name__ == "__main__":
    main()
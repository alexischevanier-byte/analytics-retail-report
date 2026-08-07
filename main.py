from pipeline.extract import cargar_datos
import logging

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Iniciando el proceso de carga de datos.")
    datos = cargar_datos()
    if datos is None:
        logging.error("No se pudieron cargar los datos. Terminando el programa.")
        raise SystemExit("Error al cargar los datos. Verifique los archivos de entrada.")

if __name__ == "__main__":
    main()
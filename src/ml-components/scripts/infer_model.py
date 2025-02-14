import pandas as pd
import logging
import os
import tensorflow as tf
from ml_components.scripts.utils import load_data, preprocess_data, load_config
# Configuración básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def load_model(model_path):
    """Carga un modelo de TensorFlow desde una ruta dada.
    Args:
        model_path (str): Ruta al directorio del modelo.
    Returns:
        tensorflow.keras.Model: El modelo cargado.
    """
    try:
        logging.info(f"Cargando modelo desde {model_path}")
        model = tf.keras.models.load_model(model_path)
        logging.info("Modelo cargado correctamente.")
        return model
    except Exception as e:
        logging.error(f"Error al cargar el modelo: {e}")
        return None
def make_predictions(model, data):
    """Realiza predicciones con el modelo cargado.
    Args:
        model (tensorflow.keras.Model): El modelo cargado.
        data (pandas.DataFrame): DataFrame con los datos para predicción.
    Returns:
        pandas.DataFrame: DataFrame con las predicciones.
    """
    if model is None or data is None:
        logging.error("Modelo o datos no válidos para hacer predicciones.")
        return None
    try:
        logging.info("Realizando predicciones...")
        predictions = model.predict(data)
        predictions_df = pd.DataFrame(predictions, columns=['prediction']) # Ajusta el nombre de la columna según tu modelo
        logging.info("Predicciones realizadas correctamente.")
        return predictions_df
    except Exception as e:
        logging.error(f"Error al realizar las predicciones: {e}")
        return None
def save_predictions(predictions_df, output_path):
    """Guarda las predicciones en un archivo CSV.
    Args:
        predictions_df (pandas.DataFrame): DataFrame con las predicciones.
        output_path (str): Ruta donde se guardará el archivo CSV.
    """
    if predictions_df is None:
        logging.error("No hay predicciones para guardar.")
        return
    try:
        logging.info(f"Guardando predicciones en {output_path}")
        predictions_df.to_csv(output_path, index=False)
        logging.info("Predicciones guardadas correctamente.")
    except Exception as e:
        logging.error(f"Error al guardar las predicciones: {e}")
if __name__ == '__main__':
    # Cargar configuración
    config_path = 'config/inference_config.json' # ruta al archivo de configuración, debe estar en la carpeta config/
    config = load_config(config_path)
    if not config:
        logging.error("No se pudo cargar la configuración. Saliendo.")
        exit()
    # Configuración de paths
    model_path = config.get('model_path', 'ml-components/models/my_model') # Ruta por defecto, puedes usar config['model_path']
    data_path = config.get('data_path', 'ml-components/data/test_data.csv') # Ruta por defecto, puedes usar config['data_path']
    output_path = config.get('output_path', 'ml-components/data/predictions.csv') # Ruta por defecto, puedes usar config['output_path']
    target_column = config.get('target_column', 'target') # Columna objetivo por defecto, puedes usar config['target_column']
    # Cargar datos
    df = load_data(data_path)
    if df is None:
        logging.error("No se pudieron cargar los datos. Saliendo.")
        exit()
    # Preprocesar datos
    X_test_scaled = preprocess_data(df, target_column)[1]
    if X_test_scaled is None:
        logging.error("No se pudieron preprocesar los datos. Saliendo.")
        exit()
    # Cargar modelo
    model = load_model(model_path)
    if model is None:
        logging.error("No se pudo cargar el modelo. Saliendo.")
        exit()
    # Hacer predicciones
    predictions_df = make_predictions(model, X_test_scaled)
    if predictions_df is not None:
       # Guardar predicciones
       save_predictions(predictions_df, output_path)
       logging.info(f"Predicciones guardadas en {output_path}")
    else:
        logging.error("No se pudieron generar predicciones.")
    logging.info("Script de inferencia completado.")

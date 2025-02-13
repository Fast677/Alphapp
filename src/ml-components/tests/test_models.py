import pandas as pd
import tensorflow as tf
import json
import os


def load_test_data(data_path):
    """Carga datos de prueba desde archivos CSV."""
    test_data = []
    for file in os.listdir(data_path):
        if file.endswith('.csv'):
            file_path = os.path.join(data_path, file)
            df = pd.read_csv(file_path)
            test_data.append(df)
    return pd.concat(test_data, ignore_index=True)


def load_metadata(metadata_path):
    """Carga metadatos de los datos de prueba."""
    metadata_file = os.path.join(metadata_path, 'test_data_info.json')
    try:
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)
    except FileNotFoundError:
         metadata = {}
         print(f"No metadata found in: {metadata_file}")
    return metadata


def evaluate_model(model_path, test_data):
    """Evalúa el modelo con los datos de prueba."""
    model = tf.keras.models.load_model(model_path)
    # Aquí iría la lógica para evaluar el modelo, usando 'test_data'
    # Para este ejemplo, solo mostramos las dimensiones de los datos
    print(f"Dimensiones de los datos de prueba: {test_data.shape}")
    # Realizar las pruebas necesarias
    # ejemplo: predictions = model.predict(test_data)
    return None

def main():
    """Función principal para cargar, preprocesar datos y evaluar el modelo"""
    # Rutas a los datos
    base_data_path = 'data/test_data/'
    raw_data_path = os.path.join(base_data_path,'raw')
    processed_data_path = os.path.join(base_data_path,'processed')
    metadata_path = os.path.join(base_data_path,'metadata')

    # Cargar datos de prueba
    test_data = load_test_data(processed_data_path)

    # Cargar metadatos
    metadata = load_metadata(metadata_path)
    print(f"Metadatos de datos de prueba: {metadata}")

    # Ruta al modelo entrenado
    model_path = 'models/my_trained_model'

    # Evaluar el modelo
    evaluate_model(model_path, test_data)



if __name__ == '__main__':
    main()

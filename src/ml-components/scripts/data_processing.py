import pandas as pd
import os
import json


def preprocess_test_data(raw_data_path, processed_data_path, metadata_path):
    """Procesa los datos de prueba y guarda la version preprocesada."""

    # Cargar la metadata
    metadata_file = os.path.join(metadata_path, 'test_data_info.json')
    metadata = {}
    try:
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)
    except FileNotFoundError:
         print(f"No metadata found in: {metadata_file}")

    # Iterar sobre los archivos
    for file in os.listdir(raw_data_path):
        if file.endswith('.csv'):
            raw_file_path = os.path.join(raw_data_path, file)
            df = pd.read_csv(raw_file_path)

            # Preprocesamiento de datos
            # ejemplo, normalizacion de datos
            for col in df.columns:
                if pd.api.types.is_numeric_dtype(df[col]):
                   df[col] = (df[col] - df[col].mean()) / df[col].std()
                   if "numeric_columns" not in metadata:
                       metadata["numeric_columns"] = []
                   metadata["numeric_columns"].append(col)

            # Guardar los datos procesados
            processed_file_name = file.replace('.csv', '_processed.csv')
            processed_file_path = os.path.join(processed_data_path,processed_file_name)
            df.to_csv(processed_file_path, index=False)
            print(f"Archivo preprocesado guardado en: {processed_file_path}")

    # Guardar la metadata
    if metadata:
      try:
          with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=4)
            print(f"Metadata guardada en: {metadata_file}")
      except Exception as e:
            print(f"Error al escribir metadata: {e}")

def main():
    """Funcion principal del script"""
    # Rutas a los datos
    base_data_path = 'data/test_data/'
    raw_data_path = os.path.join(base_data_path,'raw')
    processed_data_path = os.path.join(base_data_path,'processed')
    metadata_path = os.path.join(base_data_path,'metadata')

    # Procesar los datos
    preprocess_test_data(raw_data_path, processed_data_path, metadata_path)

if __name__ == '__main__':
    main()
